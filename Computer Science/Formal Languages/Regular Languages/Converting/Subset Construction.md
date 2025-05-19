---
tags:
  - atom
  - comp
---
For all [[Non-Deterministic Finite Automata|NFA]]s $M = (Q,\Sigma,\delta,q_{0},F)$, let the *subset automaton* [[Deterministic Finite Automata|DFA]] $M' = (\mathcal{P}(Q),\Sigma,\delta',\{ q_{0} \},F')$ where:
$$\begin{array}{rc}
	&F' = \{ S \subseteq Q : S \cap F \ne \emptyset \} \\
	&\delta'(S,a) = \bigcup_{q\in S} \delta(q,a) \\
\implies & \hat{\delta'}(S,w) = \bigcup_{q\in S} \hat{\delta}(q,w).
\end{array}$$
Then
$$\begin{align}
	w \in L(M') &\iff \hat{\delta'}(\{ q_{0}\}, w ) \in F' && (1)\\
	&\iff \hat{\delta'}(\{ q_{0}\}, w ) \cap F \ne \emptyset \\
	&\iff \left( \bigcup_{q \in \{ q_{0} \}} \hat{\delta}(q, w ) \right) \cap F \ne \emptyset\\
	&\iff \hat{\delta}(q_{0}, w ) \cap F \ne \emptyset\\
	&\iff w \in L(M) && (1)\\
\end{align}$$
\[$(1)$ [[Languages of Finite Automata]]\]