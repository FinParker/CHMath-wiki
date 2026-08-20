# 环

## 环的定义和性质

**环的定义 18.1** $\langle R, + , \times \rangle$是具有两个二元运算的代数系统,如果
(1) $\langle R, + \rangle$构成Abel群
(2) $\langle R, \cdot \rangle$构成半群
(3) R中$\cdot$对+可分配
则$\langle R, + , \times \rangle$构成环

**常见的环** 整数环,有理数环,实数环,复数环
n阶实矩阵环
模n整数环
$\langle P(B), \oplus , \cap \rangle$构成环

环中的术语

- 通常称+运算为环中的加法，·运算为环中的乘法. 
- 环中加法单位元记作 $0$. 
- 乘法单位元（如果存在）记作 $1$.
- 环中加法单位元$0$恰好是乘法的零元. 
- 对任何元素$x$，称$x$的加法逆元为负元，记作$-x$. 
- 若$x$存在乘法逆元，则称之为逆元，记作$x^{-1}$. 
- 符号：$0, 1, -x, x^{-1}, nx, x^n, x-y$

**环的性质**

1. $a0=0a=0$  
2. $(-a)b=a(-b)=-(ab)$  
3. $(-a)(-b)=ab$  
4. $a(b-c)=ab-ac$，$(b-c)a=ba-ca$  
5. $(\sum_{i=1}^{n}a_i)(\sum_{j=1}^{m}b_j)=\sum_{i=1}^{n}\sum_{j=1}^{m}a_ib_j$  
6. $(na)b=a(nb)=n(ab)$

**环中的运算** 

环中加法满足交换律、结合律； 
乘法满足结合律； 
乘法对加法满足分配律

**特殊的环**

(1) 交换环
(2) 含幺环
(3) 无零因子环: $ab=0 \Rightarrow a=0 \lor b=0$
(4) 整环: 无零因子的含幺交换环, 平凡环$\{0\}$是整环
(5) 除环: 至少含2个元素(保证$R^{*}$非空)的环, 且$\langle R^{*}, \cdot \rangle$构成群, 这里$R^{*} = R - \{0\}$

**无零因子环的特征**

设𝑅是一个无零因子环，则𝑅中非零元的加法阶相等， 这个加法阶或者是∞，或者是个素数𝑝。

设𝑅是一个无零因子环，称𝑅中非零元的加法阶为环𝑅的 特征，记为Char𝑅。当𝑅中非零元的加法阶为无穷大时，称𝑅 的特征为零，记Char𝑅 = 0；当𝑅中非零元的加法阶为某个素 数𝑝时，称𝑅的特征为𝑝，记Char𝑅 = 𝑝

设𝑅 是特征为𝑝的交换环，则对∀𝑎, 𝑏 ∈ 𝑅 ，有$(𝑎 + 𝑏)^𝑝 = 𝑎^𝑝 + 𝑏^𝑝$
## 域

**域的定义**

前提: $R^{*}$非空, 即$|R|>1$
(1) 可交换的除环是域
(2) 每个元素都有逆元的整环
(3) 有限整环是域

**域的性质**

$\langle F, + , \times \rangle$是域, 则
(1) $\langle F, + \rangle$构成Abel群
(2) $\langle F^{*}, \cdot \rangle$构成Abel群
(3) F中$\cdot$对+可分配

可以在$F^{*}$中定义乘法逆元运算(除法运算)

设p为素数，证明$Z_p$是域

**证(I):** $p$为素数, $p\geq2$, 所以$|\mathbb{Z}_p|\geq2$。

易见$\mathbb{Z}_p$关于模$p$乘法可交换，单位元是$1$，且对于任意的$i,j,k\in\mathbb{Z}_p$, $i\neq0$有

$i\otimes j=i\otimes k \Rightarrow i\otimes(j-k)=0 \Rightarrow p|i(j-k) \Rightarrow p|j-k \Rightarrow j=k,$

因此$\mathbb{Z}_p^*$中消去律成立。

又$\mathbb{Z}_p^*$关于乘法$\otimes$构成有限半群，且不含零元，故$\mathbb{Z}_p^*$关于乘法$\otimes$构成群，从而$\mathbb{Z}_p$是域。

p, q为不等的素数，证明无pq阶的整环

**定理** 

一个至少含有两个元素的无零因子的有限环是除环 

只需证: 设$𝑅 = {0, 𝑎_1, ⋯ , 𝑎_𝑛}$是一个无零因子环，𝑛是正整数， $𝑎_𝑖 ≠ 0, 1 ≤ 𝑖 ≤ 𝑛$。$\langle R^{*} \rangle$构成群

