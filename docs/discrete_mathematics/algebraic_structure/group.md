# 群

## 群的理解

- 同态核 $ker \phi$ 是特殊的正规子群
- 群G可以对正规子群做商群
- 若中心达到整个群, 则整个群为Abel群

## 群的定义和性质

**群的定义 1** $\langle G,\circ \rangle$是一个含有二元运算的代数系统,如果满足:

(1) $\circ$ 运算是可结合的

(2) 存在 $e \in G$ 是关于 $\circ$运算的单位元

(3) $\forall x \in G, \exists x^{-1} \in G, s.t. \ x \circ x^{-1} = e(x^{-1}是x的逆元)$

则称G为一个群


**定理 1** 设 $\langle G, \circ\rangle$ 是具有一个可结合二元运算的代数系统，若存在 $e\in G$，使得 $\forall a\in G$，有 $a\circ e=a$，且 $\forall a\in G$，存在 $a_0\in G$ 满足 $a\circ a_0=e$，则 $G$ 是一个群。

即, 对于一个可结合二元运算的代数系统G, 若同时存在右单位元和右逆元(或者,同时存在左单位元和左逆元), 则G是群

即: 对于半群G, 若存在左单位元e, 且任意元素a, 关于e存在左逆元, 求证G是群:
$\forall a \in G, \exists a' \in G, s.t. a'a = e$
$ee = e \Rightarrow a'ae = a'a \Rightarrow ae = a$ 故e是右单位元,是单位元
接下来证$a'$是a的右逆元, 也就是证明a是a'的左逆元($aa' = e$)
设$a'$的左逆元为$a''$($a''a' = e$),需证$a'' = a$
有$a'' = a''e = a''(a'a) = (a''a')a = ea = a$


**定义 2** 定义:
(1) 若群G中只有一个元素, 即$|G|=1$, 即$G=\{e\}$,称G为平凡群
(2) 若群G中运算满足交换律,则称G为交换群,也叫Abel群

**定义 3** 群G的基数称为群G的阶, 记为|G|, 根据|G|的有限性, 将G区分为有限群和无限群

附:

- 有限群才能使用Lagrange定理
- 无限群有无穷多个子群

**定义 4** 群G中元素a的n次幂($n \in Z$)定义为:
$a^0=e, \ a^n=a^{n-1}a(n>0), \ a^n={(a^{-1})}^{-n}(n<0)$

附:

- 半群中可以定义正整数次幂
- 独异点中可以定义0次幂,定义自然数次幂
- 群中可以定义整数次幂

**定义 5** G是群,$a \in G$, 使得$a^k=e$成立的最小正整数k称为a的阶,记作$|a|$

**定理 2** $G$ 为群，$\forall a,b\in G$ 有  
(1) $(a^{-1})^{-1}=a$;  
(2) $(ab)^{-1}=b^{-1}a^{-1}$;  
(3) $a^n a^m = a^{n+m}, m,n\in \mathbb{Z}$;  
(4) $(a^n)^m = a^{mn}, m,n\in \mathbb{Z}$;  
(5) 若 $G$ 为 Abel 群，$(ab)^n = a^n b^n, n\in \mathbb{Z}$.

**定理 3** $G$ 为群，$\forall a,b\in G$，方程 $ax=b$ 和 $ya=b$ 在 $G$ 中有解且有惟一解.

**定理 4** 设 $G$ 是半群，如果 $\forall a,b\in G$ 方程 $ax=b$ 和 $ya=b$ 在 $G$ 中有解，则 $G$ 是群.

(证: 找右单位元和任意元素的右逆元)

**定理 5** 群中运算满足消去律.

推论: 非平凡群一定不存在零元

$G$是群, 若$G$中存在零元$\theta$, 那么$\forall a \in G, a\theta = \theta$,由消去律可得, $a=e$, 此时群中只有一个元素$e$,是平凡群

**定理 6** 设 $G=\{a_1,a_2,\ldots,a_n\}$ 为有限群，则 $G$ 的运算表的每行每列都是 $G$ 中元素的一个置换.即$aG = G, Ga=G$

**定理 7** 设 $G$ 是具有一个二元运算的不含零元的有限代数系统，且该运算适合结合律和消去律，则 $G$ 是一个群.

$G$ 是有限半群,且不含零元,若G中消去律成立， 则G是群

证 设$G={a_1,a_2,…,a_n}$，任取$a_i \in G$，有 $a_iG=\{a_ia_j | j=1, 2, …, n\}$ 由封闭性知, $a_iG \subseteq G$, 假设$|a_iG| < n$, 则存在j, k使得$a_ia_j=a_ia_k$, 根据消去律，$a_j=a_k$, 矛盾！所以$a_iG=G$. 任取$a_i, a_j$, 则方程$a_ix=a_j$有解。 同理，方程$ya_i=a_j$有解。因此，G是群

注：$<Z_5, \otimes>$不是群，因为有零元0；<Z+, >也不是群，无限.

**定理 8** $G$ 是群，$a\in G$ 且 $|a| = r$，则  
(1) $a^k=e$ 当且仅当 $r\mid k$，$k \in \mathbb{Z}$；  
(2) $|a|=|a^{-1}|$；  
(3) 若 $|G|=n$ 则 $r\leq n$.

