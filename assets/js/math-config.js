/*
 * @Author: chinesehamburger 2576226012@qq.com
 * @Date: 2025-03-21 10:43:02
 * @LastEditors: chinesehamburger 2576226012@qq.com
 * @LastEditTime: 2025-03-21 10:44:19
 * @FilePath: \CHMath-wiki\docs\_static\js\math-csr.js
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
MathJax = {
	chtml: {
		matchFontHeight: true
	}
};

// 当文档加载完成后，自动调用 MathJax.typesetPromise()，确保页面中的数学公式被正确渲染
document$.subscribe(function () {
	MathJax.typesetPromise();
});
