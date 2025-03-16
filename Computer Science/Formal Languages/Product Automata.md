---
tags:
  - atom
  - comp
---
For two [[Deterministic Finite Automata|DFA]]s or [[Non-Deterministic Finite Automata|NFA]]s $M_{1}$ and $M_{2}$ where
$$\begin{align}
	M_{1} &= \left( Q_{1},\Sigma,\delta_{1},q_{1},F_{1} \right) \\
	M_{2} &= \left( Q_{2},\Sigma,\delta_{2},q_{2},F_{2} \right),
\end{align}$$
a *product automaton* of $M_{1}$ and $M_{2}$ is an automaton of the form
$$M = \left( Q_{1}\times Q_{2},\Sigma,\delta,(q_{1},q_{2}),F_{1} \times F_{2} \right)$$