(1) 𝒂 = 𝟏或𝟐 ⇔ 𝒂 = 𝒂−𝟏 (2) 𝒂 = 𝒂−𝟏 , 𝒂𝒃 = 𝒃𝒂 , 𝒂 = 𝒃𝒂𝒃−𝟏 (3) 𝒂 = 𝒓 ⇒ 𝒂𝒕 = 𝒓 (𝒕, 𝒓) (4) 𝒂 = 𝒏, 𝒃 = 𝒎, 𝒂𝒃 = 𝒃𝒂 ⇒ 𝒂𝒃 | 𝒏, 𝒎 ； 若 𝒏, 𝒎 = 𝟏, 则 𝒂𝒃 = 𝒏𝒎.

证明方法 20 证明元素的阶相等或求元素的阶的方法 证|𝒙| = |𝒚|： 令|𝒙| = 𝒓, |𝒚| = 𝒔, 验证 𝒙 𝒔 = 𝒆 ⇒ 𝒓|𝒔 验证 𝒚 𝒓 = 𝒆 ⇒ 𝒔|𝒓 求|𝒙|： 找到满足𝒙𝒏 = 𝒆的𝒏, 分析𝒏的因子. 证明群的一些基本性质的方法 工具---幂运算规则、结合律、消去律、群方程的解

例:
1. 只含有1/2阶元的群为Abel群
例2 若群𝑮中只有唯一2阶元，则这个元素与𝑮中所有元 素可交换. 证 ∀𝒙, 𝒚 ∈ 𝑮, 𝒙𝒚 = 𝒙𝒚 −𝟏 = 𝒚−𝟏𝒙−𝟏 = 𝒚𝒙 分析 𝒙𝟐 = 𝒆 ⇔ 𝒙 = 𝒙−𝟏 幂运算规则 证 设2阶元为𝒙, ∀𝒚 ∈ 𝑮, 𝒚𝒙𝒚−𝟏 = 𝒙 = 𝟐 ⇒ 𝒚𝒙𝒚−𝟏 = 𝒙 ⇒ 𝒚𝒙 = 𝒙𝒚 分析 |𝒚𝒙𝒚−𝟏| = |𝒙|


## 子群

**子群定义 6** G为群,H是G的非空子集,若H关于G中运算构成一个群,称H为G的子群,记为$H \leq G$, 若子群H是G的真子集,称为真子群,记为$H<G$

$H \leq G$

子群𝑯就是𝑮的子代数. 假若𝑯的单位元为𝒆′, 且x在𝑯中相对𝒆′的逆元为𝒙′, 则 𝒙𝒆′ = 𝒙 = 𝒙𝒆 ⇒ 𝒆′ = 𝒆 𝒙𝒙′ = 𝒆′ = 𝒆 = 𝒙𝒙−𝟏 ⇒ 𝒙′ = 𝒙−𝟏

定义(性质)

(1) $\forall a_1, a_2, \cdots a_n \in H, a_1 a_2 \cdots a_n \in H$ (封闭性)

(2) H中元素满足结合律

(3) $e \in H$ (存在单位元)

(4) $\forall a \in H, a^{-1} \in H$ (存在逆元)

**判定**:

**定理 9** (子群判定定理一) $G$ 是群，$H$ 是 $G$ 的非空子集，则 $H$ 是 $G$ 的子群当且仅当  (封闭性+逆元)
(1) $\forall a,b\in H$ 有 $ab\in H$，  
(2) $\forall a\in H$ 有 $a^{-1}\in H$.

**定理 10** (子群判定定理二) $G$ 是群，$H$ 是 $G$ 的非空子集，则 $H$ 是 $G$ 的子群当且仅当 $\forall a,b\in H$ 有 $ab^{-1}\in H$.

**定理 11** (子群判定定理三) $G$ 是群，$H$ 是 $G$ 的有穷非空子集，则 $H$ 是 $G$ 的子群当且仅当 $\forall a,b\in H$ 有 $ab\in H$. (有限子集+封闭性)

证明: 构造判定定理一即可, 若a=e,a^-1=a=e存在, 若a!=e,取$<a> \subseteq G$,由于有限,存在$i<j, a^i = a^j, a^{j-i}=e, j-i>1$, 则$a^{-1} = a^{j-i-1}$存在

附:

- 对于群G, $\forall a \in G$, $\langle a \rangle = \{a^k | k \in Z\}$, 有$\langle a \rangle \leq G$, 即群中元素生成的循环群一定是G的子群,即a生成的**循环子群**
- 对于群G, 令$C=\{a|a \in G 且 \forall x \in G(ax = xa)\}$, 则C是G的子群,称为**中心子群**,简称中心
- 对于群G,H是G的子群,令$xHx^{-1}=\{xhx^{-1} | h \in H\}$, 则$xHx^{-1}$是G的子群,称为H的**共轭子群**
- 子群的交仍是子群. 即$G为群, H \leq G, K \leq G, 则H \cap K \leq G$

**AB构成子群的条件**
(1) $AB \leq G \leftrightarrow AB=BA$
(2) $AB \leq G \rightarrow AB=\langle A \cup B \rangle$ 

附:
$A \subseteq AB, B \subseteq AB$

H1, H2为r, s 阶子群，(r, s)=1, 则 $H1 \cap H2 = \{e\}$

### 生成子群

**$\langle a \rangle$定义**:

G为群,$a \in G$,
$\langle a \rangle = \{ a^k, k \in \mathbb{Z} \}$,
则$\langle a \rangle \leq G, 且 |\langle a \rangle | = |a|$

附:

- 若G中存在n阶元a, 则G中存在n阶子群$\langle a \rangle$

**$\langle B \rangle$定义**:

G为群,B是G的非空子集,令$$S = \{H|H \leq G 且 B\subseteq H\}$$

