# 群

## 群的理解

- 同态核 $ker \phi$ 是特殊的正规子群
- 群G可以对正规子群做商群
- 若中心达到整个群, 则整个群为Abel群

## 定理汇总

**定理 17.1** 设 $\langle G, \circ\rangle$ 是具有一个可结合二元运算的代数系统，若存在 $e\in G$，使得 $\forall a\in G$，有 $a\circ e=a$，且 $\forall a\in G$，存在 $a_0\in G$ 满足 $a\circ a_0=e$，则 $G$ 是一个群。

**定理 17.2** $G$ 为群，$\forall a,b\in G$ 有  
(1) $(a^{-1})^{-1}=a$;  
(2) $(ab)^{-1}=b^{-1}a^{-1}$;  
(3) $a^n a^m = a^{n+m}, m,n\in \mathbb{Z}$;  
(4) $(a^n)^m = a^{mn}, m,n\in \mathbb{Z}$;  
(5) 若 $G$ 为 Abel 群，$(ab)^n = a^n b^n, n\in \mathbb{Z}$.

**定理 17.3** $G$ 为群，$\forall a,b\in G$，方程 $ax=b$ 和 $ya=b$ 在 $G$ 中有解且有惟一解.

**定理 17.4** 设 $G$ 是具有一个可结合的二元运算的代数系统，如果 $\forall a,b\in G$ 方程 $ax=b$ 和 $ya=b$ 在 $G$ 中有解，则 $G$ 是群.

**定理 17.5** 群中运算满足消去律.

**定理 17.6** 设 $G$ 是具有一个二元运算的不含零元的有限代数系统，且该运算适合结合律和消去律，则 $G$ 是一个群.

**定理 17.7** 设 $G=\{a_1,a_2,\ldots,a_n\}$ 为群，则 $G$ 的运算表的每行每列都是 $G$ 中元素的一个置换.

**定理 17.8** $G$ 是群，$a\in G$ 且 $|a|=r$，则  
(1) $a^k=e$ 当且仅当 $r\mid k$，$k\in \mathbb{Z}$；  
(2) $|a|=|a^{-1}|$；  
(3) 若 $|G|=n$ 则 $r\leq n$.

**定理 17.9** (子群判定定理一) $G$ 是群，$H$ 是 $G$ 的非空子集，则 $H$ 是 $G$ 的子群当且仅当  
(1) $\forall a,b\in H$ 有 $ab\in H$，  
(2) $\forall a\in H$ 有 $a^{-1}\in H$.

**定理 17.10** (子群判定定理二) $G$ 是群，$H$ 是 $G$ 的非空子集，则 $H$ 是 $G$ 的子群当且仅当 $\forall a,b\in H$ 有 $ab^{-1}\in H$.

**定理 17.11** (子群判定定理三) $G$ 是群，$H$ 是 $G$ 的有穷非空子集，则 $H$ 是 $G$ 的子群当且仅当 $\forall a,b\in H$ 有 $ab\in H$.

**定理 17.12** $G=\langle a\rangle$ 是循环群.  
(1) 若 $G$ 是无限阶循环群，则 $G$ 的生成元是 $a$ 和 $a^{-1}$.  
(2) 若 $G$ 是 $n$ 阶循环群，则 $G$ 有 $\phi(n)$ 个生成元. 当 $n=1$ 时，$G=\langle e\rangle$ 的生成元是 $e$，当 $n>1$ 时，对每一个不于等于 $n$ 的正整数 $r$，$a^r$ 是 $G$ 的生成元当且仅当 $(n,r)=1$.

**定理 17.13** $G=\langle a\rangle$ 是循环群，那么  
(1) $G$ 的子群也是循环群；  
(2) 若 $G$ 是无限阶的，则 $G$ 的子群除 $\{e\}$ 以外仍是无限阶的；  
(3) 若 $G$ 是 $n$ 阶的，则 $G$ 的子群的阶是 $n$ 的因子，对于 $n$ 的每个正因子 $d$，在 $G$ 中有且仅有一个 $d$ 阶子群, 即 $\langle a^{\frac{n}{d}} \rangle$是这个d阶子群

