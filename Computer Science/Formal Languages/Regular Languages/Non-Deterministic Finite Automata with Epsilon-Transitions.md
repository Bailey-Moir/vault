---
tags:
  - atom
  - comp
---
A *non-deterministic finite automaton with $\mathit{\varepsilon}$-transitions* is a structure $M = \left( Q,\Sigma,\delta,q_{0},F \right)$ defined the same as an [[Non-Deterministic Finite Automata|NFA]], except
- the [[Domain|domain]] of $\delta$ is $Q\times(\Sigma \cup \{ \varepsilon \})$ instead of $Q\times\Sigma$.

$M$ may move from $q$ to any state in $\delta(q,\varepsilon)$ without consuming a symbol from the input.

> [!note] $\varepsilon$-closure
> $$\begin{align*}
> 	E(q) &= \{ p \in Q : p \text{ is reachable from } q \text{ with a sequence of } \varepsilon\text{-transitions} \} \\
> 	 &= \hat{\delta}(q,\varepsilon)
> \end{align*}$$
> \[[[Extended Transition Function]]\]

\[[[Empty String]]\]