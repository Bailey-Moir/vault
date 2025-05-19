---
tags:
  - atom
  - comp
---
For a [[Deterministic Finite Automata|DFA]] or [[Non-Deterministic Finite Automata|NFA]] $M$ and an [[Equivalence Relations|equivalence relation]] $\rel$ (e.g. $\sim$[^1]) where
$$\begin{align}
	M &= \left( Q,\Sigma,\delta,q_{0},F \right) \\
\end{align}$$
a *quotient automaton* of $M$ by $\sim$ is an automaton of the form
$$M' = \left( Q/\hspace{-0.3em}\sim,\Sigma,\delta',\left[ q_{0} \right], F' \right)$$

[^1]: [[Equivalence of States]]
