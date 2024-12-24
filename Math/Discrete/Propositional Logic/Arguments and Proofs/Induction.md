---
tags:
  - atom
  - math
  - discrete
---
Let $S(n)$ be a [[Statements and Propositions|statement]] involving a positive integer $n$. If
- $S(1)$ is true (note the base case does not have to be $1$)
- if $S(k)$ is true, then $S(k+1)$ is true for all positive integers $k$,
then $S(n)$ holds for all $n \in \Z^+$.

$$ \forall S: \mathbb{Z^+} \to \B, \left( S(1) \land \left( \forall k \in \Z^+, S(k) \to S(k+1) \right) \implies \forall n \in \Z^+, S(n) \right) $$
More generally,
$$ \forall i \in \Z, S: \Z_{\ge i} \to \B, \left( S(i) \land \left( \forall k \in \Z_{\ge i}, S(k) \to S(k+1) \right) \implies \forall n \in \Z_{\ge i}, S(n) \right) $$

>[!proof]-
> Suppose $S(n)$ is not true for some $n \in \Z_{\ge i}$.
> 
> Then there is a [[Empty Set|non-empty]] [[Subsets|subset]] $A$ of $\Z_{\ge i}$ for which $S(n)$ is false. Let $m$ be the smallest integer of $A$. From the first [[Argument|premise]] ($S(1)$), $m \ne i$, so $m > i$.
> 
> Let $k = m-1$. By the minimality of $m$, $S(k)$ holds. Therefore, by the second [[Argument|premise]] ($S(k)\to S(k+1)$), $S(k+1)$ holds. But $k+1 = m$, so $S(m)$ holds; a [[Contradictions|contradiction]].
> 
> Thus, $\neg \exists n \in \Z_{\ge i} : \neg S(n)$;  $\forall n \in \Z_{\ge i} : S(n)$
> 
> \[[[Proof by Contradiction]]\]

> [!example]-
$$S(k) \iff 1 + 2 + \dots + k = \dfrac{k(k+1)}{2}$$
> **Base Case**
> $$\begin{align*}
> S(1) &\iff 1 = \dfrac{1 \times 2}{2} \\
> &\iff \T
> \end{align*}$$
> This proves the first [[Argument|premise]] of *induction*
> 
> **Induction Step**
> if $S(k)$ is true for some $k \in \Z^+$,
> $$ 1 + 2 + \dots + k = \dfrac{k(k+1)}{2} $$
> it then follows that
> $$\begin{align*}
> 	1 + 2 + \dots + k + (k+1) &= \dfrac{k(k+1)}{2} + (k+1) && \text{Using Induction Hypothesis}\\
> 	&= (k+1)\left( \dfrac{k}{2} + 1 \right) \\
> 	&= \dfrac{(k+1)( k + 2)}{2} \\
> 	1 + 2 + \dots + m &= \dfrac{m(m + 1)}{2} && \ni m=k+1\\
> \end{align*}$$
> Thus $S(k) \to S(k+1)$. The statement then follows by the principle of mathematical *induction*.