则S非空,设$K = \cap S$, 则K为B的生成的子群, 记为$K=\langle B \rangle$

(1)$\langle B \rangle \leq G$, $\langle B \rangle \subseteq G$

(2)$\langle B \rangle = \{ {b_1}^{e_1} {b_2}^{e_2} \cdots {b_n}^{e_n} | n \in \mathbb{Z^+} 且 b_i \in B, e_i = \pm 1 \}$ 这里是因为群要求逆元存在和封闭

性质:

- $\forall b \in B, b \in \langle B \rangle$
- $b_i \in B, b_i \in \langle B \rangle, b_i^{-1} \in \langle B \rangle, b_ib_j \in \langle B \rangle...$

### 中心子群

对于群G, 令$C=\{a|a \in G 且 \forall x \in G(ax = xo.m a)\}$, 则C是G的子群,称为**中心子群**,简称中心

### 共轭子群

G是群, $H \leq G$, $\forall x \in G$,

$$xHx^{-1} = \{xhx^{-1} | h \in H\}$$,
则$xHx^{-1}$是G的子群, 称为H的共轭子群

附:

- 可以在H和$xHx^{-1}$之间建立双射, 有$xHx^{-1} \approx H$
- 即若$H \leq G, \forall g \in G, gHg^{-1} \leq G, 且 |gHg^{-1}|=|H|$
	- 若H是G的唯一n阶子群,有$gHg^{-1} = H$,有H是G的正规子群

### 正规子群(不变子群) normal subgroup

**正规子群定义**:

左右陪集相等的子群是正规子群, 记作$N \unlhd G$
即对于$H\leq G, \forall a \in G, aH = Ha$

**正规子群的判定定理** $N$ 是群 $G$ 的子群，则下列条件互相等价.  
(1) $N \unlhd G$；  
(2) $\forall g\in G$ 有 $gNg^{-1}=N$；  
(3) $\forall g\in G$，$\forall n\in N$ 有 $gng^{-1}\in N$.

其他的判定方法:
(1) $|N|=n$, N是G的唯一n阶子群
(2) N是G的子群且$[G:N] = 2$ (只有2个左(右)陪集)

证明: $\forall g \in G, 若g \in N,则gN=N=Ng; 若g \notin N,则gN=G-N=Ng,故N正规子群$

**性质**
(1) 正规子群的交仍是正规子群
(2) 正规子群的乘积仍是正规子群
证明: 由于正规子群左右陪集相等,所以$HK=KH \Leftrightarrow HK\leq G$ , 再由正规子群定义可以证明 $HK \unlhd G$, 同时还有 $H \unlhd HK$

例:

群G的两个平凡子群G和$\{e\}$是G的正规子群

Abel群的所有子群H都是正规子群($aH = Ha$)

$H \leq G, |H| = n$ 若H是唯一的n阶子群, 则 $H \unlhd G$

**附** 正规子群

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

(2) 若 $G$ 是 $n$ 阶循环群，则 $G$ 有 $\phi(n)$ 个生成元. 当 $n=1$ 时，$G=\langle e\rangle$ 的生成元是 $e$，当 $n>1$ 时，对每一个小于等于 $n$ 的正整数 $r$，$a^r$ 是 $G$ 的生成元当且仅当 $(n,r)=1$.

**证明**: 

(2) n=1结论为真. 下面考虑n>1 (n, r)=1  u,vZ s.t. un+rv=1 a=aun+rv =(ar)v  ar为生成元 反之，若ar为生成元，则|𝒂𝒓| = 𝒏. 另一方面，由|𝒂| = 𝒏 知，|𝒂𝒓| = 𝒏 (𝒏,𝒓) ，故 𝒏, 𝒓 = 𝟏

**循环群的`子`群**:

$G=\langle a\rangle$ 是循环群，那么

(1) $G$ 的子群也是循环群；  子群H中**最小正方幂元**$a^m$为H的生成元

(2) 若 $G$ 是无限阶的，则 $G$ 的子群除 $\{e\}$ 以外仍是无限阶的；  

(3) 若 $G$ 是 $n$ 阶的，则 $G$ 的子群的阶是 $n$ 的因子，对于 $n$ 的每个正因子 $d$，在 $G$ 中有且仅有一个 $d$ 阶子群, 即 $\langle a^{\frac{n}{d}} \rangle$是这个d阶子群

## 变换群与置换群

变换群的定义 A上的变换： f: A→A A上的一一变换： 双射f: A→A A上的一一变换群：E(A)={ f | f: A→A为双射} 关于变换乘法构成群 A上的变换群G： G  E(A) 实例 G为群，aG，令fa: G→G, fa(x)=ax，则fa为一一变换. H={ fa | aG }关于变换乘法构成G上的变换群. H  E(G)

怎样证明H同构于G?

### n元置换群

当|A|有限时，A上的一一变换称为A上的置换。当 |A| = n时称A上置换为n元置换

定理：若𝝈和𝝉是两个不相交的n元置换，则𝝈𝝉 = 𝝉𝝈.

定理1 任何n元置换都可以表成不交的轮换之积， 并且表法是唯一的

置换的乘法：函数的合成 
例：8元置换=(132)(5648)，=(18246573), 则 =(15728)(3)(4)(6)=(15728) 
置换求逆：求反函数 
=(132)(5648)，−1=(8465)(231)

令Sn为{1, 2,…, n}上所有n元置换的集合. Sn关于置换乘法构成群，称为n元对称群.
Sn的子群称为n元置换群

