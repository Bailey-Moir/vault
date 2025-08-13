---
tags:
  - atom
  - math
---
[[Linear Homogeneous Differential Equations|Linear homogeneous DEs]] of the form $\vecbf{x}'=A(t)\vecbf{x}$ are solved by
$$\vecbf{x}(t) = \Phi(t)\Phi(t_{0})^{-1}\vecbf{x}_{0} \hspace{2em} \text{s.t. } \vecbf{x}(t_{0}) = \vecbf{x}_{0}$$
where $\Phi(t)$ is a [[Fundamental Matrices|fundamental matrix]] of the [[Linear Systems|sytem]].

> [!proof]-
> The [[Matrices|matrix]] $\Phi(t)$ is a [[Bijective Functions|bijective map]] from $\R^m$ to the solution [[Vector Spaces|space]] of $\vecbf{x}' = A(t)\vecbf{x}$ (by the definition of [[Fundamental Matrices|fundamental matrices]]).
> 
> Thus, the solution we are looking for (something in the [[Column Space|column space]] of $\Phi(t)$) is given by
> $$ \vecbf{x}(t) = \Phi(t)\vecbf{c}$$
> for some unique $\vecbf{c} \in \R^m$.
> 
> Since this solution must satisfy the [[Initial Value Problem|initial data]] $\vecbf{x}(t_{0}) = \vecbf{x}_{0}$,
> $$\begin{align}
> 	\vecbf{x}(t_{0}) = \Phi(t_{0})\vecbf{c} &= \vecbf{x}_{0} \\
> 	\vecbf{c} &= \Phi(t_{0})^{-1}\vecbf{x}_{0}, \\
> \end{align}$$
> where $\Phi(t_{0})$ is [[Matrix Invertibility|invertible]] as $\Phi(t)$ [[Matrix Invertibility|invertible]] for all $t$.
> 
> Thus, the solution to the [[Initial Value Problem|IVP]] is given by
> $$\vecbf{x}(t) = \Phi(t)\Phi(t_{0})^{-1}\vecbf{x}_{0}$$