**定理 17.14** 设 $E(A)$ 是 $A$ 上的全体一一变换构成的集合，则 $E(A)$ 关于变换的乘法构成一个群.

**定理 17.15** 设 $\sigma,\tau\in S_n$，若 $\sigma$ 与 $\tau$ 是不相交的，则 $\sigma\tau=\tau\sigma$.

**定理 17.16** 任何 $n$ 元置换都可以表成不相交的轮换之积，并且表法是惟一的.

**定理 17.17** 设 $\sigma=(i_1i_2\cdots i_k)$ 是 $A=\{1,2,\ldots,n\}$ 上的 $k$ 阶轮换，$k>1$，则 $\sigma=(i_1i_k)(i_1i_{k-1})\cdots(i_1i_2)$.

**定理 17.18** $\sigma\in S_n$ 且 $\sigma(j)=i_j$，$j=1,2,\ldots,n$，则在 $\sigma$ 的对换表示中对换个数的奇偶性与排列 $\pi=i_1i_2\cdots i_n$ 中的逆序数的奇偶性一致.

**定理 17.19** $G$ 是 $n$ 元置换群.  
(1) $\sigma\in G$，$\sigma=(i_1i_2\cdots i_k)$，则 $|\sigma|=k$.  
(2) $\tau\in G$，$\tau=\tau_1\tau_2\cdots\tau_l$ 是不相交轮换的分解式，若 $\tau_i$ 是 $k_i$ 阶轮换，$i=1,2,\ldots,l$，则 $\tau$ 的阶是 $k_1,k_2,\ldots,k_l$ 的最小公倍数，即 $|\tau|=[k_1,k_2,\ldots,k_l]$.

**定理 17.20** 设 $G$ 是群，$H$ 是 $G$ 的子群，则  
(1) $He=H$;  
(2) $\forall a\in G$, $a\in Ha$.

**定理 17.21** 设 $G$ 是群，$H$ 是 $G$ 的子群，则 $\forall a\in G$, $Ha\approx H$.

**定理 17.22** $G$ 是群，$H$ 是 $G$ 的子群，$\forall a,b\in G$ 有 $a\in Hb \Leftrightarrow Ha=Hb \Leftrightarrow ab^{-1}\in H$.

**定理 17.23** $G$ 是群，$H$ 是 $G$ 的子群，在 $G$ 上定义二元关系 $R$，$\forall a,b\in G$ 有 $aRb \Leftrightarrow ab^{-1}\in H$, 则 $R$ 为 $G$ 上的等价关系，则 $[a]_R=Ha$.

**定理 17.24** $G$ 是群，$H$ 是 $G$ 的子群，则 $\forall a,b\in G$, $Ha\cap Hb=\emptyset$ 或 $Ha=Hb$，且 $\bigcup_{a\in G} Ha=G$.

**定理 17.25** 设 $G$ 是群，$H$ 是 $G$ 的子群，则  
(1) $eH=H$；  
(2) $\forall a\in G$, $a\in aH$；  
(3) $\forall a\in G$, $aH\approx H$；  
(4) $\forall a,b\in G$, $a\in bH \Leftrightarrow aH=bH \Leftrightarrow a^{-1}b\in H$；  
(5) 在 $G$ 上定义二元关系 $R$，$\forall a,b\in G$，$aRb \Leftrightarrow a^{-1}b\in H$，则 $R$ 为 $G$ 上的等价关系，且 $[a]_R=aH$；  
(6) $\forall a,b\in G$, $aH\cap bH=\emptyset$ 或 $aH=bH$，且 $\bigcup_{a\in G} aH=G$.

**定理 17.26** (Lagrange 定理) 设 $G$ 是有限群，$H$ 是 $G$ 的子群，则 $|G|=[G:H]|H|$.

**推论 1** $G$ 是 $n$ 阶群，则 $G$ 中每个元素的阶是 $n$ 的因子，且 $\forall a\in G$ 有 $a^n=e$.