置换群的实例 
Cayley定理 每个群G都与一个变换群同构. 
推论 **每个有限群都与一个置换群同构.**

$A_n$是$S_n$中全体偶置换的集合,则$A_n \leq S_n$,称为n元交错群
(A是有穷集合,只需证明$A_n$对$S_n$中的乘法封闭)

### 轮换

下面 $xxx$ 和 $yyy$ 不交:
$(a \ xxx)(a \ yyy) = (a \ yyy \ xxx)$
$(a \ xxx \ yyy) = (a \ yyy)(a \ xxx)$

例:

$(i_1 \ i_2 \cdots i_k) = (i_1 \ i_k)(i_1 \ i_2 \cdots i_{k-1}) = \cdots = (i_1 \ i_k) (i_1 \ i_{k-1}) \cdots (i_1 i_2)$

即: **任意轮换可以表示为对换之积,但是表示不唯一**,但是对换个数的奇偶性一致

奇置换、偶置换 奇置换：表成奇数个对换之积 偶置换：表成偶数个对换之积(恒等置换是偶置换) 奇置换与偶置换之间存在一一对应，因此各有n!/2个

## 群的等价类划分

### 群的陪集分解 => Lagrange 定理

**左陪集定义** G为群,H是G的子群,$a \in G$, 称$aH=\{ ah | h \in H\}$为H在G中的一个左陪集, a称为代表元

同样,有右陪集的定义

**左陪集的性质**

设 $G$ 是群，$H$ 是 $G$ 的子群，则  
(1) $eH=H$；  
(2) $\forall a\in G$, $a\in aH$；  
(3) $\forall a\in G$, $aH\approx H$；  
(4) $\forall a,b\in G$, $a\in bH \Leftrightarrow aH=bH \Leftrightarrow a^{-1}b\in H$；  
(5) 在 $G$ 上定义二元关系 $R$，$\forall a,b\in G$，$aRb \Leftrightarrow a^{-1}b\in H$，则 $R$ 为 $G$ 上的等价关系，且 $[a]_R=aH$；  
(6) $\forall a,b\in G$, $aH\cap bH=\emptyset$ 或 $aH=bH$，且 $\bigcup_{a\in G} aH=G$.

**右陪集的性质**

设 $G$ 是群，$H$ 是 $G$ 的子群，则 
(1) $He=H$;  
(2) $\forall a\in G$, $a\in Ha$.
(3) $\forall a\in G$, $Ha\approx H$.
(4) $\forall a,b\in G$ 有 $a\in Hb \Leftrightarrow Ha=Hb \Leftrightarrow ab^{-1}\in H$.
(5) 在 $G$ 上定义二元关系 $R$，$\forall a,b\in G$ 有 $aRb \Leftrightarrow ab^{-1}\in H$, 则 $R$ 为 $G$ 上的等价关系，则 $[a]_R=Ha$.
(6) $G$ 是群，$H$ 是 $G$ 的子群，则 $\forall a,b\in G$, $Ha\cap Hb=\varnothing$ 或 $Ha=Hb$，且 $\bigcup_{a\in G} Ha=G$.

**Lagrange定理的引理** H 的左陪集和右陪集个数相等

证明: 设 $f:T→S,  f(Ha)=a^{-1}H$

其中 T,S 分别为右陪集和左陪集的集合。

f 的良定义性与单射性： $Ha=Hb \Leftrightarrow ab^{-1}∈H \Leftrightarrow (a^{−1})^{-1}b^{−1} \in H \Leftrightarrow a^{-1}H=b^{-1}H \Leftrightarrow f(Ha)=f(Hb)$

H 在 G 中的指数 $[G:H]$ 定义为 H 在G中的右（或者左）陪集个数

**定理 26** (Lagrange 定理) 设 $G$ 是有限群，$H$ 是 $G$ 的子群，则 $|G|=[G:H]|H|$.

令G 的不同的陪集为 Ha1, Ha2, … , Har , |G| = |Ha1| + |Ha2| +⋯+ |Har| = |H|r = 𝑯 [𝑮: 𝑯]

有限群G 的任意子群的阶是群G的阶的因子

**推论 1** $G$ 是 $n$ 阶有限群，则 $G$ 中每个元素的阶是 $n$ 的因子，且 $\forall a\in G$ 有 $a^n=e$.

证明: 构造子群$\langle a \rangle$, $|a| = |\langle a \rangle|$是G的阶段因子

**推论 2** 阶为素数的群是循环群.

|G| = p, p>1, 存在非单位元 a, |a|的阶是p的因子，只能是|a| = p. 故$G=<a>$

**Lagrange定理的应用**

例1 6 阶群必含3 阶元
例2 6 阶群在同构意义下只有 2 个. 证明思路： 若G含6阶元，是循环群Z6. 若不含6阶元，则含 3 阶元a, 取c{e, a, a2}, 则c, ac, a2c两两不等（消去律） 可以证明G={e, a, a2, c, ac, a2c}同构于S3. 推广 10 阶群只有2个，2p阶群只有2个. 4 阶群只有2个：循环群Z4和 Klein 四元群

A4没有6阶子群
𝑨𝟒是说明拉格朗日定理的逆命题一般不成立的最小 群：给定一个有限群G和|G|的一个因子d，不一定存在G 的一个d阶子群
### 群的共轭类分解 => 群的分类方程

**共轭关系定义**:

$a\in G, b\in G$,
$$def \ R: aRb \leftrightarrow \exists x \in G, s.t. \ b = x^{-1}ax$$

