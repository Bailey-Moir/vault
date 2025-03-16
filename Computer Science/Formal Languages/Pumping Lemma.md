---
tags:
  - atom
  - comp
---
For all [[Regular Languages|regular language]] $A$, there exists $n \in \N$ such that all $w \in A$ with $\left| w \right| \ge n$ can be broken into three parts, $w = xyz$, where
- $y \ne \varepsilon$[^1]
- $\left| xy \right| \le n$, and
- $\forall i \in \N, xy^iz \in A$

> [!example]- $A = \{ a^nb^n : n \in \N \}$
> Assume $A$ is [[Regular Languages|regular]].
> 
> Let $n \in \N$, and $w = a^nb^n$.
> 
> Let $x,y,z$ be defined such that $w = xyz$, $y \ne \varepsilon$[^1], and $\left| xy \right| \le n$.
> 
> Since $w$ starts with $a^n$, and $\left| xy \right| \le n$, $x$ and $y$ must consist only of $a$'s.
> 
> Let and $y = a^j$.
> 
> Then $xy^2z \in A$ by *the pumping lemma*, but
> $$xy^2z = xyyz = a^{n+j}b^n \notin A$$

> [!note] You give $A$, $w$, and $i$

> [!note] Formal Statement
> $$\begin{align*}
> 	 \forall A \in \Sigma^* : A \text{ regular} \implies& \\
> 	 &\hspace{-9em}\exists n \in \N : \forall w \in A : \left| w \right| \ge n, \to \\
> 	 &\hspace{-7em}\exists x,y,z \in \Sigma^* : w = xyz \land y \ne \varepsilon \land \left| xy \right| \le n  \land \forall i \in \N : xy^iz \in A
> \end{align*}$$


[^1]: [[Empty String]]
