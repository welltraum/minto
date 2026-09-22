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
  const FLOW_HOLD = 1900;
  const FLOW_MOVE = 1100;
  const FLOW_STAGGER = 320;
  const FLOW_TRAVEL = FLOW_MOVE - FLOW_STAGGER;
  const FLOW_CYCLE = (FLOW_HOLD + FLOW_MOVE) * 2;
  const FLOW_EASE = "cubic-bezier(0.3, 0, 0.2, 1)";
  const FLOW_SETTLE = "cubic-bezier(0.16, 1, 0.3, 1)";
  let stopHeroFlow = () => {};
  let stopShapeTransitions = () => {};

  const startHeroFlow = () => {
    stopHeroFlow();
    stopHeroFlow = () => {};

    const scene = document.querySelector("[data-flow-scene]");
    if (!scene || motionPreference.matches || !Element.prototype.animate) return;

    const layer = scene.querySelector("[data-flow-layer]");
    const styles = getComputedStyle(document.body);
    const palette = {
      ink: styles.getPropertyValue("--mr-ink").trim(),
      weak: styles.getPropertyValue("--mr-line").trim(),
      mustard: styles.getPropertyValue("--mr-mustard").trim(),
      field: styles.getPropertyValue("--mr-field").trim(),
      clear: "rgba(14, 10, 6, 0)",
    };
    const sourceCells = [
      ["weak", 0.44, 0.22], ["weak", 0.54, 0.30], ["weak", 0.64, 0.38],
      ["weak", 0.76, 0.48], ["weak", 0.88, 0.62], ["weak", 0.32, 0.22],
      ["weak", 0.42, 0.30], ["weak", 0.52, 0.40], ["weak", 0.66, 0.52],
      ["weak", 0.80, 0.66], ["ink", 1.68, 1], ["weak", 1.46, 0.82],
      ["ink", 1.28, 0.92], ["ink", 1.10, 1], ["ink", 0.94, 1],
    ].map(([state, scale, opacity]) => ({ state, scale, opacity }));
    const targetCells = [
      { state: "answer" },
      ...Array.from({ length: 2 }, () => ({ state: "ink" })),
      ...Array.from({ length: 4 }, () => ({ state: "ink" })),
      ...Array.from({ length: 7 }, () => ({ state: "ink" })),
      { state: "gap" },
    ];
    const permutation = sourceCells.map((_, index) => (index * 7 + 4) % sourceCells.length);
    const desktopLayout = [
      [0.10, 0.20], [0.22, 0.29], [0.34, 0.38], [0.45, 0.47], [0.56, 0.55],
      [1.01, 0.02], [0.92, 0.10], [0.83, 0.20], [0.74, 0.32], [0.65, 0.46],
      [0.39, 1.03], [0.46, 0.90], [0.53, 0.78], [0.61, 0.68], [0.71, 0.59],
    ];
    const mobileLayout = [
      [-0.06, 0.24], [0.10, 0.34], [0.25, 0.44], [0.39, 0.54], [0.52, 0.63],
      [1.04, 0.04], [0.91, 0.14], [0.79, 0.25], [0.68, 0.38], [0.58, 0.51],
      [0.02, 1.03], [0.15, 0.88], [0.28, 0.75], [0.40, 0.65], [0.52, 0.58],
    ];

    let animations = [];
    let elapsed = 0;
    let previousTime = performance.now();
    let sceneVisible = true;
    let resizeFrame = 0;
    let animationFrame = 0;
    let lastSize = { width: 0, height: 0 };

    const paint = (state) => {
      if (state === "answer") return { fill: palette.mustard, edge: palette.mustard };
      if (state === "gap") return { fill: palette.clear, edge: palette.field };
      if (state === "ink") return { fill: palette.ink, edge: palette.ink };
      return { fill: palette.weak, edge: palette.weak };
    };
    const offset = (milliseconds) => milliseconds / FLOW_CYCLE;
    const transform = (point, scale) => `translate3d(${point.x}px, ${point.y}px, 0) scale(${scale})`;
    const dimensions = () => {
      const bounds = scene.getBoundingClientRect();
      const width = Math.max(320, bounds.width);
      const height = Math.max(420, bounds.height);
      const mobile = width < 700;
      const unit = mobile
        ? Math.min(document.documentElement.clientWidth / 10.2, height / 9.5)
        : Math.min(width / 20, height / 9);
      const gap = unit * 0.15;
      return { width, height, unit, gap, step: unit + gap, mobile };
    };
    const sourcePoints = ({ width, height, unit, mobile }) => (mobile ? mobileLayout : desktopLayout)
      .map(([x, y]) => ({ x: x * width - unit / 2, y: y * height - unit / 2 }));
    const targetPoints = ({ width, height, unit, gap, step, mobile }) => {
      const points = [];
      const centreX = width * (mobile ? 0.5 : 0.74);
      const startY = height * (mobile ? 0.58 : 0.27);
      [1, 2, 4, 8].forEach((count, row) => {
        const rowWidth = count * unit + (count - 1) * gap;
        const startX = centreX - rowWidth / 2;
        for (let column = 0; column < count; column += 1) {
          points.push({ x: startX + column * step, y: startY + row * step });
        }
      });
      return points;
    };
    const arcPoint = (from, to, index, unit, reverse = false) => {
      const dx = to.x - from.x;
      const dy = to.y - from.y;
      const length = Math.hypot(dx, dy) || 1;
      const lane = Math.floor(index / 5);
      const direction = [1, -1, 1][lane] * (reverse ? -0.82 : 1);
      const amplitude = unit * (0.7 + (index % 5) * 0.17) * direction;
      return {
        x: (from.x + to.x) / 2 + (-dy / length) * amplitude,
        y: (from.y + to.y) / 2 + (dx / length) * amplitude,
      };
    };
    const animateUnit = (unitNode, from, to, sourceIndex, targetIndex, unitSize) => {
      const forwardDelay = (sourceIndex / (sourceCells.length - 1)) * FLOW_STAGGER;
      const reverseDelay = ((sourceCells.length - 1 - sourceIndex) / (sourceCells.length - 1)) * FLOW_STAGGER;
      const forwardStart = FLOW_HOLD + forwardDelay;
      const forwardMiddle = forwardStart + FLOW_TRAVEL * 0.47;
      const forwardEnd = forwardStart + FLOW_TRAVEL;
      const reverseStart = FLOW_HOLD + FLOW_MOVE + FLOW_HOLD + reverseDelay;
      const reverseMiddle = reverseStart + FLOW_TRAVEL * 0.53;
      const reverseEnd = reverseStart + FLOW_TRAVEL;
      const source = sourceCells[sourceIndex];
      const sourcePaint = paint(source.state);
      const targetPaint = paint(targetCells[targetIndex].state);
      const forwardArc = arcPoint(from, to, sourceIndex, unitSize);
      const reverseArc = arcPoint(from, to, sourceIndex, unitSize, true);

      const animation = unitNode.animate([
        { offset: 0, transform: transform(from, source.scale), opacity: source.opacity, backgroundColor: sourcePaint.fill, borderColor: sourcePaint.edge },
        { offset: offset(forwardStart), transform: transform(from, source.scale), opacity: source.opacity, backgroundColor: sourcePaint.fill, borderColor: sourcePaint.edge, easing: FLOW_EASE },
        { offset: offset(forwardMiddle), transform: transform(forwardArc, (source.scale + 1) / 2), opacity: Math.max(0.72, source.opacity), backgroundColor: sourcePaint.fill, borderColor: sourcePaint.edge, easing: FLOW_SETTLE },
        { offset: offset(forwardEnd), transform: transform(to, 1), opacity: 1, backgroundColor: targetPaint.fill, borderColor: targetPaint.edge },
        { offset: offset(reverseStart), transform: transform(to, 1), opacity: 1, backgroundColor: targetPaint.fill, borderColor: targetPaint.edge, easing: FLOW_EASE },
        { offset: offset(reverseMiddle), transform: transform(reverseArc, (source.scale + 1) / 2), opacity: Math.max(0.72, source.opacity), backgroundColor: targetPaint.fill, borderColor: targetPaint.edge, easing: FLOW_SETTLE },
        { offset: offset(reverseEnd), transform: transform(from, source.scale), opacity: source.opacity, backgroundColor: sourcePaint.fill, borderColor: sourcePaint.edge },
        { offset: 1, transform: transform(from, source.scale), opacity: source.opacity, backgroundColor: sourcePaint.fill, borderColor: sourcePaint.edge },
      ], { duration: FLOW_CYCLE, iterations: Infinity, fill: "both" });
      animation.pause();
      animation.currentTime = elapsed;
      return animation;
    };
    const build = () => {
      const size = dimensions();
      if (Math.abs(size.width - lastSize.width) < 1 && Math.abs(size.height - lastSize.height) < 1 && animations.length) return;
      lastSize = size;
      animations.forEach((animation) => animation.cancel());
      animations = [];
      layer.replaceChildren();
      const from = sourcePoints(size);
      const to = targetPoints(size);
      sourceCells.forEach((_, sourceIndex) => {
        const targetIndex = permutation[sourceIndex];
        const unitNode = document.createElement("span");
        unitNode.className = "hero__flow-unit";
        unitNode.style.setProperty("--flow-unit", `${size.unit}px`);
        layer.append(unitNode);
        animations.push(animateUnit(unitNode, from[sourceIndex], to[targetIndex], sourceIndex, targetIndex, size.unit));
      });
      scene.setAttribute("data-flow-ready", "");
    };
    const active = () => sceneVisible && !document.hidden;
    const frame = (time) => {
      if (active()) {
        elapsed = (elapsed + time - previousTime) % FLOW_CYCLE;
        animations.forEach((animation) => { animation.currentTime = elapsed; });
      }
      previousTime = time;
      animationFrame = requestAnimationFrame(frame);
    };
    const resetClock = () => { previousTime = performance.now(); };
    const visibilityObserver = "IntersectionObserver" in window
      ? new IntersectionObserver(([entry]) => {
          sceneVisible = entry.isIntersecting;
          resetClock();
        }, { threshold: 0.08 })
      : null;
    const resizeObserver = "ResizeObserver" in window
      ? new ResizeObserver(() => {
          cancelAnimationFrame(resizeFrame);
          resizeFrame = requestAnimationFrame(build);
        })
      : null;

    build();
    visibilityObserver?.observe(scene);
    resizeObserver?.observe(scene);
    document.addEventListener("visibilitychange", resetClock);
    animationFrame = requestAnimationFrame(frame);

    stopHeroFlow = () => {
      visibilityObserver?.disconnect();
      resizeObserver?.disconnect();
      cancelAnimationFrame(resizeFrame);
      cancelAnimationFrame(animationFrame);
      document.removeEventListener("visibilitychange", resetClock);
      animations.forEach((animation) => animation.cancel());
      layer.replaceChildren();
      scene.removeAttribute("data-flow-ready");
    };
  };

  const startShapeTransitions = () => {
    stopShapeTransitions();
    stopShapeTransitions = () => {};

    if (motionPreference.matches || !Element.prototype.animate) return;

    const scenes = [...document.querySelectorAll("[data-shape-transition]")];

    const centre = (rect) => ({
      x: rect.left + rect.width / 2,
      y: rect.top + rect.height / 2,
    });

    const travel = (fromRect, toRect, index) => {
      const from = centre(fromRect);
      const to = centre(toRect);
      const dx = to.x - from.x;
      const dy = to.y - from.y;
      const length = Math.hypot(dx, dy) || 1;
      const amplitude = Math.min(28, Math.max(9, length * 0.24)) * (index % 2 ? -1 : 1);
      const arcX = (-dy / length) * amplitude;
      const arcY = (dx / length) * amplitude;
      return {
        destination: `translate(${dx}px, ${dy}px) scale(0.78)`,
        forwardMiddle: `translate(${dx / 2 + arcX}px, ${dy / 2 + arcY}px) scale(0.9)`,
        reverseMiddle: `translate(${dx / 2 - arcX * 0.82}px, ${dy / 2 - arcY * 0.82}px) scale(0.9)`,
      };
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

        const sourceDestinations = sourceRects.map((_, index) => targetRects[(index * 3 + 1) % targetRects.length]);
        const targetOrigins = targetRects.map((_, index) => sourceRects[(index * 5 + 2) % sourceRects.length]);

        sourceUnits.forEach((unit, index) => {
          const path = travel(sourceRects[index], sourceDestinations[index], index);
          const forwardDelay = (index / Math.max(1, sourceUnits.length - 1)) * FLOW_STAGGER;
          const reverseDelay = ((sourceUnits.length - 1 - index) / Math.max(1, sourceUnits.length - 1)) * FLOW_STAGGER;
          const forwardStart = FLOW_HOLD + forwardDelay;
          const forwardMiddle = forwardStart + FLOW_TRAVEL * 0.47;
          const forwardEnd = forwardStart + FLOW_TRAVEL;
          const reverseStart = FLOW_HOLD + FLOW_MOVE + FLOW_HOLD + reverseDelay;
          const reverseMiddle = reverseStart + FLOW_TRAVEL * 0.53;
          const reverseEnd = reverseStart + FLOW_TRAVEL;
          controller.animations.push(unit.animate([
            { offset: 0, transform: "none", opacity: 1 },
            { offset: forwardStart / FLOW_CYCLE, transform: "none", opacity: 1, easing: FLOW_EASE },
            { offset: forwardMiddle / FLOW_CYCLE, transform: path.forwardMiddle, opacity: 0.88, easing: FLOW_SETTLE },
            { offset: forwardEnd / FLOW_CYCLE, transform: path.destination, opacity: 0 },
            { offset: reverseStart / FLOW_CYCLE, transform: path.destination, opacity: 0, easing: FLOW_EASE },
            { offset: reverseMiddle / FLOW_CYCLE, transform: path.reverseMiddle, opacity: 0.88, easing: FLOW_SETTLE },
            { offset: reverseEnd / FLOW_CYCLE, transform: "none", opacity: 1 },
            { offset: 1, transform: "none", opacity: 1 },
          ], { duration: FLOW_CYCLE, iterations: Infinity, fill: "both" }));
        });

        targetUnits.forEach((unit, index) => {
          const path = travel(targetRects[index], targetOrigins[index], index);
          const forwardDelay = (index / Math.max(1, targetUnits.length - 1)) * FLOW_STAGGER;
          const reverseDelay = ((targetUnits.length - 1 - index) / Math.max(1, targetUnits.length - 1)) * FLOW_STAGGER;
          const forwardStart = FLOW_HOLD + forwardDelay;
          const forwardMiddle = forwardStart + FLOW_TRAVEL * 0.47;
          const forwardEnd = forwardStart + FLOW_TRAVEL;
          const reverseStart = FLOW_HOLD + FLOW_MOVE + FLOW_HOLD + reverseDelay;
          const reverseMiddle = reverseStart + FLOW_TRAVEL * 0.53;
          const reverseEnd = reverseStart + FLOW_TRAVEL;
          controller.animations.push(unit.animate([
            { offset: 0, transform: path.destination, opacity: 0 },
            { offset: forwardStart / FLOW_CYCLE, transform: path.destination, opacity: 0, easing: FLOW_EASE },
            { offset: forwardMiddle / FLOW_CYCLE, transform: path.forwardMiddle, opacity: 0.72, easing: FLOW_SETTLE },
            { offset: forwardEnd / FLOW_CYCLE, transform: "none", opacity: 1 },
            { offset: reverseStart / FLOW_CYCLE, transform: "none", opacity: 1, easing: FLOW_EASE },
            { offset: reverseMiddle / FLOW_CYCLE, transform: path.reverseMiddle, opacity: 0.72, easing: FLOW_SETTLE },
            { offset: reverseEnd / FLOW_CYCLE, transform: path.destination, opacity: 0 },
            { offset: 1, transform: path.destination, opacity: 0 },
          ], { duration: FLOW_CYCLE, iterations: Infinity, fill: "both" }));
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

  const restartMotion = () => {
    startHeroFlow();
    startShapeTransitions();
  };
  restartMotion();
  motionPreference.addEventListener?.("change", restartMotion);

  // Two surfaces need the same control: the case tabs here and the measure
  // switch on the eval map. Both ship as real in-page links so that without
  // JavaScript every panel stays in the document; this only upgrades them.
  const bindTabs = ({ tabAttr, panelAttr, tablist, prefix }) => {
    const tabs = [...document.querySelectorAll(`[${tabAttr}]`)];
    const panels = [...document.querySelectorAll(`[${panelAttr}]`)];
    const key = tabAttr.replace("data-", "").replace(/-(\w)/g, (_, c) => c.toUpperCase());
    const panelKey = panelAttr.replace("data-", "").replace(/-(\w)/g, (_, c) => c.toUpperCase());

    if (!tabs.length || !panels.length) return;

    const select = (name) => {
      tabs.forEach((tab) => {
        const selected = tab.dataset[key] === name;
        tab.setAttribute("aria-selected", String(selected));
        tab.setAttribute("tabindex", selected ? "0" : "-1");
      });

      panels.forEach((panel) => {
        panel.hidden = panel.dataset[panelKey] !== name;
      });
    };

    // Roles first: aria-selected on an <a> only means anything once the
    // element is a tab.
    document.querySelector(tablist)?.setAttribute("role", "tablist");

    tabs.forEach((tab) => {
      tab.setAttribute("role", "tab");
      tab.setAttribute("aria-controls", `${prefix}${tab.dataset[key]}`);

      tab.addEventListener("click", (event) => {
        event.preventDefault();
        select(tab.dataset[key]);
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
        select(next.dataset[key]);
      });
    });

    panels.forEach((panel) => {
      panel.setAttribute("role", "tabpanel");
      panel.setAttribute("tabindex", "-1");
    });

    const requested = window.location.hash.replace(`#${prefix}`, "");
    const initial = tabs.some((tab) => tab.dataset[key] === requested)
      ? requested
      : tabs[0].dataset[key];
    select(initial);
  };

  bindTabs({
    tabAttr: "data-case-tab",
    panelAttr: "data-case-panel",
    tablist: "[data-tablist]",
    prefix: "case-",
  });

  bindTabs({
    tabAttr: "data-map-tab",
    panelAttr: "data-map-panel",
    tablist: "[data-map-tablist]",
    prefix: "map-",
  });

  // The pair page sets two outputs side by side. On a phone they would stack
  // into one long scroll, so there the two become tabs; wider, both stay open.
  // Without JavaScript the tabs are anchors and both outputs are in the page.
  const armTabs = [...document.querySelectorAll("[data-arm-tab]")];
  const armPanels = [...document.querySelectorAll("[data-arm-panel]")];
  if (armTabs.length && armPanels.length) {
    const narrow = window.matchMedia("(max-width: 899px)");
    let current = window.location.hash === "#arm-skill" ? "skill" : "control";
    const apply = () => {
      armPanels.forEach((panel) => {
        panel.hidden = narrow.matches && panel.dataset.armPanel !== current;
        panel.setAttribute("role", narrow.matches ? "tabpanel" : "article");
      });
      armTabs.forEach((tab) => {
        const selected = tab.dataset.armTab === current;
        tab.setAttribute("aria-selected", String(selected));
        tab.setAttribute("tabindex", selected ? "0" : "-1");
      });
    };
    document.querySelector("[data-arm-tablist]")?.setAttribute("role", "tablist");
    armTabs.forEach((tab) => {
      tab.setAttribute("role", "tab");
      tab.setAttribute("aria-controls", `arm-${tab.dataset.armTab}`);
      tab.addEventListener("click", (event) => {
        event.preventDefault();
        current = tab.dataset.armTab;
        apply();
      });
      tab.addEventListener("keydown", (event) => {
        if (!["ArrowRight", "ArrowLeft"].includes(event.key)) return;
        event.preventDefault();
        const next = armTabs[(armTabs.indexOf(tab) + 1) % armTabs.length];
        next.focus();
        current = next.dataset.armTab;
        apply();
      });
    });
    narrow.addEventListener("change", apply);
    apply();
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