易证, 共轭关系是G上等价关系, 等价类为 $\bar{a} = [a]_R$

**定理 28** $G$ 是群，$C$ 是 $G$ 的中心，则 $\forall a\in G$ 有 $a\in C \Leftrightarrow \bar{a}=\{a\}$.

**定理 29** $G$ 是群，则 $\forall a\in G$，$N(a)$ 是 $G$ 的子群.

**定理 30** $G$ 是有限群，则 $\forall a\in G$ 有 $|\bar{a}|=[G:N(a)]$.

$$
\bar a = \{ xax^{-1} | x \in G\} 与 \{xN(a) | x \in G\}有双射关系
$$
若$[G: N(a)] = 1, 则 |\bar a|=1, 即\bar a = \{a\}, 即a\in C$

![[Pasted image 20250421213514.png]]


**定理 31** (群的分类方程) $G$ 是有限群，$C$ 是 $G$ 的中心. 设 $G$ 中至少含有两个元素的共轭类有 $k$ 个，且 $a_1,a_2,\ldots,a_k$ 分别为这 $k$ 个共轭类的代表元素，则  
$$
|G|=|C|+[G:N(a_1)]+[G:N(a_2)]+\cdots+[G:N(a_k)].
$$

## 商群

$G为群, N \unlhd G$,定义:
$$
G/N=\{Na|a\in G\}, (Na)(Nb)=Nab
$$
称$G/N$为商群
良定义性质：$Na=Nx, Nb=Ny \Rightarrow Nab=Nxy$

商群G/N 就是商代数:
同态f $f:G \rightarrow G/N, f(a) = Na$
由该同态导出的同余关系 $aRb \Leftrightarrow Na=Nb \Leftrightarrow ab^{-1}\in N$
说明: (1) $aRb, cRd \Rightarrow ac(bd)^{−1} \in N \Rightarrow acRbd$
(2) $aRb \Rightarrow ab^{−1} \in N \Rightarrow a^{−1}(b^{−1})^{−1} \in N \Rightarrow a^{−1}Rb^{−1}$
$G/N$是该同余关系导出的商代数

命题：设𝑮是一个群，𝑵是𝑮的正规子群. 
(1) 若𝑯是𝑮的子群且𝑵 ⊆ 𝑯，则𝑵是𝑯的正规子群， 𝑯/𝑵是𝑮/𝑵的子群. 
(2) 若𝑳是𝑮/𝑵的子群，则存在𝑮的子群𝑯，使得𝑵 ⊆ 𝑯且𝑳 = 𝑯/𝑵. (提示: 取 $H=\{a\in G | Na \in L\}$)

**附:**
(1) 对于Abel群,由于其所有子群H都是正规子群, 可以构造商群 $G/\langle a \rangle$, 若$a \neq e$,有$|G/\langle a \rangle| < |G|$

**商群性质:**
(1) $| G/N | = [G:N]$, 商群的阶是$|G|$的因子, 商群的阶是正规子群的指数
(2) 商群保持G的交换性/循环性

例:
(1) G为Abel群，|G|=n, 素数p整除n, 则G中有p阶元.
(2) 设p, q为互异素数，则pq阶Abel群必为循环群。
例如，6=2 \* 3阶交换群只能是6阶循环群；10=2 \* 5 阶交换群只能是10阶循环群

## 群的同态与同构

给定群G1和G2，称f为G1到G2的同态，如果 $f: G1→G2, 且\forall x, y \in G1，f(xy)=f(x)f(y)$
将群看成代数系统$\langle G, ∘, -1, e \rangle$，则同态f 满 足：$f(e_1)=e_2，f(x^{−1})=f(x)^{−1}$

**同态保持元素的性质**
$f(e_1)=e_2$, $f(x^{-1})=f(x)^{-1}$，满同态 $f$ 将生成元映到生成元。
$|f(a)|$ 整除 $|a|$，同构条件下 $|f(a)|=|a|$ 

**同态保持子代数的性质** 
$H\leq G_1 \Rightarrow f(H)\leq G_2$
$H\unlhd G_1$, $f$ 为满同态时，$f(H)\unlhd G_2$ 

同态核
$\text{ker}f\overset{\text{def}}{=}\{x\in G | f(x)=e_2\}$

**同态核的性质**
$e_1 \in \text{ker} f$
$\text{ker}f\unlhd G_1$
$\forall a,b\in G_1$, $f(a)=f(b) \Leftrightarrow a\text{ker}f=b\text{ker}f$ 
$f(a)=f(b) \Leftrightarrow f(a)^{–1}f(b)=e_2 \Leftrightarrow f(a^{−1}b)=e_2 \Leftrightarrow a^{-1}b \in kerf \Leftrightarrow akerf = bkerf$
$\text{ker}f=\{e_1\} \Leftrightarrow f$ 为单同态

**同态基本定理** 
(1) $N$ 为 $G$ 的正规子群，则 $G/N$ 是 $G$ 的同态像。 即任何群均与其商群同态，或**商群总是群的同态像**
(2) 若 $G'$ 为 $G$ 的同态像($f(G)=G'$)，则 $G/\text{ker}f\cong f(G)$. **群的同态像一定与kerf导出的商群同构**
(3) 在同构意义下， 群的同态像就是它的商群
(4) 确定群的全部同态像等价于找出该群的全部正规子群

推论 设𝑮与 $\bar 𝑮$是两个有限群，若存在满同态$𝝋: 𝑮 → \bar 𝑮$， 则 $|\bar G| | |G|$ .

