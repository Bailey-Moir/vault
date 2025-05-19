---
tags:
  - atom
  - comp
---
A [[Context-Free Grammars|CFG]] $G = (N,\Sigma,P,S)$ is in *Chomsky normal form* iff every [[Context-Free Grammars|production]] has the form
- $A \to BC$, where $B,C \in N$, or
- $A \to a$, where $a \in \Sigma$.

> [!algorithm]- Each [[Context-Free Grammars|CFG]] where $\varepsilon$[^1] is not [[Derivability|derivable]] can be given in *Chomsky normal form*.
> 1. While possible, if $A \to uBv \in P$ for $u,v \in (\Sigma \cup N)^*$ and $B \to \varepsilon \in P$, add $A \to uv$ to $P$.
> 2. Remove all $\varepsilon$-productions of the form $A \to \varepsilon$.
> 3. While possible, if $A \to B \in P$ and $B \to w \in P$ for $w \in (\Sigma \cup N)^*$, add $A \to w$ to $P$.
> 4. Remove all unit-productions of the form $A \to B$.
> 5. Remove all [[Context-Free Grammars|non-generating]] non-terminals, along with all productions containing them.
> 6. Remove all [[Context-Free Grammars|non-reachable]] non-terminals, along with all productions containing them.
> 7. Whenever a terminal $a$ appears in a $\text{RHS}$ of length at least $2$, replace it with a non-terminal $A$, with $A \to a \in P$.
> 8. While possible, split productions of the form $A \to B_{1}B_{2}\dots B_{n}$ where $B_{1},\dots,B_{n} \in N$ into $A \to B_{1}C$ and $C \to B_{2}\dots B_{n}$.
> > [!note] If $\varepsilon$ is needed,
> > - Add a new non-terminal $S'$ and the production $S'\to\varepsilon$.
> > - For each $S \to w$ of the start symbol, add $S' \to w$.
> > - Make $S'$ the new start symbol.

> [!note] Everything is [[Context-Free Grammars|generating]] and [[Context-Free Grammars|reachable]].

[^1]: [[Empty String]]
