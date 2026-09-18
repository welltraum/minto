(() => {
  const root = document.documentElement;
  const isRussian = root.lang === "ru";
  const status = document.querySelector(".copy-status");
  let statusTimer;

  // The class is set in the head before first paint. Without JavaScript it is
  // absent, so all five cases and both states of every diagram stay visible.

  const writeClipboard = async (text) => {
    if (navigator.clipboard?.writeText) {
      await navigator.clipboard.writeText(text);
      return;
    }

    const input = document.createElement("textarea");
    input.value = text;
    input.setAttribute("readonly", "");
    input.style.position = "fixed";
    input.style.opacity = "0";
    document.body.append(input);
    input.select();
    document.execCommand("copy");
    input.remove();
  };

  const announce = (message) => {
    if (!status) return;
    window.clearTimeout(statusTimer);
    status.textContent = message;
    statusTimer = window.setTimeout(() => {
      status.textContent = "";
    }, 3200);
  };

  document.querySelectorAll("[data-copy]").forEach((button) => {
    const label = button.querySelector("[data-copy-label]");
    let labelTimer;

    button.addEventListener("click", async () => {
      try {
        await writeClipboard(button.dataset.copy);
        announce(isRussian ? "Скопировано в буфер обмена." : "Copied to clipboard.");

        if (!label) return;

        // Read the original from the dataset, not from the DOM: a second
        // click inside the timeout would otherwise capture "Copied".
        if (label.dataset.copyLabel === "") {
          label.dataset.copyLabel = label.textContent;
        }

        label.textContent = isRussian ? "Готово" : "Copied";
        window.clearTimeout(labelTimer);
        labelTimer = window.setTimeout(() => {
          label.textContent = label.dataset.copyLabel;
        }, 1600);
      } catch {
        announce(
          isRussian
            ? "Не удалось скопировать. Выделите команду вручную."
            : "Could not copy. Select the command manually.",
        );
      }
    });
  });

  const motionPreference = window.matchMedia("(prefers-reduced-motion: reduce)");
  let stopShapeTransitions = () => {};

  const startShapeTransitions = () => {
    stopShapeTransitions();
    stopShapeTransitions = () => {};

    if (motionPreference.matches || !Element.prototype.animate) return;

    const HOLD = 1800;
    const MOVE = 650;
    const CYCLE = (HOLD + MOVE) * 2;
    const SOURCE_HOLD_END = HOLD / CYCLE;
    const TARGET_START = (HOLD + MOVE) / CYCLE;
    const TARGET_HOLD_END = (HOLD + MOVE + HOLD) / CYCLE;
    const EASE = "cubic-bezier(0.16, 1, 0.3, 1)";
    const scenes = [...document.querySelectorAll("[data-shape-transition]")];

    const centre = (rect) => ({
      x: rect.left + rect.width / 2,
      y: rect.top + rect.height / 2,
    });

    // Prefer a one-to-one nearest match. If one state has fewer squares, the
    // remaining units converge on the closest already-used destination.
    const matchNearest = (fromRects, toRects) => {
      const open = toRects.map((_, index) => index);

      return fromRects.map((fromRect) => {
        const candidates = open.length ? open : toRects.map((_, index) => index);
        const from = centre(fromRect);
        let match = candidates[0];
        let distance = Number.POSITIVE_INFINITY;

        candidates.forEach((index) => {
          const to = centre(toRects[index]);
          const nextDistance = Math.hypot(to.x - from.x, to.y - from.y);
          if (nextDistance < distance) {
            match = index;
            distance = nextDistance;
          }
        });

        const openIndex = open.indexOf(match);
        if (openIndex !== -1) open.splice(openIndex, 1);
        return toRects[match];
      });
    };

    const offsetTransform = (fromRect, toRect) => {
      const from = centre(fromRect);
      const to = centre(toRect);
      return `translate(${to.x - from.x}px, ${to.y - from.y}px) scale(0.72)`;
    };

    const controllers = scenes.map((scene) => {
      const source = scene.querySelector('[data-shape-state="source"]');
      const target = scene.querySelector('[data-shape-state="target"]');
      const controller = {
        scene,
        visible: false,
        animations: [],
        size: null,
      };

      const syncPlayback = () => {
        const shouldRun = controller.visible && !document.hidden;
        controller.animations.forEach((animation) => {
          if (shouldRun) animation.play();
          else animation.pause();
        });
        scene.toggleAttribute("data-transition-running", shouldRun);
      };

      const build = () => {
        controller.animations.forEach((animation) => animation.cancel());
        controller.animations = [];
        scene.removeAttribute("data-transition-ready");

        const sourceUnits = [...source.querySelectorAll(".unit")];
        const targetUnits = [...target.querySelectorAll(".unit")];
        const sourceRects = sourceUnits.map((unit) => unit.getBoundingClientRect());
        const targetRects = targetUnits.map((unit) => unit.getBoundingClientRect());
        if (!sourceRects.length || !targetRects.length) return;

        const sourceDestinations = matchNearest(sourceRects, targetRects);
        const targetOrigins = matchNearest(targetRects, sourceRects);

        sourceUnits.forEach((unit, index) => {
          const destination = offsetTransform(sourceRects[index], sourceDestinations[index]);
          controller.animations.push(unit.animate([
            { offset: 0, transform: "none", opacity: 1 },
            { offset: SOURCE_HOLD_END, transform: "none", opacity: 1, easing: EASE },
            { offset: TARGET_START, transform: destination, opacity: 0 },
            { offset: TARGET_HOLD_END, transform: destination, opacity: 0, easing: EASE },
            { offset: 1, transform: "none", opacity: 1 },
          ], { duration: CYCLE, iterations: Infinity, fill: "both" }));
        });

        targetUnits.forEach((unit, index) => {
          const origin = offsetTransform(targetRects[index], targetOrigins[index]);
          controller.animations.push(unit.animate([
            { offset: 0, transform: origin, opacity: 0 },
            { offset: SOURCE_HOLD_END, transform: origin, opacity: 0, easing: EASE },
            { offset: TARGET_START, transform: "none", opacity: 1 },
            { offset: TARGET_HOLD_END, transform: "none", opacity: 1, easing: EASE },
            { offset: 1, transform: origin, opacity: 0 },
          ], { duration: CYCLE, iterations: Infinity, fill: "both" }));
        });

        controller.animations.forEach((animation) => animation.pause());
        scene.setAttribute("data-transition-ready", "");
        const bounds = scene.getBoundingClientRect();
        controller.size = { width: bounds.width, height: bounds.height };
        syncPlayback();
      };

      controller.build = build;
      controller.syncPlayback = syncPlayback;
      build();
      return controller;
    });

    const visibilityObserver = "IntersectionObserver" in window
      ? new IntersectionObserver((entries) => {
          entries.forEach((entry) => {
            const controller = controllers.find(({ scene }) => scene === entry.target);
            if (!controller) return;
            controller.visible = entry.isIntersecting;
            controller.syncPlayback();
          });
        }, { threshold: 0.15 })
      : null;

    controllers.forEach((controller) => {
      if (visibilityObserver) visibilityObserver.observe(controller.scene);
      else {
        controller.visible = true;
        controller.syncPlayback();
      }
    });

    const handleVisibility = () => {
      controllers.forEach((controller) => controller.syncPlayback());
    };
    document.addEventListener("visibilitychange", handleVisibility);

    let resizeFrame;
    const resizeObserver = "ResizeObserver" in window
      ? new ResizeObserver((entries) => {
          const changed = entries
            .map((entry) => controllers.find(({ scene }) => scene === entry.target))
            .filter((controller) => {
              if (!controller?.size) return false;
              const bounds = controller.scene.getBoundingClientRect();
              return Math.abs(bounds.width - controller.size.width) > 0.5
                || Math.abs(bounds.height - controller.size.height) > 0.5;
            });

          if (!changed.length) return;
          window.cancelAnimationFrame(resizeFrame);
          resizeFrame = window.requestAnimationFrame(() => {
            changed.forEach((controller) => controller.build());
          });
        })
      : null;

    controllers.forEach((controller) => resizeObserver?.observe(controller.scene));

    stopShapeTransitions = () => {
      visibilityObserver?.disconnect();
      resizeObserver?.disconnect();
      window.cancelAnimationFrame(resizeFrame);
      document.removeEventListener("visibilitychange", handleVisibility);
      controllers.forEach((controller) => {
        controller.animations.forEach((animation) => animation.cancel());
        controller.scene.removeAttribute("data-transition-ready");
        controller.scene.removeAttribute("data-transition-running");
      });
    };
  };

  startShapeTransitions();
  motionPreference.addEventListener?.("change", startShapeTransitions);

  const tabs = [...document.querySelectorAll("[data-case-tab]")];
  const panels = [...document.querySelectorAll("[data-case-panel]")];

  if (tabs.length && panels.length) {
    const setCase = (name) => {
      tabs.forEach((tab) => {
        const selected = tab.dataset.caseTab === name;
        tab.setAttribute("aria-selected", String(selected));
        tab.setAttribute("tabindex", selected ? "0" : "-1");
      });

      panels.forEach((panel) => {
        panel.hidden = panel.dataset.casePanel !== name;
      });
    };

    // Roles first: aria-selected on an <a> only means anything once the
    // element is a tab.
    document.querySelector("[data-tablist]")?.setAttribute("role", "tablist");

    tabs.forEach((tab) => {
      tab.setAttribute("role", "tab");
      tab.setAttribute("aria-controls", `case-${tab.dataset.caseTab}`);

      tab.addEventListener("click", (event) => {
        event.preventDefault();
        setCase(tab.dataset.caseTab);
        history.replaceState(null, "", tab.hash);
      });

      tab.addEventListener("keydown", (event) => {
        if (!["ArrowDown", "ArrowUp", "ArrowRight", "ArrowLeft"].includes(event.key)) {
          return;
        }

        event.preventDefault();
        const direction = ["ArrowDown", "ArrowRight"].includes(event.key) ? 1 : -1;
        const next = tabs[(tabs.indexOf(tab) + direction + tabs.length) % tabs.length];
        next.focus();
        setCase(next.dataset.caseTab);
      });
    });

    panels.forEach((panel) => {
      panel.setAttribute("role", "tabpanel");
      panel.setAttribute("tabindex", "-1");
    });

    const requested = window.location.hash.replace("#case-", "");
    const initial = tabs.some((tab) => tab.dataset.caseTab === requested)
      ? requested
      : tabs[0].dataset.caseTab;
    setCase(initial);
  }

  const navLinks = [...document.querySelectorAll("[data-section-link]")];
  const observedSections = navLinks
    .map((link) => document.getElementById(link.dataset.sectionLink))
    .filter(Boolean);

  if ("IntersectionObserver" in window && observedSections.length) {
    const sectionObserver = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

        if (!visible) return;

        navLinks.forEach((link) => {
          link.toggleAttribute(
            "aria-current",
            link.dataset.sectionLink === visible.target.id,
          );
        });
      },
      { rootMargin: "-25% 0px -60% 0px", threshold: [0.05, 0.25, 0.5] },
    );

    observedSections.forEach((section) => sectionObserver.observe(section));
  }
})();
