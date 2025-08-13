---
tags:
  - atom
  - math
---
![1000|center](bounding.excalidraw.md)
A [[Sequences|sequence]] $\left( a_{n} \right)$ is *bounded* iff $\{ a_{n} : n \in \N \}$ is a [[Bounded Sets|bounded set]] in $\R$.

> [!theorem]- **2.8** If $\left( a_{n} \right)$ is [[Convergence of Sequences|convergent]], then it is *bounded*
> Since $\left( a_{n} \right)$ is [[Convergence of Sequences|convergent]], $\forall \varepsilon > 0, \exists N : \forall n \ge N, \left| a_{n} - L \right| < \varepsilon$.
> 
> Thus, for $\varepsilon > 0$, there is an $N$ such that $\left| a_{n} - L \right| < \varepsilon$ for all $n \ge N$.
> 
> Thus, for $n \ge N$, $L - \varepsilon\le a_{n} \le L + \varepsilon$, meaning $\left( a_{n} \right)$ is *bounded* for $n \ge N$.
> 
> If $K = \max \{  \left| a_{1} \right|,\dots,\left| a_{N-1} \right| \}$ (which must exist as the [[Sets|set]] is finite), then $-K \le a_{n} \le K$, meaning $\left( a_{n} \right)$ is *bounded* for $n < N$.
> 
> Thus, $\left( a_{n} \right)$ is *bounded* for all $n \in \N$.