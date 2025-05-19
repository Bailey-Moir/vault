---
tags:
  - atom
  - comp
---
The fourth-step of [[Compilers|compiling]] is *machine-independent optimisation*. Optimisation takes place on the [[Syntax Diagrams|syntax tree]] (or another intermediate form).

> [!examples]- Constant propagation, constant folding, dead code elimination.
> ```
> x = 11
> y = 4
> z = 8*x
> z = x*y
> z = z * 2 + x
> if z > 99:
> 	z = 0
> else:
> 	z = 1
> ```
> becomes
> ```
> z = 1
> ```

> [!example]- Constant folding [[Attribute Grammars|attribute grammar]]
> **Attributes**
> - $\text{value} \in \R \cup \{ ? \}$ with $E$, $T$, $F$, $\text{num}$, $id$
> $$\text{valueof}(\text{op},x_{1},x_{2}) = \left\{\begin{array}{lcl}
> 	x_{1} + x_{2} &&\text{op} = + \\
> 	x_{1} * x_{2} &&\text{op} = * \\
> 	x_{1} / x_{2} &&\text{op} = / \\
> 	\vdots && \vdots \\
> \end{array}\right.$$
> ---
> $$\begin{array}{lll}
> 	E = T &\hspace{1em}& E\text{.value} = T\text{.value} \\
> 	E = EAT && E_{0}\text{.value} = \text{valueof}(A\text{.op},E_{1}\text{.value},T\text{.value}) \\
> 	T = F && T\text{.value} = F\text{.value} \\
> 	T = TMF && T_{0}\text{.value} = \text{typeof}(M\text{.op},T_{1}\text{.value},F\text{.value}) \\
> 	F = (E) && F\text{.value} = E\text{.value} \\
> 	F = \text{num} && F\text{.value} = \text{num}\text{.value} \\
> 	F = \text{id} && F\text{.value} = \text{id}\text{.value} \\
> \end{array}$$