**推论 2** 阶为素数的群是循环群.

**定理 17.27** 群 $G$ 上的共轭关系是 $G$ 上的等价关系.

**定理 17.28** $G$ 是群，$C$ 是 $G$ 的中心，则 $\forall a\in G$ 有 $a\in C \Leftrightarrow \bar{a}=\{a\}$.

**定理 17.29** $G$ 是群，则 $\forall a\in G$，$N(a)$ 是 $G$ 的子群.

**定理 17.30** $G$ 是有限群，则 $\forall a\in G$ 有 $|\bar{a}|=[G:N(a)]$.

**定理 17.31** (群的分类方程) $G$ 是有限群，$C$ 是 $G$ 的中心. 设 $G$ 中至少含有两个元素的共轭类有 $k$ 个，且 $a_1,a_2,\ldots,a_k$ 分别为这 $k$ 个共轭类的代表元素，则  
$$
|G|=|C|+[G:N(a_1)]+[G:N(a_2)]+\cdots+[G:N(a_k)].
$$

**定理 17.32** $N$ 是群 $G$ 的子群，则下列条件互相等价.  
(1) $N\triangleleft G$；  
(2) $\forall g\in G$ 有 $gNg^{-1}=N$；  
(3) $\forall g\in G$，$\forall n\in N$ 有 $gng^{-1}\in N$.

**定理 17.33** 设 $\phi$ 是群 $G_1$ 到 $G_2$ 的同态，则 $\phi$ 为单同态当且仅当 $\ker\phi=\{e_1\}$.

**定理 17.34** $G_1=\langle a\rangle$ 是循环群，$\phi$ 是 $G_1$ 到 $G_2$ 的满同态，则 $G_2$ 也是循环群.

**定理 17.35** 设 $\phi$ 是群 $G_1$ 到 $G_2$ 的同态.  
(1) 若 $H$ 是 $G_1$ 的子群，则 $\phi(H)$ 是 $G_2$ 的子群.  
(2) 若 $H$ 是 $G_1$ 的正规子群，且 $\phi$ 是满同态，则 $\phi(H)$ 是 $G_2$ 的正规子群.

**定理 17.36** 设 $\phi$ 是群 $G_1$ 到 $G_2$ 的同态，则  
(1) $\ker\phi$ 是 $G_1$ 的正规子群；  
(2) $\forall a,b\in G_1$, $\phi(a)=\phi(b) \Leftrightarrow a\ker\phi=b\ker\phi$.

**定理 17.37** (群同态基本定理) 设 $G$ 是群，$H$ 是 $G$ 的正规子群，则 $G$ 的商群 $G/H$ 是 $G$ 的同态像. 若 $G'$ 是 $G$ 的同态像，$G\stackrel{\phi}{\sim} G'$，则 $G/\ker\phi\cong G'$.

**群的同构定理**

**定理 17.38** $G$ 是群，则 $\mathrm{End}(G)$ 关于映射的合成运算构成一个独异点，$\mathrm{Aut}(G)$ 关于映身的合成运算构成一个群.

**定理 17.39** $G$ 是群，则 $\mathrm{Inn}(G)\triangleleft \mathrm{Aut}(G)$.

**定理 17.40** 设 $G$ 是群，$K$ 和 $L$ 是 $G$ 的子群，则 $G=K\times L$ 当且仅当下面的条件成立：  
(1) $K\triangleleft G, L\triangleleft G$;  
(2) $K\cap L=\{e\}$;  
(3) $G=KL$.

**定理 17.41** 设 $G$ 是群，$G_1,G_2,\ldots,G_n$ 是 $G$ 的子群，则 $G=G_1\times G_2\times\cdots\times G_n$ 当且仅当以下条件成立：  
(1) $G_i\triangleleft G, i=1,2,\ldots,n$；  
(2) $G_i\cap G_1G_2\cdots G_{i-1}G_{i+1}\cdots G_n=\{e\}, i=1,2,\ldots,n$；  
(3) $G=G_1G_2\cdots G_n$.

