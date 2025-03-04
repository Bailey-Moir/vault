---
tags:
  - atom
  - comp
---
A *deterministic finite automaton* (DFA) is a labelled [[Directed Graphs|directed]] [[Graphs|graph]]; a structure $M = \left( Q,\Sigma,\delta,q_{0},F \right)$ where
- $Q$, the **states**, is a non-[[Empty Set|empt]] finite [[Sets|set]],
- $\Sigma$ is the input [[Alphabets|alphabet]],
- $\delta : Q\times\Sigma \to Q$ is the **transition function** (the [[Edges|edges]]),
- $q_{0}\in Q$ is the **start state**,
- $F\subseteq Q$ is the set of **accept/final states**.

$M$ process an input [[Strings|string]] symbol-by-symbol, starting at state $q_{0}$. If it is in state $q$ and the next symbol is $a$, then $M$ moves to $\delta(q,a)$. The [[Strings|string]] is accepted iff the final state is in $F$.

> [!example]- ![1000|center](deterministic-finite-automata.excalidraw)
> The above **transition diagram** can be represented as
> $$\left( \{ q_{0},q_{1},q_{2} \},\{ a,b \},\delta,q_{0},\{ q_{2} \} \right)$$
> where
> $$\begin{align*}
> 	\delta(q_{0},a) &= q_{1} \\
> 	\delta(q_{0},b) &= \delta(q_{1},b) = q_{0} \\
> 	\delta(q_{1},a) &= \delta(q_{2},a) = \delta(q_{2},b)  = q_{2}, \\
> \end{align*}$$
> or with a **transition table**, as seen below.
> 
> |  $\delta$ | $a$     | $b$     |
> | ---------- | ------- | ------- |
> | $q_{0}$    | $q_{1}$ | $q_{0}$ |
> | $q_{1}$    | $q_{2}$ | $q_{0}$ |
> | $q_{2}$    | $q_{2}$ | $q_{2}$ |
