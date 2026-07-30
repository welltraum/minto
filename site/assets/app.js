(() => {
  const status = document.querySelector(".copy-status");
  const isRussian = document.documentElement.lang === "ru";
  let statusTimer;

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
        announce(isRussian ? "Не удалось скопировать. Выделите команду вручную." : "Could not copy. Select the command manually.");
      }
    });
  });
})();
