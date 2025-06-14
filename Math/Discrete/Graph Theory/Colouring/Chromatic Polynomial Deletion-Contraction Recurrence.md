---
tags:
  - atom
  - math
  - discrete
---
For all [[Graphs|graphs]] $G$ and $e \in E(G)$,
$$P(G,\lambda) = P(G\setminus e,\lambda) - P(G/e,\lambda)$$
> [!proof]-
> Let $e = \{ u,v \}$.
> 
> For each colouring of $G\setminus e$ where $u$ and $v$ are assigned **the same colour**, there is a corresponding colouring of $G/e$ that assigns the contracted vertex the same colour as $u$ and $v$ (and vice versa).
> 
> As this correspondence is a [[Bijective Functions|bijection]], $P(G/e,\lambda)$ is exactly the number of colourings of $G\setminus e$ using $\lambda$ colours in which $u$ and $v$ are assigned the same colour.
> 
> For each colour of $G\setminus e$ in which $u$ and $v$ are assigned **different colours**, there is a corresponding colouring of $G$ that assigns $u$ and $v$ different colours.
> 
> As this correspondence is a [[Bijective Functions|bijection]], $P(G,\lambda)$ is exactly the number of colourings of $G\setminus e$ using $\lambda$ colours in which $u$ and $v$ are assigned the difference colours.
> 
> Thus, $P(G/e,\lambda) + P(G,\lambda) = P(G\setminus e)$

\[[[Chromatic Polynomials]], [[Contraction & Deletion]]\]

> [!corollary]
> For all [[Graphs|graphs]] $G$ such that $\left| V(G) \right| = n$, $P(G,\lambda)$ is a [[Polynomials|polynomial]] in $\lambda$ with
> 1. leading term $\lambda^n$
> 2. integer coefficients, and
> 3. a zero constant coefficient.

> [!proof of corollary]-
> Let $G = \left( V,E \right)$ where $\left| V \right| = n$ and $\left| E \right| = m$.
> 
> **Edge Cases**
> If $G$ contains a loop, $P(G,\lambda) = 0$, and the corollary holds
> 
> **Base Case**
> If $m = 0$, $P(G,\lambda) = \lambda^n$, for which the corollary holds.
> 
> **Induction Step**
> Assume the corollary holds for all graphs with $m-1$ [[Edges|edges]].
> 
> Suppose that $G$ has $m$ edges, and let $e \in E$.
> 
> Then both $G\setminus e$ and $G/e$ have $m-1$ edges, meaning (by the induction hypothesis), there are integers $a_{1},a_{2},\dots,a_{n-1}$ and $b_{1},b_{2},\dots,b_{n-2}$ such that
> $$\begin{align}
> 	P(G\setminus e) &= \lambda^n +  \sum_{i = 1}^{n-1} a_{i}\lambda^i \\
> 	P(G/e) &= \lambda^{n-1} + \sum_{i = 1}^{n-2} b_{i}\lambda^i. \\
> \end{align}$$
> This gives
> $$\begin{align}
> 	P(G,\lambda) &= P(G\setminus e,\lambda) - P(G/e,\lambda) \\
> 	&= \lambda^n + \sum_{i = 1}^{n-1} a_{i}\lambda^i - \lambda^{n-1} - \sum_{i = 1}^{n-1} b_{i}\lambda^i \\
> 	&= \lambda^n - \lambda^{n-1} + a_{n-1}\lambda^{n-1} + \sum_{i = 1}^{n-2} a_{i}\lambda^i - \sum_{i = 1}^{n-2} b_{i}\lambda^i \\
> 	&= \lambda^n + \left( a_{n-1} - 1 \right)\lambda^{n-1} + \sum_{i = 1}^{n-2} \left(  a_{i} -  b_{i} \right)\lambda^i, \\
> \end{align}$$
> thus, the corollary holds.