**定理 17.42** 用 $r$-电路计算一个 $m$ 元函数至少需要 $d\log_r me$ 个时间单位.

**定理 17.43** 设 $\langle Z_n,\otimes\rangle$ 是群，若存在 $a\in Z_n$，$a\neq 0$，且 $a$ 属于 $Z_n$ 的每一个非平凡的子群，则对于任意的模 $n$ 加法器 $T$，总存在着某个输入，使得 $T$ 至少依赖于输入的 $2d\log_2 ne$ 位.

**推论 1** 若 $Z_n$ 中含有一个无所不在的元素，则用 $r$-电路计算 $Z_n$ 中的加法至少需要 $d\log_r (2 d\log_2 ne)e$ 个时间单位.

**推论 2** 若 $Z_n$ 中不存在无所不在的元素，$H$ 是 $Z_n$ 的子群，$H$ 中存在一个无所不在的元素，则用 $r$-电路计算 $Z_n$ 中的加法至少需要 $d\log_r (2 d\log_2|H|e)e$ 个时间单位.

**定理 17.44**  
(1) $n=p^i$，$p$ 为素数，$i$ 为正整数，则用 $r$-电路计算 $Z_n$ 中的加法至少需要 $d\log_r (2 d\log_2 ne)e$ 个时间单位.  
(2) $n=p_1^{i_1}p_2^{i_2}\cdots p_k^{i_k}$，是 $n$ 的素因子分解式，则用 $r$-电路计算 $Z_n$ 中的加法至少需要 $d\log_r (2 d\log_2 t(n)e)e$ 个时间单位，其中 $t(n)=\max\{p_1^{i_1},p_2^{i_2},\ldots,p_k^{i_k}\}$.

## 子群

$H \leq G$

定义(性质)

(1) $\forall a_1, a_2, \cdots a_n \in H, a_1 a_2 \cdots a_n \in H$ (封闭性)

(2) H中元素满足结合律

(3) $e \in H$ (存在单位元)

(4) $\forall a \in H, a^{-1} \in H$ (存在逆元)

**判定**:

**定理 17.9** (子群判定定理一) $G$ 是群，$H$ 是 $G$ 的非空子集，则 $H$ 是 $G$ 的子群当且仅当  
(1) $\forall a,b\in H$ 有 $ab\in H$，  
(2) $\forall a\in H$ 有 $a^{-1}\in H$.

**定理 17.10** (子群判定定理二) $G$ 是群，$H$ 是 $G$ 的非空子集，则 $H$ 是 $G$ 的子群当且仅当 $\forall a,b\in H$ 有 $ab^{-1}\in H$.

**定理 17.11** (子群判定定理三) $G$ 是群，$H$ 是 $G$ 的有穷非空子集，则 $H$ 是 $G$ 的子群当且仅当 $\forall a,b\in H$ 有 $ab\in H$.

**性质**:

(1) 子群的交仍是子群, 即$G为群, H \leq G, K \leq G, 则H \cap K \leq G$
提示: 根据子群定义证明

(2) $H \cup K \leq G \leftrightarrow H \subseteq K \ or \ K \subseteq H$

H1, H2为r, s 阶子群，(r, s)=1, 则 H1∩H2={e}

### 生成子群

**$\langle a \rangle$定义**:

G为群,$a \in G$,
$\langle a \rangle = \{ a^k, k \in \mathbb{Z} \}$,
则$\langle a \rangle \leq G, 且 |\langle a \rangle | = |a|$

若G中存在n阶元a, 则G中存在n阶子群$\langle a \rangle$

**$\langle B \rangle$定义*

G为群,B是G的非空子集,令$$S = \{H|H \leq G 且 B\subseteq H\}$$,

则S非空,设$K = \cap S$, 则K为B的生成的子群, 记为$K=\langle B \rangle$

(1)$\langle B \rangle \leq G$, $\langle B \rangle \subseteq G$

