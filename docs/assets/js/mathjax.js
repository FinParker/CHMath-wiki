// MathJax 3 配置
// 说明: pymdownx.arithmatex (generic 模式) 已把 $...$ / $$...$$ 转换为 \(...\) / \[...\],
// 因此 MathJax 只处理被标记为 arithmatex 的 HTML 类。
window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
};
