# 组合数学

前置知识：
1. 生成函数(母函数)
2. 动态规划(知道怎么划分子问题就可以)
3. 组合数 $C(n, m)$
4. 第二类Stirling数

注: 这篇笔记是我在复习组合数学时所写, 欢迎转载, 转载请注明出处, 谢谢!

如发现有错误, 欢迎与我交流!

先看总结:



| 球相同 | 盒相同 | 允许空盒 | 放球方法数                                                            | 对应的组合问题                               |
| --- | --- | ---- | ---------------------------------------------------------------- | ------------------------------------- |
| 不同  | 相同  | 可空   | $P_{m}(n)$                                                       | 一个非负整数n如何无序拆分成m个非负整数                  |
|     | 相同  | 不空   | $Q_m(n) = P_{m}(n)-P_{m-1}(n)$                                   | 一个非负整数n如何拆分成m个**正整数**                 |
|     | 不同  | 可空   | $C(n+m-1,n)$                                                     | $x_{1}+x_{2}+\ldots+x_{m}=n$的非负整数解    |
|     | 不同  | 不空   | $C(n-1,m-1)$                                                     | $x_{1}+x_{2}+\ldots+x_{m}=n$的**正整数解** |
| 不同  | 相同  | 可空   | $\sum_{k=1}^{m}\left\{\begin{array}{l}n \\ k\end{array}\right\}$ | 第二类Stirling数求和                        |
|     | 相同  | 不空   | $\left\{\begin{array}{l}n \\ m\end{array}\right\}$               | 第二类Stirling数                          |
|     | 不同  | 可空   | $m^{n}$                                                          | 第二类Stirling数性质                        |
|     | 不同  | 不空   | $m!\left\{\begin{array}{l}n \\ m\end{array}\right\}$             | 第二类Stirling数+ 盒子全排列                   |


## 整数的无序拆分

先来谈一谈整数的无序拆分问题

对于正整数$N$, 将$N$无序拆分为正整数$a_1,a_2,...,a_n$

相当于把一个正整数N分解为$x_1$个$a_1$, $x_2$个$a_2$, $\cdots$, $x_n$个$a_n$, 这里$x_i$为非负整数

即相当于 $a_1x_1+a_2x_2+\cdots +a_nx_n=N$的正整数解$(x_1,x_2,\cdots x_n)$的个数

注: 另外,如果考虑N=0的情况, 我们一般规定这时的拆分方法数为1

(1.1) 如果我们要求拆分出来的正整数不能重复，即$\forall x_i, 0 \leq x_i \leq 1$

其生成函数

$$
G(x)=(1+x^{a_1})(1+x^{a_2})\cdots (1+x^{a_n})
$$

拆分方法数即为$G(x)$展开式中$x^N$的系数

(1.2) 如果我们要求拆分出来的正整数可以重复, 即$\forall x_i, x_i \geq 0$ 

其生成函数

$$
G(x)=(1+x^{a_1}+x^{2a_1}+\cdots)(1+x^{a_2}+x^{2a_2}+\cdots)\cdots (1+x^{a_n}+x^{2a_n}+\cdots)
$$

也就是

$$G(x) = \frac {1}{(1-x^{a_1})(1-x^{a_2})\cdots (1-x^{a_n})}$$

拆分方法数即为$G(x)$展开式中$x^N$的系数

(1.2.1) 考虑 (1.2) 的一个特殊情况, 考虑正整数n, 可以拆分成几个1, 几个2, 几个3, .$\cdots$, 几个m的和呢?

比如$n=5, m=3$, 可以有如下的拆分方法:

1. 5个1, 0个2, 0个3
2. 3个1, 1个2, 0个3
3. 2个1, 0个2, 1个3
4. 1个1, 2个2, 0个3
5. 0个1, 1个2, 1个3

转化成数学语言:

$$对于1 \cdot x_1+ 2 \cdot x_2+\cdots + m \cdot x_m=n $$

拆分方法数等同于上式的非负整数解的个数

由(1.2) 可得到生成函数

$$G(x)=(1+x^1+x^2+\cdots)(1+x^2+x^4+\cdots)\cdots (1+x^m+x^{2m}+\cdots)$$

即

$$
G(x) = \frac {1} {(1-x)(1-x^2)(1-x^3)\cdots(1-x^m)}
$$

拆分方法数即为$G(x)$展开式中$x^n$的系数

但使用生成函数有时并不直观, 这里我们可以使用一个简单的**分类讨论将这个问题转化为更小的子问题**:

回到这个例子:

比如$n=5, m=3$, 记这个问题为$T(5, 3)$可以有如下的拆分方法:

