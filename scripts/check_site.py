#!/usr/bin/env python3
"""Validate the dependency-free GitHub Pages artifact."""

from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
HTML_FILES = tuple(SITE.rglob("*.html"))
REQUIRED_FILES = (
    SITE / "index.html",
    SITE / "ru" / "index.html",
    SITE / "eval-map" / "index.html",
    SITE / "ru" / "eval-map" / "index.html",
    SITE / "404.html",
    SITE / "assets" / "styles.css",
    SITE / "assets" / "app.js",
    SITE / "assets" / "favicon.svg",
    SITE / "assets" / "og.png",
)


class ReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[tuple[str, str]] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        values = dict(attrs)
        for attribute in ("href", "src"):
            value = values.get(attribute)
            if value:
                self.references.append((attribute, value))


def resolve_reference(document: Path, reference: str) -> Path | None:
    parsed = urlsplit(reference)
    if parsed.scheme or parsed.netloc or reference.startswith(("#", "mailto:", "tel:")):
        return None
    if reference.startswith("/"):
        raise ValueError("root-absolute references break on the /minto/ project path")

    target = (document.parent / unquote(parsed.path)).resolve()
    try:
        target.relative_to(SITE.resolve())
    except ValueError as error:
        raise ValueError("reference escapes the site artifact") from error

    return target / "index.html" if target.is_dir() else target


def main() -> int:
    errors: list[str] = []

    for path in REQUIRED_FILES:
        if not path.is_file():
            errors.append(f"missing required file: {path.relative_to(ROOT)}")

    for path in SITE.rglob("*"):
        if path.is_symlink():
            errors.append(f"symlink is not allowed in Pages artifact: {path.relative_to(ROOT)}")

    for document in HTML_FILES:
        parser = ReferenceParser()
        parser.feed(document.read_text(encoding="utf-8"))

        for attribute, reference in parser.references:
            try:
                target = resolve_reference(document, reference)
            except ValueError as error:
                errors.append(
                    f"{document.relative_to(ROOT)}: {attribute}={reference!r}: {error}"
                )
                continue

            if target is not None and not target.exists():
                errors.append(
                    f"{document.relative_to(ROOT)}: broken {attribute}={reference!r}"
                )

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1

    print(f"Validated {len(HTML_FILES)} HTML files in site/.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
