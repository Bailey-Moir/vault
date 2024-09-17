---
tags:
  - atom
  - math
  - discrete
---
Let $S(n)$ be a [[Statements and Propositions|statement]] involving a positive integer $n$, and $l$ be some integer greater than 1. If
- $S(1), S(2), \dots, S(l)$ are true
- if $S(1), S(2), \dots, S(k)$ are true, then $S(k+1)$ is true for all integers $k \ge l$,
then $S(n)$ holds for all $n \in \Z^+$.

The difference between this and [[Induction|normal induction]] is [[Induction|normal induction]] assumes $S(k)$ is true, whereas *strong induction* assumes $S(1), S(2), \dots, S(k)$. Note ***strong induction* is [[Logical Equivalence|logically equivalent]] to [[Induction|induction]]**.

$$ \forall S: \mathbb{Z^+} \to \B, \left( S(1) \land S(2) \land \dots \land S(l)\land \left( \forall k \in \Z^+, S(1) \land S(2) \land \dots \land S(k) \to S(k+1) \right) \implies \forall n \in \Z^+, S(n) \right) $$
More generally,
$$ \forall i \in \Z, S: \Z_{\ge i} \to \B, \left( S(i) \land \left( \forall k \in \Z_{\ge i}, S(1) \land S(2) \land \dots \land S(k) \to S(k+1) \right) \implies \forall n \in \Z_{\ge i}, S(n) \right) $$

> [!example]-
$$S(k) \iff \forall n \in \Z^+ \setminus \{1,3\}, \exists a,b \in \Z^+ : n = 2a + 5b$$
> **Base Cases**
> $$\begin{align*}
> S(2) &\iff 2 = 2\times1 + 5\times0 \\
> S(4) &\iff 4 = 2\times2 + 5\times0 \\
> S(5) &\iff 5 = 2\times0 + 5\times1 \\
> &\iff \T
> \end{align*}$$
> This proves the first [[Argument|premise]] of *strong induction* where $k = 5$.
> 
> **Induction Step**
> If $S(2), S(4), S(5), \dots, S(k)$ are true for some $k \in \Z^+ \setminus \{1,3\}$, $S(k+1)$ is true.
> $$ k+1 = k-1 + 2 $$
> Since $S(k-1)$ is true, $k - 1$ must be a [[Linear Combinations|linear combination]] of $2$s and $5$s, therefore $k+1$ must be a [[Linear Combinations|linear combination]] of $2$s and $5$s, meaning $S(k+1)$ is necessarily true. Thus $S(2) \land S(4) \land S(5) \land \dots \land S(k) \to S(k+1)$. The statement then follows by the principle of *strong mathematical induction*.
