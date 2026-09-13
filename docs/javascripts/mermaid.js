document$.subscribe(() => {
  const isDark = document.body.getAttribute("data-md-color-scheme") === "slate";

  mermaid.initialize({
    startOnLoad: false,
    theme: isDark ? "dark" : "default",
    securityLevel: "strict",
  });
  mermaid.run({ querySelector: ".mermaid" });
});
