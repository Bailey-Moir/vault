---
tags:
  - atom
  - comp
---
The types of grammars are defined by restricting the form of the productions $x \to y$, where $x \in \left( N\cup\Sigma \right)^+$ and $y \in \left( N\cup\Sigma \right)^*$.
- **Type-0 (General, [[Turing Machines|TM]]s)** - No Restrictions
- **Type-1 (Context-Sensitive, [[Linearly Space-Bounded Non-Detereministic TMs|LBA]]s)** - $\left| x \right| \le \left| y \right|$ but $S\to\varepsilon$ is allowed if $S$ is not produced.
- **Type-2 ([[Context-Free Grammars|Context-Free]])** - $x \in N$, **can** have epsilon productions.
- **Type-3 ([[Regular Grammar]])** - $x \in N$ and $y \in \Sigma N \cup \{ \varepsilon \}$

> [!note] For $i > j$, the type-$i$ **[[Languages|languages]]** are a [[Subsets|subset]] of the type-$j$ **[[Languages|languages]]**.

# Properties
- **Type-0**
	  - Accepted by [[Turing Machines|TM]]s.
- **Type-1** [[Languages|Languages]]
	- Closed under [[Complement|complement]].
	- [[Decidability|Decidable]].
	- Accepted by [[Linearly Space-Bounded Non-Detereministic TMs|LBA]]s.