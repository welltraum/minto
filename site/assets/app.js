(() => {
  const root = document.documentElement;
  const isRussian = root.lang === "ru";
  const status = document.querySelector(".copy-status");
  let statusTimer;

  root.classList.add("js");

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
    button.addEventListener("click", async () => {
      const text = button.dataset.copy;

      try {
        await writeClipboard(text);
        announce(isRussian ? "Скопировано в буфер обмена." : "Copied to clipboard.");

        const label = button.querySelector(".copy-button span, .prompt-action");
        if (!label) return;

        const previous = label.textContent;
        label.textContent = isRussian ? "Готово" : "Copied";
        window.setTimeout(() => {
          label.textContent = previous;
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

  const transformation = document.querySelector("[data-transformation]");

  if (transformation) {
    const controls = [...transformation.querySelectorAll("[data-transform-control]")];
    const panels = [...transformation.querySelectorAll("[data-transform-panel]")];
    const transformationStatus = transformation.querySelector(".transform-status");

    const setTransformation = (view, shouldAnnounce = true) => {
      controls.forEach((control) => {
        control.setAttribute(
          "aria-pressed",
          String(control.dataset.transformControl === view),
        );
      });

      panels.forEach((panel) => {
        panel.hidden = panel.dataset.transformPanel !== view;
      });

      if (shouldAnnounce && transformationStatus) {
        transformationStatus.textContent =
          view === "after"
            ? isRussian
              ? "Показана версия после Minto."
              : "Showing the version with Minto."
            : isRussian
              ? "Показан исходный текст."
              : "Showing the original document.";
      }
    };

    controls.forEach((control) => {
      control.addEventListener("click", () => {
        setTransformation(control.dataset.transformControl);
      });
    });

    setTransformation("before", false);
  }

  const modeExplorer = document.querySelector("[data-mode-explorer]");

  if (modeExplorer) {
    const tabs = [...modeExplorer.querySelectorAll("[data-mode-tab]")];
    const panels = [...modeExplorer.querySelectorAll("[data-mode-panel]")];

    const setMode = (mode, focusPanel = false) => {
      tabs.forEach((tab) => {
        const selected = tab.dataset.modeTab === mode;
        tab.setAttribute("aria-selected", String(selected));
        tab.setAttribute("tabindex", selected ? "0" : "-1");
        tab.toggleAttribute("aria-current", selected);
      });

      panels.forEach((panel) => {
        const selected = panel.dataset.modePanel === mode;
        panel.hidden = !selected;
        panel.setAttribute("aria-hidden", String(!selected));
      });

      if (focusPanel) {
        const activePanel = panels.find((panel) => panel.dataset.modePanel === mode);
        activePanel?.focus({ preventScroll: true });
      }
    };

    tabs.forEach((tab) => {
      tab.setAttribute("role", "tab");
      tab.setAttribute("aria-controls", `mode-${tab.dataset.modeTab}`);

      tab.addEventListener("click", (event) => {
        event.preventDefault();
        setMode(tab.dataset.modeTab);
        history.replaceState(null, "", tab.hash);
      });

      tab.addEventListener("keydown", (event) => {
        if (!["ArrowDown", "ArrowUp", "ArrowRight", "ArrowLeft"].includes(event.key)) {
          return;
        }

        event.preventDefault();
        const direction = ["ArrowDown", "ArrowRight"].includes(event.key) ? 1 : -1;
        const currentIndex = tabs.indexOf(tab);
        const nextIndex = (currentIndex + direction + tabs.length) % tabs.length;
        const nextTab = tabs[nextIndex];
        nextTab.focus();
        setMode(nextTab.dataset.modeTab);
      });
    });

    modeExplorer.querySelector(".mode-tabs")?.setAttribute("role", "tablist");
    panels.forEach((panel) => {
      panel.setAttribute("role", "tabpanel");
    });

    const requestedMode = window.location.hash.replace("#mode-", "");
    const initialMode = tabs.some((tab) => tab.dataset.modeTab === requestedMode)
      ? requestedMode
      : "intent";
    setMode(initialMode);
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

  window.requestAnimationFrame(() => {
    document.body.classList.add("is-ready");
  });
})();