定理4 设𝑮与 $\bar 𝑮$是两个群(不必有限)且𝝋: 𝑮 → $\bar 𝑮$是满同态，则当𝑮是循环群时， $\bar 𝑮$也是循环群。（等价的说法 是：循环群的同态像还是循环群
 循环群的子群还是循环群； 
 循环群的同态像还是循环群； 
 循环群的商群也是循环群

**同态映射下子群间的关系** 
定理5 设$φ: G → \overline{G}$是群$G$到群$\overline{G}$的满同态，$kerφ = K$，则$G$的包含$K$的子群与$\overline{G}$的所有子群之间可以建立一个保持包含关系的双射。即，令 $M = {H | H ≤ G, H ⊇ K}$，$\overline{M} = {\overline{H} | \overline{H} ≤ \overline{G}}$， 则$M$与$\overline{M}$之间可以建立一个保持包含关系的双射。

**定理6（第一同构定理）** 
设$\varphi$是群$G$到群$\overline{G}$的一个满同态，且$\ker\varphi\subseteq N\trianglelefteq G$，记$\varphi(N)=\overline{N}$，则 $G/N\cong\overline{G}/\overline{N}$，或$G/N\cong\varphi(G)/\varphi(N)$。 当$N=\ker\varphi$时，$\varphi(N)=\{\overline{e}\}$，$\overline{G}/\overline{N}=\overline{G}/\{\overline{e}\}\cong\overline{G}$，第一同构定理退化成同态基本定理。

推论 设$H\trianglelefteq G$，$N\trianglelefteq G$且$N\subseteq H$，则 $$G/H\cong\frac{G/N}{H/N}.$$ **证**：取自然同态$\varphi:G\to G/N$，$\varphi(a)=aN$，其核$\ker\varphi=N$。在第一同构定理中取$\overline{G}=G/N$，取$N$为这里的$H$，并注意$\varphi(H)=H/N$，由第一同构定理得$G/H\cong\frac{G/N}{H/N}$。
## 自同态与自同构

$End \ G$: G上的所有映射中自同态映射的集合
$Aut \ G$: G上的所有映射中自同构映射的集合
$Inn \ G$: G上的所有映射中内自同构映射的集合
内自同构映射: $f_a: \ G \rightarrow G, f_a(x)=axa^{-1}$

EndG 为独异点
AutG 为群 
InnG 为群，且 InnG ⊴ AutG.
$I_G=f_e \in InnG$


$G = \langle Z_6, \oplus \rangle$, G上的所有映射:
$f_p(x)=px(mod \ 6), p = 0,1,2,3,4,5$
这里G是交换群,
$End \ G = {f_0, f_1, \cdots , f_5}$
$Aut \ G = {f_1, f_5}$
$Inn \ G = {f_1}$

定理 设$G$是群，$C(G)$是$G$的中心，则 $\quad G/C(G) \cong InnG.$ 
只需要找一个G到Inn G的满同态即可
证：由定义知， $InnG = \{f_a | a \in G\}, f_a(x) = axa^{-1}, \forall x \in G,$ 在$G$与$InnG$之间建立映射： $\quad \sigma: G \to InnG, \sigma(a) = f_a, \forall a \in G$ 可证$\sigma$是一个满同态。 $ker\sigma = \{a \in G | f_a = I_G\} = \{a \in G | axa^{-1} = x, \forall x \in G\} = C(G).$ 故由同态基本定理得 $\quad G/C(G) \cong InnG.$

## 常见群

### 模n整数加群

$\langle Z, + \rangle$是一个群, 0为单位元, $x^{-1} = -x$

$\langle Z_n, \oplus \rangle$是一个群, 0为单位元, $x^{-1} = (n-x)mod \ n$

### 4阶群

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

## 定义汇总

**定义 1** 若$\langle G,\circ \rangle$是一个含有二元运算的代数系统,如果满足:

(1) $\circ$ 运算是可结合的

(2) 存在 $e \in G$ 是关于 $\circ$运算的单位元

(3) $\forall x \in G, \exists x^{-1} \in G, s.t. \ x \circ x^{-1} = e(x^{-1}是x的逆元)$

则称G为一个群

**定义 2** 定义:
(1) 若群G中只有一个元素, 即$|G|=1$, 即$G=\{e\}$,称G为平凡群
(2) 若群G中运算满足交换律,则称G为交换群,也叫Abel群

**定义 3** 群G的基数称为群G的阶, 记为|G|, 根据|G|的有限性, 将G区分为有限群和无限群

**定义 4** 群G中元素a的n次幂($n \in Z$)定义为:
$a^0=e, \ a^n=a^{n-1}a(n>0), \ a^n={(a^{-1})}^{-n}(n<0)$

**定义 5** G是群,$a \in G$, 使得$a^k=e$成立的最小正整数k称为a的阶,记作$|a|$

## 定理汇总

**定理 1** 设 $\langle G, \circ\rangle$ 是具有一个可结合二元运算的代数系统，若存在 $e\in G$，使得 $\forall a\in G$，有 $a\circ e=a$，且 $\forall a\in G$，存在 $a_0\in G$ 满足 $a\circ a_0=e$，则 $G$ 是一个群。

**定理 2** $G$ 为群，$\forall a,b\in G$ 有  
(1) $(a^{-1})^{-1}=a$;  
(2) $(ab)^{-1}=b^{-1}a^{-1}$;  
(3) $a^n a^m = a^{n+m}, m,n\in \mathbb{Z}$;  
(4) $(a^n)^m = a^{mn}, m,n\in \mathbb{Z}$;  
(5) 若 $G$ 为 Abel 群，$(ab)^n = a^n b^n, n\in \mathbb{Z}$.

