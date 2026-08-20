
## Set-Theoretic vs. Category-Theoretic Views of Functions


**1. Set-Theoretic Definition**
- In set theory (e.g., ZFC), a function $f: A \to B$ is defined as a **set of ordered pairs** (its graph) $f \subseteq A \times B$ satisfying:
  - **Totality**: $\forall a \in A, \exists b \in B$ such that $(a, b) \in f$
  - **Functionality**: If $(a, b) \in f$ and $(a, b') \in f$, then $b = b'$
- The **range** is $\operatorname{im}(f) = \{ b \in B \mid \exists a \in A, (a,b) \in f \}$
- **Key consequence**: Two functions are **equal** if they have identical graphs, regardless of codomain.  
  - Example: Identity $\operatorname{id}_{\mathbb{N}}: \mathbb{N} \to \mathbb{N}$ and inclusion $\iota: \mathbb{N} \to \mathbb{Z}$ both have graph $\{(n, n) \mid n \in \mathbb{N}\}$.  
  - In set theory, $\operatorname{id}_{\mathbb{N}} = \iota$.

**2. Category-Theoretic Definition in Set**
- In $\mathbf{Set}$, an arrow $f: A \to B$ is a total function where **codomain $B$ is part of the arrow's identity**.
- **Critical distinction**: Arrows with identical graphs but different codomains are **distinct**.  
  - Example: $\operatorname{id}_{\mathbb{N}}: \mathbb{N} \to \mathbb{N}$ and $\iota: \mathbb{N} \to \mathbb{Z}$ are different arrows in $\mathbf{Set}$.

**3. Why Codomain Matters in Category Theory**
- **Composition**: Arrows compose only if codomain of first matches domain of second.  
  - For $g: \mathbb{Z} \to \mathbb{Z}, g(x) = x + 1$:  
    - Composition $\iota ; g: \mathbb{N} \to \mathbb{Z}$ is valid  
    - Composition $\operatorname{id}_{\mathbb{N}} ; g$ is **invalid** ($\operatorname{codomain}(\operatorname{id}_{\mathbb{N}}) = \mathbb{N} \neq \mathbb{Z}$)
- **Structural Roles**: Codomain specifies "where outputs live" in the universe of sets.
- **Categorical Constructs**: Properties like surjectivity depend on specified codomain. A morphism $f: A \to B$ is epic in $\mathbf{Set}$ iff surjective **into $B$**.

**Key Insight**  

> In $\mathbf{Set}$, an arrow $f: A \to B$ encodes **both the mapping rule (graph) and contextual information** (domain $A$, codomain $B$). The codomain is not derivable from the graph and is intrinsic to the arrow's identity.
## 怎么证明在Set中, 一个morphism是满的等价于是满射

**问题**  
证明集合范畴 $\mathbf{Set}$ 中，一个态射是满态射（右可约）当且仅当它是满射。

**证明**  

**定义回顾**  
1.  **满射 (Surjective)**：  
    函数 $f: A \to B$ 是满射，当且仅当 $\forall b \in B$， $\exists a \in A$ 满足 $f(a) = b$， 即像集 $f(A) = B$。  
2.  **满态射 (Epimorphism)**：  
    在范畴 $\mathbf{Set}$ 中， $f: A \to B$ 是满态射， 当且仅当它满足右可约性： 对任意集合 $C$ 和任意函数 $g, h: B \to C$， 若 $g \circ f = h \circ f$， 则 $g = h$。

---

**步骤 1： 若 $f$ 是满射， 则 $f$ 是满态射**  
- **假设**： $f: A \to B$ 是满射。  
- **目标**： 证明对任意 $C$ 和 $g, h: B \to C$， 若 $g \circ f = h \circ f$， 则 $g = h$。  
- **证明**：  
  设 $g \circ f = h \circ f$。 需证 $g(b) = h(b)$ 对所有 $b \in B$ 成立。  
  取任意 $b \in B$。 由满射性， 存在 $a \in A$ 使得 $f(a) = b$。  
  由 $g \circ f = h \circ f$， 有 $(g \circ f)(a) = (h \circ f)(a)$， 即 $g(f(a)) = h(f(a))$。  
  代入 $f(a) = b$ 得 $g(b) = h(b)$。 故 $g = h$， 即 $f$ 是满态射。

**步骤 2： 若 $f$ 是满态射， 则 $f$ 是满射**  
- **假设**： $f$ 是满态射（即右可约）。  
- **目标**： 证明 $f$ 是满射（反证法）。  
- **证明**：  
  假设 $f$ 不满射， 即存在 $b_0 \in B$ 满足 $\forall a \in A$， $f(a) \neq b_0$。  
  取 $C = \{0, 1\}$， 并定义：  
  $$ 
  g(b) = 0 \quad (\forall b \in B), \quad h(b) = 
  \begin{cases} 
  0 & \text{if } b \neq b_0 \\ 
  1 & \text{if } b = b_0 
  \end{cases}
  $$  
  **验证**：  
  - $g \circ f = h \circ f$：  
    对任意 $a \in A$， 有 $f(a) \neq b_0$， 故 $h(f(a)) = 0$。 而 $g(f(a)) = 0$， 因此 $(g \circ f)(a) = (h \circ f)(a) = 0$。  
  - 但 $g \neq h$：  
    因 $g(b_0) = 0$ 而 $h(b_0) = 1$。  
  这与 $f$ 是满态射矛盾！ 故假设错误， $f$ 必为满射。

**结论**  
在 $\mathbf{Set}$ 中：  
$$ 
\boxed{f \text{ 是满态射} \quad \iff \quad f \text{ 是满射}}
$$