(2)$\langle B \rangle = \{ {a_1}^{e_1} {a_2}^{e_2} \cdots {a_n}^{e_n} | n \in \mathbb{Z^+} 且 a_i \in B, e_i = \pm 1 \}$

### 共轭子群

G是群, $H \leq G$, 令$$xHx^{-1} = \{xhx^{-1} | h \in H\}$$,
则$xHx^{-1}$是G的子群, 称为H的共轭子群

可以在H和$xHx^{-1}$之间建立双射, 有$xHx^{-1} \approx H$

### 正规子群(不变子群) normal subgroup

**正规子群定义**:

左右陪集相等的子群是正规子群, 记作$N \unlhd G$
即对于$H\leq G, \forall a \in G, aH = Ha$

**子群的判定定理** $N$ 是群 $G$ 的子群，则下列条件互相等价.  
(1) $N \unlhd G$；  
(2) $\forall g\in G$ 有 $gNg^{-1}=N$；  
(3) $\forall g\in G$，$\forall n\in N$ 有 $gng^{-1}\in N$.

例:

群G的两个平凡子群G和$\{e\}$是G的正规子群

Abel群的所有子群H都是正规子群($aH = Ha$)

$H \leq G, |H| = n$ 若H是唯一的n阶子群, 则 $H \unlhd G$
证明:

## 循环群

**循环群定义**:

对于群 $G$, 如果 $\exists a \in G, s.t. G = {a^k|k \in G}$, 则 $G$ 为循环群, $G=\langle a \rangle$, $a$ 为生成元

**性质**:

(1) 若 $|a|$ 存在,则 $\langle a \rangle = \{ e, a, a^2 \cdots a^{n-1}\}$为n阶循环群,
即$| \langle a \rangle | = |a|$

(2) 若 $|a|$ 不存在,则 $\langle a \rangle = \{ e, a, a^{-1}, a^2, a^{-2}, \cdots \}$为无限阶循环群

(3) 循环群一定是Abel群, Abel群的中心就是其本身

**循环群的生成元**:

$G=\langle a\rangle$ 是循环群.  

(1) 若 $G$ 是无限阶循环群，则 $G$ 的生成元只有 $a$ 和 $a^{-1}$.

(2) 若 $G$ 是 $n$ 阶循环群，则 $G$ 有 $\phi(n)$ 个生成元. 当 $n=1$ 时，$G=\langle e\rangle$ 的生成元是 $e$，当 $n>1$ 时，对每一个不于等于 $n$ 的正整数 $r$，$a^r$ 是 $G$ 的生成元当且仅当 $(n,r)=1$.

**循环群的子群**:

$G=\langle a\rangle$ 是循环群，那么

(1) $G$ 的子群也是循环群；  

(2) 若 $G$ 是无限阶的，则 $G$ 的子群除 $\{e\}$ 以外仍是无限阶的；  

(3) 若 $G$ 是 $n$ 阶的，则 $G$ 的子群的阶是 $n$ 的因子，对于 $n$ 的每个正因子 $d$，在 $G$ 中有且仅有一个 $d$ 阶子群, 即 $\langle a^{\frac{n}{d}} \rangle$是这个d阶子群

## 变换群与置换群

## 轮换

下面 $xxx$ 和 $yyy$ 不交:
$(a \ xxx)(a \ yyy) = (a \ yyy \ xxx)$
$(a \ xxx \ yyy) = (a \ yyy)(a \ xxx)$

例:

$(i_1 \ i_2 \cdots i_k) = (i_1 \ i_k)(i_1 \ i_2 \cdots i_{k-1}) = \cdots = (i_1 \ i_k) (i_1 \ i_{k-1}) \cdots (i_1 i_2)$

即: 任意轮换可以表示为对换之积,但是表示不唯一

## 群的等价类划分(分类)

### 群的陪集分解 => Lagrange 定理

**定理 17.20** 设 $G$ 是群，$H$ 是 $G$ 的子群，则  
(1) $He=H$;  
(2) $\forall a\in G$, $a\in Ha$.

