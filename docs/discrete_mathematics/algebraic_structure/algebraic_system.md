<!--
 * @Author: chinesehamburger 2576226012@qq.com
 * @Date: 2025-03-21 09:59:29
 * @LastEditors: chinesehamburger 2576226012@qq.com
 * @LastEditTime: 2025-04-02 15:45:58
 * @FilePath: \CHMath-wiki\docs\discrete_mathematics\algebraic_structure\algebraic_system.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
# 代数系统

## 代数的理解

- 同态映射是这样一种特殊的映射, 保持了对应元素的运算

`A`上二元运算

## A上的n元运算

### 定义

设A为集合，函数 $f: A \times A \rightarrow A$ 称为A上的二元运算。

设A为集合，函数 $f: A^n \rightarrow A$ 称为A上的n元运算。

- 当 $n = 0$，0元运算，$f: \rightarrow A$，A中的一个元素。
- 当 $n = 1$，一元运算，$f: A \rightarrow A$
- $a = (1, 3, 4, 3, 4)$

### n元运算的封闭性

根据n元运算的定义, 运算结果均属于A

### 例子

#### 解析表达式
- `○`是实数集 $\mathbb{R}$ 上的二元运算
  $$
  x \circ y = x + y - 2xy
  $$

#### 运算表
- $A = P(\{a, b\})$，$A$上的二元运算$\oplus$，一元运算$\sim$

#### 二元运算表$\oplus$

| $\oplus$    | $\varnothing$ | $\{a\}$     | $\{b\}$     | $\{a,b\}$   |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| $\varnothing$ | $\varnothing$ | $\{a\}$     | $\{b\}$     | $\{a,b\}$   |
| $\{a\}$     | $\{a\}$     | $\varnothing$ | $\{a,b\}$   | $\{b\}$     |
| $\{b\}$     | $\{b\}$     | $\{a,b\}$   | $\varnothing$ | $\{a\}$     |
| $\{a,b\}$   | $\{a,b\}$   | $\{b\}$     | $\{a\}$     | $\varnothing$ |

#### 一元运算表$\sim$
| $X$         | $\sim X$    |
| ----------- | ----------- |
| $\varnothing$ | $\{a,b\}$   |
| $\{a\}$     | $\{b\}$     |


| $\{b\}$     | $\{a\}$     |
| $\{a,b\}$   | $\varnothing$ |

## 二元运算的运算律

| | 运算律 |
| - | - |
| 交换律 | $\forall a,b \in A, a \circ b = b \circ a$ |
| 结合律 | $\forall a,b,c \in A, (a \circ b) \circ c = a \circ (b \circ c)$ |
| 幂等律 | $\forall a \in A, a \circ a = a$ |
| 左分配律 | $\forall a,b,c \in A, a \circ (b * c) = (a \circ b) * (a \circ c)$ |
| 右分配律 | $\forall a,b,c \in A, (b * c) \circ a = (b \circ a) * (c \circ a)$ |
| 吸收律 | 设$\circ$,$*$可交换, $\forall a,b \in A, a \circ (a * b) = a, a * (a \circ b) = a, a * (a \circ b) = a$ |

