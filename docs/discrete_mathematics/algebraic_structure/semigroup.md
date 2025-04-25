<!--
 * @Author: chinesehamburger 2576226012@qq.com
 * @Date: 2025-03-21 10:06:15
 * @LastEditors: iming 2576226012@qq.com
 * @LastEditTime: 2025-04-21 16:31:58
 * @FilePath: \CHMath-wiki\docs\discrete_mathematics\algebraic_structure\semigroup.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 半群和独异点


**半群定义**
- 封闭二元运算，满足结合律  
- 可以定义非零次幂运算  

**定理1** 幂运算的等式  
- $a^n a^m = a^{n+m}$  
- $(a^n)^m = a^{nm}$  

---

**独异点**  
- 任何半群都可以扩张为独异点（幺半群）  
- 在独异点中可以定义零次幂运算  

---

**子半群和子独异点**  
**子半群、子独异点 B 的判定:**  
非空子集 B，B 对于 V 中的运算（含0元运算）封闭，即  
$\forall a, b \in B, ab \in B$  

- 若干子半群的非空交集仍为子半群  
- 若干子独异点的交集仍为子独异点  

**重要的子半群**  
- **子集合 B 生成的子半群**：  
  $V = \langle S, * \rangle$, $B \subseteq S$，包含 B 的最小的半群  
  $B' = \bigcap \{ A \mid A \text{ 是 } S \text{ 的子半群，} B \subseteq A \}$  
  $B' = \bigcup_{n \in \mathbb{Z}^+} B^n$, 其中  
  $B^n = \{ b_1 b_2 \cdots b_n \mid b_i \in B, i = 1, 2, \ldots, n \}$  

---

**半群、独异点的直积**  
- 半群的直积仍是半群  
- 独异点的直积仍是独异点  

---

**半群、独异点的商代数**  
- 半群 $\langle A, \circ \rangle$ 的商半群：$\langle A/R, \bar{\circ} \rangle$  
- 独异点 $\langle A, \circ, e \rangle$ 的商独异点：$\langle A/R, \bar{\circ}, [e] \rangle$  

---

**半群、独异点的同态和同构**  
- 半群同态：$f(xy) = f(x)f(y)$  
- 独异点同态：$f(xy) = f(x)f(y)$，且 $f(e) = e'$  

**定理3**  
设 $V = \langle S, * \rangle$ 为半群，则 $V' = \langle S^S, \circ \rangle$（$\circ$ 为合成运算）也是半群，且存在 $V$ 到 $V'$ 的同态。  

---

**独异点的表示定理**  
**定理4**  
设 $V = \langle S, *, e \rangle$ 为独异点，则存在 $T \subseteq S^S$，使得 $\langle S, *, e \rangle$ 同构于 $\langle T, \circ, I_S \rangle$。  
- 这个同态一定是单射，因此可以建立同构。  
- 同态映射 $\varphi: S \to S^S$ 定义为：  
  $\varphi(a) = f_a$，其中 $f_a(x) = a * x$  
- 性质：  
  $\varphi(a * b) = \varphi(a) \circ \varphi(b)$，且 $\varphi(e) = f_e = I_S$  