1. 5个1, 0个2, 0个3
2. 3个1, 1个2, 0个3
3. 2个1, 0个2, 1个3
4. 1个1, 2个2, 0个3
5. 0个1, 1个2, 1个3

按照分解的结果中是否含有3(最大的拆分数,也就是m)来讨论

1. 如果分解的结果中没有3($x_3=0$),那么相当于对$n=5, m=2$进行拆分, 即问题转化为$T(5,2)$
2. 如果分解的结果中至少有1个3, 那么我们可以考虑先从n=5中去掉1个3, 这样问题又转化为对$n=2, m=3$进行拆分, 即问题转化为$T(2,3)$

注: 我们发现,如果原问题时$n < m$, 那么分解的结果一定不含m,就只有第一种情况

按照这样的转化思路,我们可以得到

$$T(5,3)=T(5,2)+T(2,3)$$
进一步

$$T(5,2)=T(5,1)+T(3,2); T(2,3)=T(2,2)$$

$$T(5,1);T(3,2)=T(3,1)+T(1,2);T(2,2)=T(2,1)+T(0,2)$$

这里

$$T(5,1)=T(3,1)=T(2,1)=1, \ T(1,2) = T(0,2) = 1$$

不难发现最基本的情况只有2种:

1. $T(n,1) = 1$
2. $T(0,m) = 1$

代回去,可以得到 $T(5,3) = 5$

总结一下,下面就是我们对于这种拆分问题的递推方程

$$T(n,m) = T(n,m-1) + T(n-m, m) \ (n\geq m \geq 1)$$

$$T(n,m)=T(n,m-1)\ (n < m \land m \geq 1)$$

初始值:

$$T(n,1) = 1$$  $$T(0,m) = 1$$

## 小球放盒问题

小球放盒问题, 顾名思义就是把n个小球放入m个盒子中的不同方法数.

为了圆满解决小球放盒问题,我们需要对这个**大**问题分类:

1. 小球是否不同(小球是否编号)
2. 盒子是否不同(盒子是否编号)(是分组还是填盒子)
3. 盒子是否可空

注: 在这篇文章讨论的时候, n是可以为0的(方便表达递推方程. 规定n=0时方法数为1)
注: 对于盒子数m的话, 如果递推方程没有导出m=0的项, 我们都默认$m\geq 1$; 否则仍和n一样, 规定m=0时方法数为1

我们计数的时候只需要2个参数: 小球个数n,盒子个数m, 那么这个计数问题就是$T(n,m)$

排列组合得到8类问题, 我们下面逐个详细讨论

### 2.1 小球相同,盒子相同,盒子可空

n个相同小球,放入m个相同盒子,盒子可空,

这个问题等价于一个非负整数n如何拆分成m个非负整数,

二者之间容易建立一一对应关系.

比如$T(5,3)$, 拆分方法如下:

1. 0 0 5
2. 0 1 4
3. 0 2 3
4. 1 1 3
5. 1 2 2

不同位置的数相当于在不同的盒子里放几个小球

那么我们该如何求解呢?

我们这里还是使用划分子问题(动态规划)的方法: 

对于问题$T(n,m)$(盒子可空)

1. 如果盒子中有至少有一个是空盒, 我们可以想象拿走某个空盒子, 那么问题$T(n,m)$(盒子可空)的方法数就等于子问题$T(n,m-1)$(盒子可空)的方法数
2. 如果每个盒子中都至少有一个球, 我们可以想象从每个盒子中都取走一个球, 那么问题$T(n,m)$(盒子可空)的方法数就转化到了子问题$T(n-m,m)$(盒子可空)的方法数

讨论完这个, 我们在考虑一下不能被分解的基本子问题

1. T(n,1), n个相同小球放入1个盒子,可空, 显然只有1种方法
2. T(0, m), 显然只有1种方法

到这里, 聪明的你有没有发现什么华点?

**这个问题和(1.2.1)的整数拆分问题的结构完全一样!!!**

这就说明, 下面3个问题的答案是等价的:

1. n个相同小球,放入m个相同盒子, 盒子可空, 一共有多少方法数?
2. 一个非负整数n, 拆分成m个非负整数, 允许重复, 一共有多少拆分方法?
3. 一个非负整数n, 拆分成几个1,几个2,$\cdots$ 几个m, 一共有多少种拆分方法?

因此,对于**n个相同小球,放入m个相同盒子, 盒子可空**问题, 我们可以使用(1.2.1)的生成函数来求解,也就是

生成函数

$$G(x)=(1+x^1+x^2+\cdots)(1+x^2+x^4+\cdots)\cdots (1+x^m+x^{2m}+\cdots)$$

即

