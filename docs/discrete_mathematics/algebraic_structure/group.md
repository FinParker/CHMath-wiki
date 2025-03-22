# 群

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
(3) 若 $G$ 是 $n$ 阶的，则 $G$ 的子群的阶是 $n$ 的因子，对于 $n$ 的每个正因子 $d$，在 $G$ 中有且仅有一个 $d$ 阶子群.

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

(3) $e \in H$

(4) $\forall a \in H, a^{-1} \in H$


### 生成子群

G为群,B是G的非空子集,令
$$S = {H|H \leq G 且 B\subseteq H}$$,
则S非空,设$K = \cap S$, 则K为B的生成的子群, 记为$K=<B>$

性质

(1)$<B>\leq G$, $<B>\subseteq G$

(2)$<B> = \{ {a_1}^{e_1} {a_2}^{e_2} \cdots {a_n}^{e_n} | n \in \mathbb{Z^+} 且 a_i \in B, e_i = \pm 1 \}$

## 轮换

$(a \ xxx)(a \ yyy) = (a \ yyy \ xxx)$
$(a \ xxx \ yyy) = (a \ yyy)(a \ xxx)$

例:

$(i_1 \ i_2 \cdots i_k) = (i_1 \ i_k)(i_1 \ i_2 \cdots i_{k-1}) = \cdots = (i_1 \ i_k) (i_1 \ i_{k-1}) \cdots (i_1 i_2)$

即: 任意轮换可以表示为对换之积,但是表示不唯一