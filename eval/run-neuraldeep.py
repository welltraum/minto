#!/usr/bin/env python3
"""Run one evaluation prompt through NeuralDeep's OpenAI-compatible API."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


RETRYABLE_STATUS = {408, 429, 500, 502, 503}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("model")
    parser.add_argument("prompt", type=Path)
    parser.add_argument("output", type=Path)
    return parser.parse_args()


def retry_delay(error: urllib.error.HTTPError, attempt: int) -> float:
    raw = error.headers.get("Retry-After", "")
    try:
        requested = float(raw)
    except ValueError:
        requested = 2**attempt
    maximum = float(os.environ.get("NEURALDEEP_MAX_RETRY_DELAY", "60"))
    return max(1.0, min(requested, maximum))


def message_text(message: dict[str, object]) -> str:
    content = message.get("content", "")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict) and isinstance(item.get("text"), str):
                parts.append(item["text"])
        return "".join(parts)
    return ""


def main() -> int:
    args = parse_args()
    api_key = os.environ.get("NEURALDEEP_API_KEY")
    if not api_key:
        print("NEURALDEEP_API_KEY is required", file=sys.stderr)
        return 2

    base_url = os.environ.get(
        "NEURALDEEP_BASE_URL", "https://api.neuraldeep.ru/v1"
    ).rstrip("/")
    timeout = float(os.environ.get("NEURALDEEP_TIMEOUT", "300"))
    attempts = int(os.environ.get("NEURALDEEP_ATTEMPTS", "2"))
    max_tokens = int(os.environ.get("NEURALDEEP_MAX_TOKENS", "8192"))
    temperature = float(os.environ.get("NEURALDEEP_TEMPERATURE", "0.1"))

    prompt = args.prompt.read_text(encoding="utf-8")
    payload = json.dumps(
        {
            "model": args.model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": temperature,
            "user": f"minto-eval-{args.model}-{args.prompt.parent.name}-{args.prompt.stem}",
        },
        ensure_ascii=False,
    ).encode("utf-8")

    for attempt in range(1, attempts + 1):
        request = urllib.request.Request(
            f"{base_url}/chat/completions",
            data=payload,
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                result = json.load(response)
            choices = result.get("choices") or []
            if not choices:
                raise ValueError("response has no choices")
            text = message_text(choices[0].get("message") or {}).strip()
            if not text:
                raise ValueError("assistant response is empty")
            args.output.write_text(text + "\n", encoding="utf-8")

            usage = result.get("usage") or {}
            finish_reason = choices[0].get("finish_reason", "unknown")
            print(
                "model={} prompt_tokens={} completion_tokens={} finish_reason={}".format(
                    args.model,
                    usage.get("prompt_tokens", "unknown"),
                    usage.get("completion_tokens", "unknown"),
                    finish_reason,
                ),
                file=sys.stderr,
            )
            return 0
        except urllib.error.HTTPError as error:
            body = error.read().decode("utf-8", errors="replace")[:1000]
            if error.code not in RETRYABLE_STATUS or attempt == attempts:
                print(
                    f"NeuralDeep HTTP {error.code} after attempt {attempt}: {body}",
                    file=sys.stderr,
                )
                return 1
            delay = retry_delay(error, attempt)
            print(
                f"NeuralDeep HTTP {error.code}; retrying in {delay:g}s "
                f"(attempt {attempt}/{attempts})",
                file=sys.stderr,
            )
            time.sleep(delay)
        except (OSError, ValueError, json.JSONDecodeError) as error:
            if attempt == attempts:
                print(
                    f"NeuralDeep request failed after attempt {attempt}: {error}",
                    file=sys.stderr,
                )
                return 1
            delay = min(2**attempt, 30)
            print(
                f"NeuralDeep request error; retrying in {delay}s "
                f"(attempt {attempt}/{attempts}): {error}",
                file=sys.stderr,
            )
            time.sleep(delay)

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