$$
G(x) = \frac {1} {(1-x)(1-x^2)(1-x^3)\cdots(1-x^m)}
$$

装盒方法数即为$G(x)$展开式中$x^n$的系数

当然我们也可以使用子问题分解的方法, 上文已经给出

这里我们使用一个记号

$$P_m(n) := 非负整数n拆分成m个非负整数,允许重复的方法数$$

当然也可以这样定义

$$P_m(n) := n个相同小球,放入m个相同盒子, 盒子可空的方法数$$

有

$$P_m(n) = P_{m-1}(n) + P_m(n-m) \ (n\geq m \geq 1)$$
$$P_m(n) = P_{m-1}(n) \ (n<m \land m \geq 1)$$
$$P_1(n) = 1 = P_m(0)$$


### 2.2 小球相同,盒子相同,盒子不空

n个相同小球,放入m个相同盒子,盒子不空,

这个问题等价于一个非负整数n如何拆分成m个**正整数**,

二者之间容易建立一一对应关系.

比如$T(5,3)$, 拆分方法如下:

1. 1, 1, 3
2. 1, 2, 2

不同位置的数相当于在不同的盒子里放几个小球

我们这里使用记号$Q_m(n)$来标记这个问题

$$Q_m(n) := 非负整数n无序拆分成m个正整数且不允许重复的方法数$$

还是规定 $Q_m(0)  = 1$

例如 $Q_3(5) = 2$ 有

1. 5 = 1 + 1 + 3
2. 5 = 1 + 2 + 2

$Q_3(8) = 5$ 有

1. 8 = 1 + 1 + 6
2. 8 = 1 + 2 + 5
3. 8 = 1 + 3 + 4
4. 8 = 2 + 2 + 4
5. 8 = 2 + 3 + 3

相信大家可能注意到了, 这个问题和上个问题有很多相似点:

比如对于n = 5 相同小球, m = 3相同盒子, 

如果盒子可空

1. 5 = 0 + 0 + 5
2. 5 = 0 + 1 + 4
3. 5 = 0 + 2 + 3
4. 5 = 1 + 1 + 3
5. 5 = 1 + 1 + 2

这里情况1可以看做$Q_1(5)$, 情况2和3可以看做$Q_2(5)$, 情况4和5可以看做$Q_3(5)$

也就是说

$$P_m(n) = Q_1(n)+ Q_2(n) + \cdots + Q_m(n)$$
那么, 我们有

$$P_{m-1}(n) = Q_1(n)+ Q_2(n) + \cdots + Q_{m-1}(n)$$

两式相减, 有

$$Q_m(n) = P_m(n) - P_{m-1}(n) \ (*)$$

**芜湖, 我们这里用2.1情况计算出了情况2.2 !!!**

更令人兴奋的是, 我们还可以导出$P_m(n)$由$Q_m(n)$表出的表达式!

回顾一下$P_m(n)$的递推方程: 

$$P_m(n) = P_{m-1}(n) + P_m(n-m) \ (n\geq m \geq 1) \ (1)$$
$$P_m(n) = P_{m-1}(n) \ (n<m \land m \geq 1) \ (2)$$
$$P_1(n) = 1 = P_m(0)\ (3)$$

我们把$(*)$式带入$(1)$, 有

$$Q_m(n) = P_m(n-m) \ (n \geq m \geq 1)$$
也就是

$$P_m(n) = Q_m(m+n) \ (n\geq 0, m\geq 1)$$

那么要是把$(*)$式带入$(2)$呢?

显然这时 $n < m$, $P_m(n) = 0$, 成为恒等式

**恭喜你! 你到这里用2.2情况计算出了情况2.1 !!!**

我们有这个式子

$$P_m(n) = Q_m(m+n)$$

注: **其实这个式子也可以直接由情况2.1向情况2.2变换得到, 请读者自己动手尝试一下

提示: 可以参考情况2.4的证明

### 2.3 小球相同,盒子不同,盒子可空

个人认为, 情况2.1和情况2.2是比较困难的情况, 下面我们的旅程将会轻松许多!

对于小球相同,盒子不同,盒子可空的计数, 

完全等价于

$$x_1 + x_2 + \cdots + x_m = n$$的**非负整数解**的个数

这时我们的计数公式为$C(n+m-1, n)$

(1) 组合角度证明:

考虑

$$\underbrace{1\cdots 1}_{x_1个1} \ 0 \ \underbrace{1\cdots 1}_{x_2个1} \ 0 \cdots 0 \ \underbrace{1\cdots 1}_{x_i个1} \ 0 \cdots \ 0 \  \underbrace{1\cdots 1}_{x_m个1}$$

一共有n个1, m-1个0, 相当于从n+m-1个数中选定n个数成为1

