# 组合数学

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