**定理 3** $G$ 为群，$\forall a,b\in G$，方程 $ax=b$ 和 $ya=b$ 在 $G$ 中有解且有惟一解.

**定理 4** 设 $G$ 是具有一个可结合的二元运算的代数系统，如果 $\forall a,b\in G$ 方程 $ax=b$ 和 $ya=b$ 在 $G$ 中有解，则 $G$ 是群.

**定理 5** 群中运算满足消去律.

**定理 6** 设 $G$ 是具有一个二元运算的不含零元的有限代数系统，且该运算适合结合律和消去律，则 $G$ 是一个群.

即, 设G为有限半群, 且不含零元. 若G中消去律成立,则G是群

**定理 7** 设 $G=\{a_1,a_2,\ldots,a_n\}$ 为群，则 $G$ 的运算表的每行每列都是 $G$ 中元素的一个置换.

**定理 8** $G$ 是群，$a\in G$ 且 $|a|=r$，则  
(1) $a^k=e$ 当且仅当 $r\mid k$，$k\in \mathbb{Z}$；  
(2) $|a|=|a^{-1}|$；  
(3) 若 $|G|=n$ 则 $r\leq n$.

**定理 9** (子群判定定理一) $G$ 是群，$H$ 是 $G$ 的非空子集，则 $H$ 是 $G$ 的子群当且仅当  
(1) $\forall a,b\in H$ 有 $ab\in H$，  
(2) $\forall a\in H$ 有 $a^{-1}\in H$.

**定理 10** (子群判定定理二) $G$ 是群，$H$ 是 $G$ 的非空子集，则 $H$ 是 $G$ 的子群当且仅当 $\forall a,b\in H$ 有 $ab^{-1}\in H$.

**定理 11** (子群判定定理三) $G$ 是群，$H$ 是 $G$ 的有穷非空子集，则 $H$ 是 $G$ 的子群当且仅当 $\forall a,b\in H$ 有 $ab\in H$.

**定理 12** $G=\langle a\rangle$ 是循环群.  
(1) 若 $G$ 是无限阶循环群，则 $G$ 的生成元是 $a$ 和 $a^{-1}$.  
(2) 若 $G$ 是 $n$ 阶循环群，则 $G$ 有 $\phi(n)$ 个生成元. 当 $n=1$ 时，$G=\langle e\rangle$ 的生成元是 $e$，当 $n>1$ 时，对每一个不于等于 $n$ 的正整数 $r$，$a^r$ 是 $G$ 的生成元当且仅当 $(n,r)=1$.

**定理 13** $G=\langle a\rangle$ 是循环群，那么  
(1) $G$ 的子群也是循环群；  
(2) 若 $G$ 是无限阶的，则 $G$ 的子群除 $\{e\}$ 以外仍是无限阶的；  
(3) 若 $G$ 是 $n$ 阶的，则 $G$ 的子群的阶是 $n$ 的因子，对于 $n$ 的每个正因子 $d$，在 $G$ 中有且仅有一个 $d$ 阶子群, 即 $\langle a^{\frac{n}{d}} \rangle$是这个d阶子群

**定理 14** 设 $E(A)$ 是 $A$ 上的全体一一变换构成的集合，则 $E(A)$ 关于变换的乘法构成一个群.

**定理 15** 设 $\sigma,\tau\in S_n$，若 $\sigma$ 与 $\tau$ 是不相交的，则 $\sigma\tau=\tau\sigma$.

**定理 16** 任何 $n$ 元置换都可以表成不相交的轮换之积，并且表法是惟一的.

**定理 17** 设 $\sigma=(i_1i_2\cdots i_k)$ 是 $A=\{1,2,\ldots,n\}$ 上的 $k$ 阶轮换，$k>1$，则 $\sigma=(i_1i_k)(i_1i_{k-1})\cdots(i_1i_2)$.

**定理 18** $\sigma\in S_n$ 且 $\sigma(j)=i_j$，$j=1,2,\ldots,n$，则在 $\sigma$ 的对换表示中对换个数的奇偶性与排列 $\pi=i_1i_2\cdots i_n$ 中的逆序数的奇偶性一致.

**定理 19** $G$ 是 $n$ 元置换群.  
(1) $\sigma\in G$，$\sigma=(i_1i_2\cdots i_k)$，则 $|\sigma|=k$.  
(2) $\tau\in G$，$\tau=\tau_1\tau_2\cdots\tau_l$ 是不相交轮换的分解式，若 $\tau_i$ 是 $k_i$ 阶轮换，$i=1,2,\ldots,l$，则 $\tau$ 的阶是 $k_1,k_2,\ldots,k_l$ 的最小公倍数，即 $|\tau|=[k_1,k_2,\ldots,k_l]$.

**定理 20** 设 $G$ 是群，$H$ 是 $G$ 的子群，则  
(1) $He=H$;  
(2) $\forall a\in G$, $a\in Ha$.

**定理 21** 设 $G$ 是群，$H$ 是 $G$ 的子群，则 $\forall a\in G$, $Ha\approx H$.

**定理 22** $G$ 是群，$H$ 是 $G$ 的子群，$\forall a,b\in G$ 有 $a\in Hb \Leftrightarrow Ha=Hb \Leftrightarrow ab^{-1}\in H$.

