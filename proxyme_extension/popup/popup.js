// document.getElementById("toggle").addEventListener("change", (e) => {
//     const mode = e.target.checked ? "ProxyMe" : "RealMe";
//     chrome.storage.local.set({ mode });
// });
document.addEventListener("DOMContentLoaded", () => {
  const toggle = document.getElementById("toggle");
  const status = document.getElementById("status");

  chrome.storage.local.get("mode", (data) => {
    const mode = data.mode || "RealMe";
    toggle.checked = mode === "ProxyMe";
    status.textContent = `Current Mode: ${mode}`;
  });

  toggle.addEventListener("change", () => {
    const mode = toggle.checked ? "ProxyMe" : "RealMe";
    chrome.storage.local.set({ mode });
    status.textContent = `Current Mode: ${mode}`;
  });
});