**定理 17.21** 设 $G$ 是群，$H$ 是 $G$ 的子群，则 $\forall a\in G$, $Ha\approx H$.

**定理 17.22** $G$ 是群，$H$ 是 $G$ 的子群，$\forall a,b\in G$ 有 $a\in Hb \Leftrightarrow Ha=Hb \Leftrightarrow ab^{-1}\in H$.

**定理 17.23** $G$ 是群，$H$ 是 $G$ 的子群，在 $G$ 上定义二元关系 $R$，$\forall a,b\in G$ 有 $aRb \Leftrightarrow ab^{-1}\in H$, 则 $R$ 为 $G$ 上的等价关系，则 $[a]_R=Ha$.

**定理 17.24** $G$ 是群，$H$ 是 $G$ 的子群，则 $\forall a,b\in G$, $Ha\cap Hb=\emptyset$ 或 $Ha=Hb$，且 $\bigcup_{a\in G} Ha=G$.

**定理 17.25** 设 $G$ 是群，$H$ 是 $G$ 的子群，则  
(1) $eH=H$；  
(2) $\forall a\in G$, $a\in aH$；  
(3) $\forall a\in G$, $aH\approx H$；  
(4) $\forall a,b\in G$, $a\in bH \Leftrightarrow aH=bH \Leftrightarrow a^{-1}b\in H$；  
(5) 在 $G$ 上定义二元关系 $R$，$\forall a,b\in G$，$aRb \Leftrightarrow a^{-1}b\in H$，则 $R$ 为 $G$ 上的等价关系，且 $[a]_R=aH$；  
(6) $\forall a,b\in G$, $aH\cap bH=\emptyset$ 或 $aH=bH$，且 $\bigcup_{a\in G} aH=G$.

**定理 17.26** (Lagrange 定理) 设 $G$ 是有限群，$H$ 是 $G$ 的子群，则 $|G|=[G:H]|H|$.

**推论 1** $G$ 是 $n$ 阶群，则 $G$ 中每个元素的阶是 $n$ 的因子，且 $\forall a\in G$ 有 $a^n=e$.

**推论 2** 阶为素数的群是循环群.

### 群的共轭类分解 => 群的分类方程

**共轭关系定义**:

$a\in G, b\in G$,
$$def \ R: aRb \leftrightarrow \exists x \in G, s.t. \ b = x^{-1}ax$$

易证, 共轭关系是G上等价关系, 等价类为 $\bar{a} = [a]_R$

**定理 17.28** $G$ 是群，$C$ 是 $G$ 的中心，则 $\forall a\in G$ 有 $a\in C \Leftrightarrow \bar{a}=\{a\}$.

**定理 17.29** $G$ 是群，则 $\forall a\in G$，$N(a)$ 是 $G$ 的子群.

**定理 17.30** $G$ 是有限群，则 $\forall a\in G$ 有 $|\bar{a}|=[G:N(a)]$.

**定理 17.31** (群的分类方程) $G$ 是有限群，$C$ 是 $G$ 的中心. 设 $G$ 中至少含有两个元素的共轭类有 $k$ 个，且 $a_1,a_2,\ldots,a_k$ 分别为这 $k$ 个共轭类的代表元素，则  
$$
|G|=|C|+[G:N(a_1)]+[G:N(a_2)]+\cdots+[G:N(a_k)].
$$

## 商群

## 自同态与自同构

$End \ G$: G上的所有映射中自同态映射的集合
$Aut \ G$: G上的所有映射中自同构映射的集合
$Inn \ G$: G上的所有映射中内自同构映射的集合
内自同构映射: $f_a: \ G \rightarrow G, f_a(x)=axa^{-1}$

### 例子

$G = \langle Z_6, \oplus \rangle$, G上的所有映射:
$f_p(x)=px(mod \ 6), p = 0,1,2,3,4,5$
这里G是交换群,
$End \ G = {f_0, f_1, \cdots , f_5}$
$Aut \ G = {f_1, f_5}$
$Inn \ G = {f_1}$