## 子环

定义：
环R的非空子集关于环中运算$+, \cdot$ 构成环

子环就是子代数，平凡子环存在

**子环判定定理**

设R是环, S是R的非空子集,若
(1) $\forall a, b \in S, a - b \in S$  (加法子群判定)
(2) $\forall a,b \in S, ab \in S$    (乘法子半群判定)

## 理想子环

**理想子环定义**

I是环R的非空子集,若满足
(1) $\langle I, +\rangle$是$\langle R, +\rangle$的子群 
	即 $\forall a,b \in I, a-b \in I$
(2) $\forall r \in R, rI \subseteq I, Ir \subseteq I$
则称I为理想

若只满足$rI \subseteq I$,称为左理想, 若只满足$Ir \subseteq I$,称为右理想
平凡理想：{0}, R自身

**理想性质**
(1) 理想I是子环
(2) 若乘法单位元$1 \in I$, 则$I = R$

在交换环R中, $\forall x \neq 0, x \in R$, $Rx = \{rx|r\in R\}$, 有$Rx$是理想, ; 若$x = 0, \langle 0 \rangle = \{ 0 \}$

有人会问: 这不是与 当$R$是交换环时，$\langle\alpha\rangle=\{s\alpha+n\alpha \mid \forall s\in R,\forall n\in\mathbb{Z}\}$； 矛盾吗?
不是的, 因为如果$1 \notin R, x \notin Rx$

例1 R为交换环，$1 \in R$, 且$1 \neq 0$, 则R为域当且仅当 R只含有平凡理想

F[x]为数域F上的多项式环， I={a1x+a2x2+⋯+anxn|ai∈F, n∈ℕ}, 即I是由所有常数项为0的多项式构成的集合，则I 是F[x]的理想

## 商环

**商环定义**

若I为环R的理想, $\forall x \in R$, 取x的加法陪集 $\bar x = I + x = \{i+x|i\in I\}$
定义 $R/I = \{I + x | x \in R\}$, 其中加法运算 $(I+x) + (I+y) = I + (x+y)$
乘法运算 $(I+x)(I+y) = I+xy$
则$\langle R/I, +, \cdot \rangle$构成环, 称为R关于I的商环

## 环同态

**环同态**

- 环同态 $f:R_1\to R_2$  
    - $f(x+y)=f(x)+f(y)$  
    - $f(xy)=f(x)f(y)$  
- 同态核：$\text{ker}f=\{x\in R_1 \mid f(x)=0\}$  
- 实例  
    - $f_c:\mathbb{Z}\to\mathbb{Z}$, $f_c(x)=cx$, $c=0,1$  
        - $\text{ker}f_0=\mathbb{Z}$; $\text{ker}f_c=\{0\}$, $c\neq 0$  
    - $\varphi:\mathbb{Z}\to\mathbb{Z}_n$, $\varphi(x)=x\mod n$  
        - $\text{ker}\varphi=n\mathbb{Z}$  

**环同态的性质**

1. $f(0)=0$, $f(-x)=-f(x)$, $f(x^{-1})=f(x)^{-1}$

2.  (1) 若$S$是$R_1$的子环，则$f(S)$是$R_2$的子环.  
   (2) 若$T$是$R_2$的子环，则$f^{-1}(T)$是$R_1$的子环.  
   (3) 若$I$是$R_1$的理想，则$f(I)$是$f(R_1)$的理想.  
   (4) 若$I$是$R_2$的理想，则$f^{-1}(I)$是$R_1$的理想.  

3. 定义$\text{ker}f=\{x\in R_1 \mid f(x)=0\}$，则$\text{ker}f$是$R_1$的理想.称$\text{ker}f$为同态$f$的核.

## 环同态基本定理

**同态基本定理**

**定理** 环$R$的任何商环$R/I$均是$R$的同态像，即对于环$R$的任意理想$I$，均存在自然的满同态  
$\pi: R \rightarrow R/I, x \mapsto \bar{x}, \forall x \in R.$  
证：利用定义可以直接验证。  

**同态基本定理** 设$R,R'$是环，$f: R \rightarrow R'$是环同态，则$R/\ker f \cong f(R)$.  
证：类似于群同态基本定理可以证明。

**子集T生成的理想:**

设$R$是一个环，$T$是$R$的一个非空子集，则称$R$中所有包含$T$的理想的交为由$T$生成的理想，记为$\langle T\rangle$，即  
$\langle T\rangle=\cap\{I \mid I \supseteq T,I$是$R$的理想$\}$。  
特别地，若$T=\{\alpha\}$，则简记$\langle T\rangle$为$\langle\alpha\rangle$，称之为由$\alpha$生成的主理想。  