**定理 23** $G$ 是群，$H$ 是 $G$ 的子群，在 $G$ 上定义二元关系 $R$，$\forall a,b\in G$ 有 $aRb \Leftrightarrow ab^{-1}\in H$, 则 $R$ 为 $G$ 上的等价关系，则 $[a]_R=Ha$.

**定理 24** $G$ 是群，$H$ 是 $G$ 的子群，则 $\forall a,b\in G$, $Ha\cap Hb=\emptyset$ 或 $Ha=Hb$，且 $\bigcup_{a\in G} Ha=G$.

**定理 25** 设 $G$ 是群，$H$ 是 $G$ 的子群，则  
(1) $eH=H$；  
(2) $\forall a\in G$, $a\in aH$；  
(3) $\forall a\in G$, $aH\approx H$；  
(4) $\forall a,b\in G$, $a\in bH \Leftrightarrow aH=bH \Leftrightarrow a^{-1}b\in H$；  
(5) 在 $G$ 上定义二元关系 $R$，$\forall a,b\in G$，$aRb \Leftrightarrow a^{-1}b\in H$，则 $R$ 为 $G$ 上的等价关系，且 $[a]_R=aH$；  
(6) $\forall a,b\in G$, $aH\cap bH=\emptyset$ 或 $aH=bH$，且 $\bigcup_{a\in G} aH=G$.

**定理 26** (Lagrange 定理) 设 $G$ 是有限群，$H$ 是 $G$ 的子群，则 $|G|=[G:H]|H|$.

**推论 1** $G$ 是 $n$ 阶群，则 $G$ 中每个元素的阶是 $n$ 的因子，且 $\forall a\in G$ 有 $a^n=e$.

**推论 2** 阶为素数的群是循环群.

**定理 27** 群 $G$ 上的共轭关系是 $G$ 上的等价关系.

**定理 28** $G$ 是群，$C$ 是 $G$ 的中心，则 $\forall a\in G$ 有 $a\in C \Leftrightarrow \bar{a}=\{a\}$.

**定理 29** $G$ 是群，则 $\forall a\in G$，$N(a)$ 是 $G$ 的子群.

**定理 30** $G$ 是有限群，则 $\forall a\in G$ 有 $|\bar{a}|=[G:N(a)]$.

**定理 31** (群的分类方程) $G$ 是有限群，$C$ 是 $G$ 的中心. 设 $G$ 中至少含有两个元素的共轭类有 $k$ 个，且 $a_1,a_2,\ldots,a_k$ 分别为这 $k$ 个共轭类的代表元素，则  
$$
|G|=|C|+[G:N(a_1)]+[G:N(a_2)]+\cdots+[G:N(a_k)].
$$

**定理 32** $N$ 是群 $G$ 的子群，则下列条件互相等价.  
(1) $N\triangleleft G$；  
(2) $\forall g\in G$ 有 $gNg^{-1}=N$；  
(3) $\forall g\in G$，$\forall n\in N$ 有 $gng^{-1}\in N$.

**定理 33** 设 $\phi$ 是群 $G_1$ 到 $G_2$ 的同态，则 $\phi$ 为单同态当且仅当 $\ker\phi=\{e_1\}$.

**定理 34** $G_1=\langle a\rangle$ 是循环群，$\phi$ 是 $G_1$ 到 $G_2$ 的满同态，则 $G_2$ 也是循环群.

**定理 35** 设 $\phi$ 是群 $G_1$ 到 $G_2$ 的同态.  
(1) 若 $H$ 是 $G_1$ 的子群，则 $\phi(H)$ 是 $G_2$ 的子群.  
(2) 若 $H$ 是 $G_1$ 的正规子群，且 $\phi$ 是满同态，则 $\phi(H)$ 是 $G_2$ 的正规子群.

**定理 36** 设 $\phi$ 是群 $G_1$ 到 $G_2$ 的同态，则  
(1) $\ker\phi$ 是 $G_1$ 的正规子群；  
(2) $\forall a,b\in G_1$, $\phi(a)=\phi(b) \Leftrightarrow a\ker\phi=b\ker\phi$.

**定理 37** (群同态基本定理) 设 $G$ 是群，$H$ 是 $G$ 的正规子群，则 $G$ 的商群 $G/H$ 是 $G$ 的同态像. 若 $G'$ 是 $G$ 的同态像，$G\stackrel{\phi}{\sim} G'$，则 $G/\ker\phi\cong G'$.

**群的同构定理**

**定理 38** $G$ 是群，则 $\mathrm{End}(G)$ 关于映射的合成运算构成一个独异点，$\mathrm{Aut}(G)$ 关于映身的合成运算构成一个群.

**定理 39** $G$ 是群，则 $\mathrm{Inn}(G)\triangleleft \mathrm{Aut}(G)$.

**定理 40** 设 $G$ 是群，$K$ 和 $L$ 是 $G$ 的子群，则 $G=K\times L$ 当且仅当下面的条件成立：  
(1) $K\triangleleft G, L\triangleleft G$;  
(2) $K\cap L=\{e\}$;  
(3) $G=KL$.

**定理 41** 设 $G$ 是群，$G_1,G_2,\ldots,G_n$ 是 $G$ 的子群，则 $G=G_1\times G_2\times\cdots\times G_n$ 当且仅当以下条件成立：  
(1) $G_i\triangleleft G, i=1,2,\ldots,n$；  
(2) $G_i\cap G_1G_2\cdots G_{i-1}G_{i+1}\cdots G_n=\{e\}, i=1,2,\ldots,n$；  
(3) $G=G_1G_2\cdots G_n$.