## 常见群

4阶群G在同构意义下只有2个:
(1) $\mathbb{Z_4}$ 加法循环群
(2) Klein四元群

根据拉格朗日定理，四阶群中元素的阶只能是1、2或4。通过以下分析可以排除其他可能性：

存在四阶元的情况：

若群 G 中存在一个四阶元 a，则 $G=⟨a⟩={e,a,a2,a3}$，因此 G 是循环群，同构于 $\mathbb{Z_4}$​

所有非单位元的阶均为2的情况：

若群 G 中没有四阶元，则所有非单位元的阶均为2。假设 $G=\{e,a,b,c\}$，其中 $a^2 = b^2 = c^2 = e$。
闭合性要求 $ab$ 必须是 G 中的元素。由于 $a \neq b$ 且 $a^2=e$，所以 ab 只能是 c（否则会导致矛盾，如 $ab=a \rightarrow b=e$，与 b 是非单位元矛盾）。
进一步验证运算表，发现 $K_4$​ 的结构唯一，且满足交换律，因此 G 同构于 $K_4$

$K_4$(Klein四元群)是Abel群

### Klein 四元群

克莱因四元群（Klein四元群，记为 \( V_4 \) 或 \( K_4 \)）是群论中一个重要的基本群，以下是其核心性质的详细总结：

**1. 基本性质**:

- **阶**：群的阶为4，包含4个元素：一个单位元 \( e \) 和三个阶为2的元素（例如 \( a, b, c \)）。
  \[
  K_4 = \{ e, a, b, c \}, \quad \text{其中} \ a^2 = b^2 = c^2 = e.
  \]
- **交换性**：克莱因四元群是阿贝尔群（交换群），即任意两个元素的乘积满足 \( ab = ba \)。
- **非循环性**：它不是循环群，因为没有任何单个元素能生成整个群。例如，若 \( a \) 是生成元，则 \( \langle a \rangle = \{ e, a \} \)，无法生成所有元素。

**2. 结构与表示**:

- **直积结构**：  
  克莱因四元群同构于两个循环群 \( \mathbb{Z}_2 \times \mathbb{Z}_2 \)，其元素可表示为：
  \[
  K_4 \cong \mathbb{Z}_2 \times \mathbb{Z}_2 = \{ (0,0), (1,0), (0,1), (1,1) \},
  \]
  其中运算为坐标分量的模2加法。
- **数值结构**：  
  例如，集合 \( \{1, 3, 5, 7\} \) 在模8乘法下构成克莱因四元群：
  \[
  3 \times 5 = 15 \equiv 7 \pmod{8}, \quad 3^2 = 9 \equiv 1 \pmod{8}.
  \]
- **置换表示**：  
  在四元素的置换群 \( S_4 \) 中，克莱因四元群可表示为：
  \[
  K_4 = \{ \text{恒等置换}, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3) \},
  \]
  这是 \( S_4 \) 的一个正规子群。

**3. 几何实现**:

- **二维对称群**：  
  - **菱形的对称群**：菱形的对称操作包括恒等、水平翻转、垂直翻转和对角线翻转，这些操作构成克莱因四元群。
  - **矩形（非正方形）的对称群**：矩形的对称操作包括恒等、水平翻转、垂直翻转和中心对称，但注意正方形的对称群是更大的二面体群 \( D_4 \)。
  - **十字架的对称群**：如知识库中提到的十字架，可通过水平或垂直翻转保持不变，其对称群为 \( K_4 \)。

- **三维对称群**：  
  在三维空间中，克莱因四元群可表示为以下对称群：
  1. **\( D_2 \)**：具有三个垂直的2倍旋转轴。
  2. **\( C_{2h} \)**：包含一个2倍旋转轴和一个垂直的反射平面。
  3. **\( C_{2v} \)**：在反射平面上具有2倍旋转轴。

**4. 自同构群**:

