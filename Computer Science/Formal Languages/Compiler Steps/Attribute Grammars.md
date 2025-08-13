---
tags:
  - atom
  - comp
---
[[Type Systems|Type systems]] are implemented with *attribute [[Context-Free Grammars|grammars]]*, which are [[Context-Free Grammars|CFGs]] extended with *attributes* and rules.

> [!example]- Simple system for numbers
> **(Synthetic) Attributes**
>  - $\text{type} \in \{ \text{int},\text{float} \}$ with $E$, $T$, $F$, $\text{num}$, $\text{id}$.
> - $\text{op} \in \{ +,-,\times,/ \}$ with $A$, $M$
>  $$\text{typeof}(\text{op},t_{1},t_{2}) \left\{\begin{array}{ll}
> 	\text{int} &\text{if op} \in \{ +,-,* \} \text{ and } t_{1} = t_{2} = \text{int} \\
> 	\text{float} &\text{otherwise}
> \end{array}\right.$$
> ---
> $$\begin{array}{lll}
> 	E = T &\hspace{1em}& E\text{.type} = T\text{.type} \\
> 	E = EAT && E_{0}\text{.type} = \text{typeof}(A,E_{1}\text{.type},T\text{.type}) \\
> 	A = + && A\text{.op} = + \\
> 	A = - && A\text{.op} = - \\
> 	T = F && T\text{.type} = F\text{.type} \\
> 	T = TMF && T_{0}\text{.type} = \text{typeof}(M,T_{1}\text{.type},F\text{.type}) \\
> 	M = * && M\text{.op} = * \\
> 	M = / && M\text{.op} = / \\
> 	F = (E) && F\text{.type} = E\text{.type} \\
> 	F = \text{num} && F\text{.type} = \text{num}\text{.type} \\
> 	F = \text{id} && F\text{.type} = \text{id}\text{.type} \\
> \end{array}$$

> [!definition]- **Synthetic** *attributes* are propagated bottom-up, where the value on the $\text{LHS}$ depends on the value of the $\text{RHS}$

> [!definition]- **Inherited** *attributes* are propagated top-down, where the value on the $\text{RHS}$ depends on the value of the $\text{LHS}$