---
tags:
  - atom
  - comp
---
$A \subseteq \Sigma^*$ is *regular* iff there exists a [[Deterministic Finite Automata|DFA]] $M$ such that $A = L(M)$[^1].
#TODO exam jumpscare

> [!note]- Every [[Languages of Finite Automata|language accepted by]] an [[Non-Deterministic Finite Automata|NFA]] is accepted by a [[Deterministic Finite Automata|DFA]] (and vice versa)
> Thus,  $A \subseteq \Sigma^*$ is *regular* iff there exists a [[Deterministic Finite Automata|DFA]] or [[Non-Deterministic Finite Automata|NFA]] $M$ such that $A = L(M)$[^1].
# Closure
*Regular languages* are *closed* under
> [!proof]- [[Complement|Complement]]
> Given a *regular language* $A = L(M)$ where $M = \left( Q,\Sigma,\delta,q_{0},F \right)$, let $M' = \left( Q,\Sigma,\delta,q_{0},Q-F \right)$.
> $$\begin{align}
> 	w \in L(M') &\iff \hat{\delta}(q_{0},w) \in Q - F \\
> 	&\iff \hat{\delta}(q_{0},w) \notin F \\
> 	&\iff w \notin L(M) \\
> 	&\iff w \notin A \\
> 	&\iff w \in A^c \\
> \end{align}$$

> [!proof]- [[Unions and Intersections|Intersection]]
> Given *regular languages* $A = L(M_{1})$ and $B = L(M_{2})$ where $M_{1} = \left( Q_{1},\Sigma,\delta_{1},q_{1},F_{1} \right)$ and $M_{2} = \left( Q_{2},\Sigma,\delta_{2},q_{2},F_{2} \right)$, let $M = \left( Q_{1}\times Q_{2},\Sigma,\delta,(q_{1},q_{2}),F_{1} \times F_{2} \right)$ (called the **product automaton**) where $\delta$ is defined by
> $$\delta((p_{1},p_{2}),a) = (\delta_{1}(p_{1},a), \delta_{2}(p_{2},a)) \hspace{2em} a \in \Sigma$$
> meaning
> $$\hat{\delta}((p_{1},p_{2}),w) = (\hat{\delta_{1}}(p_{1},a), \hat{\delta_{2}}(p_{2},w))\hspace{2em} w \in \Sigma^*$$[^1]
which can be proven [[Inductors|inductively]] using the definition of the [[Extended Transition Function|extended transition function]].
> $$\begin{align}
> 	w \in L(M) &\iff \hat{\delta}((q_{1},q_{2}),w) \in F_{1}\times F_{2} \\
> 	&\iff (\hat{\delta_{1}}(q_{1},w), \hat{\delta_{2}}(q_{2},w)) \in F_{1}\times F_{2} \\
> 	&\iff \hat{\delta_{1}}(q_{1},w) \in F_{1} \land \hat{\delta_{2}}(q_{2},w)F_{2} \\
> 	&\iff w \in L(M_{1}) \land w \in L(M_{2}) \\
> 	&\iff w \in L(M_{1}) \cap L(M_{2}) \\
> \end{align}$$
> \[[[Cartesian Product]], [[Unions and Intersections]]\]

> [!proof]- [[Unions and Intersections|Union]] 
> Given two *regular languages* $A$ and $B$,
> $$\begin{align}
> 	A \cup B &= \{ x : x \in A \lor x \in B \} && (1)\\
> 	&= \{ x : \neg(x \notin A \land x \notin B) \} && (2) \\
> 	&= \{ x : \neg(x \in A^c \land x \in B^c) \} && (3) \\
> 	&= \{ x : \neg(x \in A^c \cap B^c) \} && (1) \\
> 	&= (A^c \cap B^c)^c && (3) \\
> \end{align}$$
> \[$1$ [[Unions and Intersections]], $(2)$ [[De Morgan's Laws]], $(3)$, [[Complement]]\]
> 
> As proven above, *regular languages* are *closed* under [[Complement|complement]] and [[Unions and Intersections|intersection]], meaning they must also be *closed* under [[Unions and Intersections|union]].

- [[Concatenation of Languages and Alphabets|concatenation and star]],

[^1]: [[Languages of Finite Automata]]