显然，$\langle T\rangle$是$R$中包含$T$的最小的理想。  

**定理**  
设$R$是环，$\forall a\in R$，则$\langle a \rangle=$  
$\{(x_1 a y_1+\cdots+x_ma y_m)+sa+at+na \mid \forall x_i,y_i,s,t\in R,\forall m,n\in\mathbb{Z}\}$  

证：利用理想的定义可以直接验证。  

**主理想（续）**  

**推论**  
设$R$是环，$\forall\alpha\in R$。则  
1) 当$R$是交换环时，$\langle\alpha\rangle=\{s\alpha+n\alpha \mid \forall s\in R,\forall n\in\mathbb{Z}\}$；  
2) 当$R$有单位元时，$\langle\alpha\rangle=\{x_1\alpha y_1+\cdots+x_m\alpha y_m \mid \forall x_i,y_i\in R\}$；  
3) 当$R$是含幺交换环时，$\langle\alpha\rangle=R\alpha=\{r\alpha \mid \forall r\in R\}=\alpha R$。  

**素理想和极大理想**

**定义** 设$P$是含幺交换环$R$的一个理想，$P\neq R$. $a,b\in R$, 如果$ab\in P\Rightarrow a\in P$或$b\in P$, 则称$P$是$R$的一个素理想。

**定义** 设$R$是环，$M$是$R$的理想，且$M\neq R$. 如果在$R$的所有理想中，除了$M$本身和$R$外，没有包含$M$的理想，则称$M$为$R$的极大理想。


**例** 整数环$\mathbb{Z}$中由素数$p$生成的理想$\langle p\rangle$是一个素理想，同时也是一个极大理想。
**证**: $\mathbb{Z}$ 中由素数 $p$ 生成的理想 $\langle p\rangle=\{pk|k\in\mathbb{Z}\}$. 若 $ab\in\langle p\rangle$, 则 $p|ab$. 由 $p$ 是素数知, $p|a$ 或 $p|b$. 因此有 $a\in\langle p\rangle$ 或 $b\in\langle p\rangle$, 故 $\langle p\rangle$ 是一个素理想。

由于 $1\notin\langle p\rangle$, 故 $\langle p\rangle\neq\mathbb{Z}$. 设 $I$ 是包含 $\langle p\rangle$ 的一个理想。若 $\langle p\rangle\neq I$, 则存在 $q\in I\setminus\langle p\rangle$. 由 $p$ 是素数可知, $q$ 与 $p$ 互素, 于是存在整数 $s$ 和 $t$, 使得 $sp+tq=1$. 又 $p\in I$, 而且 $I$ 是理想, 所以 $1\in I$, 进而有 $I=\mathbb{Z}$. 故 $\langle p\rangle$ 是一个极大理想。

---

定理 设 $R$ 是含幺交换环，则  
1) $M$ 是 $R$ 的极大理想当且仅当 $R/M$ 是域。  
2) $P$ 是 $R$ 的素理想当且仅当 $R/P$ 是整环。

**商域**

定理 对于每个整环𝑹，一定存在一个域𝑸，使得𝑹是𝑸的子环

取$Q = \{ \frac{b}{a} \mid a,b \in R, a \neq 0\}$

 约定 
 1) 𝑎 = 𝑎 / 1 , ∀𝑎 ∈ 𝑅, 1是𝑅的单位元。 
 2) 0 / 𝑎 = 0, ∀𝑎 ∈ 𝑅, 0是𝑅的零元。
 3) 𝑏𝑐 / 𝑎𝑐 = 𝑏/ 𝑎 , ∀𝑎, 𝑏, 𝑐 ∈ 𝑅, 𝑎 ≠ 0, 𝑐 ≠ 0

可以定义形式加法和乘法

 加法：𝑏 / 𝑎 + 𝑑 / 𝑐 = 𝑏𝑐+𝑎𝑑 / 𝑎𝑐 , ∀𝑎, 𝑏, 𝑐, 𝑑 ∈ 𝑅, 𝑎 ≠ 0, 𝑐 ≠ 0; 
 乘法：𝑏 / 𝑎 ⋅ 𝑑 / 𝑐 = 𝑏𝑑 / 𝑎𝑐 , ∀𝑎, 𝑏, 𝑐, 𝑑 ∈ 𝑅, 𝑎 ≠ 0, 𝑐 ≠ 0.