即$C(n+m-1, n)$

当然, 也可以从n+m-1个数中选定m-1个数成为0

即$C(n+m-1, m-1)$二者天然是相等的

(2) 生成函数说明

$$G(x)=(1+x+x^2+\cdots)^m$$

有

$$G(x) = \frac {1} {(1-x)^m} = (1-x)^{-m} = \Sigma_{n=0}^{\infty}(n+m-1,n)x^n$$

这里n,m都是整数,牛顿二项式系数退化为组合数$C(n+m-1,n)$

### 2.4 小球相同,盒子不同,盒子不空


对于小球相同,盒子不同,盒子不空的计数, 

完全等价于

$$x_1 + x_2 + \cdots + x_m = n$$的**正整数解**的个数$(x_i\geq 1)$

我们这里做一下变量替换, 令$y_i = x_i - 1 \geq 0$

则原方程

$$
(y_1+1)+(y_2+1)+\cdots +(y_m+1) = n
$$

即

$$
y_1+y_2+\cdots +y_m = n - m
$$

求**非负整数解**的个数

这样就转化到了情况2.3

计数为

$$C((n-m)+m-1, m-1) = C(n-1, m-1)$$

当然, 也可以写成

$$C(n-1, n-m)$$

### 2.5 小球不同,盒子相同,盒子可空

可以先看一眼情况2.6的解法(第二类Stirling数), 再回到这里:

可以按照非空盒个数k讨论, $0 < k <= m$

如果有k个非空盒, 也就是$n-k$个空盒, 相当于把n个不同小球放入k个相同盒子, 盒子不空,也就是$\{n,k\}$

总方法数为 $$\Sigma_{k=1}^{n} \{n,k\}$$


### 2.6 小球不同,盒子相同,盒子不空

这个问题直接对应第二类Stirling数: (更多性质和推导细节参考第二类Stirling数的推导)

$$\{n,m\} := n个不同元素放到m个相同盒子中的方法数(n>0,m>0)$$
或者这样来说, 好理解一点

$$\{n,m\} := n个元素分成m个组的方法数(n>0,m>0)$$

递推关系

$$\{n, r\} = r\{n-1, r\} + \{n-1 , r-1\}$$

证明:

在n-1个元素分组的基础上考虑:

1. 如果新增的第n个元素自成一组, 有$\{n-1, r-1\}$种方法
2. 如果新增的第n个元素加入到r个组中的某一组,有 $r\{n-1,r\}$种方法

一些特殊值

$$\{n, n\} = 1, \{n, n-1\} = (n,2), \{n,2\} = 2^{n-1}-1, \{n,1\}=1$$
### 2.7 小球不同,盒子不同, 盒子可空

每个小球都有m种选择盒子的方法, 最终结果

$$m^n$$

也可以由情况2.6和情况2.8推导得到:

考虑有k个非空盒子$0<k<m$

$$\Sigma_{k=1}^m(m,k)\{n,k\}k!$$

解释: 哪k个盒子非空 \* 小球不同盒子不同盒子不空(2.8)的方法数

这里是一个恒等式:

$$m^n = \Sigma_{k=1}^m(m,k)\{n,k\}k!$$

### 2.8 小球不同,盒子不同,盒子不空

可以由情况2.6推导得到:

只需要在小球不同,盒子相同,盒子不空的基础上, 对m个盒子进行全排列

$$m!\{n,m\}$$


至此,大功告成!

## 错位排列数

错位排列数（Derangement），也称为“错排问题”，是指在一个排列中，所有元素都不在它们原始位置上的排列数。错位排列数通常用$D_n$表示，其中$n$是排列的元素个数。

---

### **1. 错位排列数的定义**

假设有一个集合$\{1, 2, \dots, n\}$，我们需要找到一个排列$\sigma$，使得对于每个元素$i$，都有$\sigma(i) \neq i$。满足这种条件的排列数就是错位排列数$D_n$。

---

### **2. 错位排列数的递推公式**

错位排列数可以通过以下递推公式计算：
$$
D_n = (n - 1) \cdot (D_{n-1} + D_{n-2})
$$
其中：
-$D_0 = 1$（空集的错排数为 1）。
-$D_1 = 0$（只有一个元素时，无法错排）。
-$D_2 = 1$
-$D_3 = 2$
-$D_4 = 9$
-$D_5 = 44$
-$D_6 = 265$

---

### **3. 错位排列数的显式公式**

错位排列数也可以通过显式公式直接计算：
$$
D_n = n! \cdot \sum_{k=0}^n \frac{(-1)^k}{k!}
$$
这个公式来源于容斥原理，表示从所有排列中减去不符合条件的排列。

---