- **自同构群的结构**：  
  克莱因四元群的自同构群（保持群结构的同构映射）是置换群 \( S_3 \)，其阶为6。这是因为三个非单位元 \( a, b, c \) 可以任意排列，而单位元 \( e \) 固定不变。
  - 例如，自同构可以将 \( a \leftrightarrow b \)，\( a \leftrightarrow c \) 或 \( b \leftrightarrow c \)，共 \( 3! = 6 \) 种可能。

**5. 子群与正规性**:

- **所有子群均为正规**：  
  由于克莱因四元群是阿贝尔群，所有子群都是正规子群。
- **子群结构**：  
  其子群包括：
  - 三个阶为2的子群：\( \{e, a\} \)、\( \{e, b\} \)、\( \{e, c\} \)；
  - 整个群 \( K_4 \) 本身；
  - 以及平凡子群 \( \{e\} \)。

**6. 代数与应用**:

- **伽罗瓦理论**：  
  在四次方程的求解中，克莱因四元群的置换表示解释了四次方程可解的对称性（如拉格朗日解析度）。
- **布尔代数**：  
  克莱因四元群是布尔群的一个例子，其元素的运算类似于集合的对称差运算。
- **环论**：  
  在某些环的构造中，克莱因四元群作为加法群的结构出现。例如，四元素环的加法群通常是 \( K_4 \)。

**7. 特殊性质**:

- **初等阿贝尔群**：  
  克莱因四元群是初等阿贝尔2群，即所有非单位元的阶均为素数2。
- **与二面体群的关系**：  
  克莱因四元群同构于二面体群 \( D_2 \)（4阶二面体群），但不同于更高阶的二面体群（如 \( D_4 \)）。
- **唯一性**：  
  四阶群在同构意义下只有两种类型：循环群 \( \mathbb{Z}_4 \) 和克莱因四元群 \( K_4 \)，因此 \( K_4 \) 是唯一的非循环四阶群。

**总结**:
克莱因四元群是群论中一个典型的 **非循环阿贝尔群**，其核心性质包括：

- 所有非单位元的阶均为2；
- 作为直积 \( \mathbb{Z}_2 \times \mathbb{Z}_2 \) 或几何对称群存在；
- 自同构群为 \( S_3 \)，子群结构简单；
- 在代数、几何和物理中均有重要应用。

$\boxed{K_4 \text{ 是阶为4的非循环阿贝尔群，其元素的阶均为1或2，且同构于} \ \mathbb{Z}_2 \times \mathbb{Z}_2}$

## 一些证明整理

**题目** 设 $N \unlhd G$, $\varphi$是G到G'的同态, 求证$\varphi (N) \unlhd G$ (正规子群的同态像也是正规子群)

**证明** 首先, 

**题目** 设 $H\unlhd G$, $N\unlhd G$, 求证: $G/HK \cong (G/H)/(HK/H)$

**题目** 设G是群, C是G的中心,证$G/C \cong Inn \ G$

**题目** R是实数加群,$R \times R$关于分量加法构成群, $N=\{ \langle 0,b \rangle | b \in R\}, 证N是$R \times R$的正规子群, 且$(R \times R)/N \cong R$

## 做题

怎么证明同构?
(1)定义: 同态 + 双射
(2)同态基本定理, 其中一个群是商群

与有限群相关的数量结果

1. $|G| = [G:H] |H|$

   $|G| = |G/H| |H|$

   $|a| \mid |G|$, $a \in G$

2. $f: G \to G'$ 是满同态 $\Rightarrow |G'| \mid |G|$ 且 $|G'| = |G/\ker f|$

3. $|G| = n$, $p$ 为素数, $p \mid n$, $G$ 为 Abel 群

   $\Rightarrow G$ 中含 $p$ 阶元

4. $|\overline{a}| = [G:N(a)]$

   $a$ 的正规化子 $N(a) = \{x \in G | xa = ax\}$

5. $A$, $B$ 是 $G$ 的子群, $A$, $B$ 有限, 则 $|AB| = \frac{|A||B|}{|A \cap B|}$