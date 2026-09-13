document$.subscribe(() => {
  const isDark = document.body.getAttribute("data-md-color-scheme") === "slate";
  const themeVariables = isDark
    ? {
        background: "#3f3f3f",
        primaryColor: "#2b2b2b",
        primaryTextColor: "#dcdccc",
        primaryBorderColor: "#5f5f5f",
        secondaryColor: "#4f4f4f",
        tertiaryColor: "#3f3f3f",
        lineColor: "#709080",
        textColor: "#dcdccc",
        mainBkg: "#2b2b2b",
        nodeBorder: "#8cd0d3",
        clusterBkg: "#4f4f4f",
        clusterBorder: "#709080",
        titleColor: "#f0dfaf",
        edgeLabelBackground: "#3f3f3f",
        errorBkgColor: "#cc9393",
        errorTextColor: "#2b2b2b",
        fontFamily: "Gothic A1, sans-serif",
      }
    : {
        background: "#f3f0df",
        primaryColor: "#e6e3d1",
        primaryTextColor: "#3f3f3f",
        primaryBorderColor: "#709080",
        secondaryColor: "#dedbc9",
        tertiaryColor: "#f3f0df",
        lineColor: "#5f7f5f",
        textColor: "#3f3f3f",
        mainBkg: "#e6e3d1",
        nodeBorder: "#3f7f7f",
        clusterBkg: "#dedbc9",
        clusterBorder: "#709080",
        titleColor: "#8f5f2f",
        edgeLabelBackground: "#f3f0df",
        errorBkgColor: "#cc9393",
        errorTextColor: "#3f3f3f",
        fontFamily: "Gothic A1, sans-serif",
      };

  mermaid.initialize({
    startOnLoad: false,
    theme: "base",
    themeVariables,
    securityLevel: "strict",
  });
  mermaid.run({ querySelector: ".mermaid" });
});
