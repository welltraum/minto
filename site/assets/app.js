(() => {
  const root = document.documentElement;
  const isRussian = root.lang === "ru";
  const status = document.querySelector(".copy-status");
  let statusTimer;

  // Paired with `.js [hidden] { display: none !important }`: without JS no
  // panel is ever hidden, so all five cases render as one long page.
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
