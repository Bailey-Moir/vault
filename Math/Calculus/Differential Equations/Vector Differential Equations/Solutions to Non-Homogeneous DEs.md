---
tags:
  - atom
  - math
---
[[Linear Homogeneous Differential Equations|Linear homogeneous DEs]] of the form $\vecbf{x}'=A(t)\vecbf{x} + \vecbf{b}$ are solved by
$$\vecbf{x}(t) = \Phi(t)\left( \Phi(t_{0})^{-1}\vecbf{x}_{0} + \int_{t_{0}}^t \Phi(s)^{-1}\vecbf{b}\,ds \right) \hspace{2em} \text{s.t. } \vecbf{x}(t_{0}) = \vecbf{x}_{0}$$
where $\Phi(t)$ is a [[Fundamental Matrices|fundamental matrix]] of the [[Linear Systems|system]].

> [!proof]-
> Suppose $\Phi(t)\vecbf{u}'(t) = \vecbf{b}(t)$, meaning that $\vecbf{x}(t) = \Phi(t)\vecbf{u}(t)$ solves $\vecbf{x}'(t) = A(t)\vecbf{x}(t)+b(t)$, as
> $$\begin{align}
> 	\left[ \Phi(t)\vecbf{u}(t) \right]'
> 	&= \Phi'(t)\vecbf{u}(t) + \Phi(t)\vecbf{u}'(t) \\
> 	&= \left[ A(t)\Phi(t) \right]\vecbf{u}(t) + \left[ \vecbf{b}(t) \right] \\
> 	&= A(t)\left[ \Phi(t)\vecbf{u}(t) \right]  + \vecbf{b}(t). \\
> \end{align}$$
> To find $\vecbf{u}$,
> $$\begin{align}
> 	\Phi(t)\vecbf{u}'(t) &= \vecbf{b}(t) \\
> 	\vecbf{u}'(t) &= \Phi(t)^{-1}\vecbf{b}(t) \\
> 	\vecbf{u}(t) &= \int^t_{c}\Phi(s)^{-1}\vecbf{b}(s) \,ds \\
> 	&= \vecbf{c} + \int^t_{t_{0}}\Phi(s)^{-1}\vecbf{b}(s) \,ds, \\
> \end{align}$$
> where the lower bound of integration is chosen to be $t_{0}$ so that
> $$\begin{align}
> 	\vecbf{u}(t_{0}) &= \vecbf{c} \\
> 	\to \vecbf{x}(t_{0}) = \Phi(t_{0})\vecbf{u}(t_{0}) &= \Phi(t_{0})\vecbf{c}. \\
> \end{align}$$
> 
> Since $\vecbf{x}(t_{0}) = \vecbf{x}_{0}$, this gives $\vecbf{c} = \Phi(t_{0})^{-1}\vecbf{x_{0}}$. Thus, 
> $$\vecbf{x}(t) = \Phi(t)\left( \Phi(t_{0})^{-1}\vecbf{x}_{0} + \int_{t_{0}}^t \Phi(s)^{-1}\vecbf{b}\,ds \right).$$

> [!intuition]- from [[Variation of Parameters|Variation of Parameters]]
> [[Variation of Parameters|Variation of parameters]] gives a solution of the form
> $$u_{1}(t)y_{1}(t) + \dots + u_{m}(t)y_{m}(t) = \Phi(t)\vecbf{u}(t),$$\[[[Variation of Parameters]]\]
> where
> $$\begin{array}{c}
> 	\begin{align}
> 		u_{1}'y_{1} + \dots + u_{m}'y_{m} &= 0 \\
> 		u_{1}'y_{1}' + \dots + +u_{m}'y_{m}' &= \dfrac{f(t)}{a_{m}(t)}\\
> 	\end{align} \\
> 	\large\Updownarrow \\
> 	\Phi(t)\vecbf{u}' = \vecbf{b},
> \end{array}$$
> as $a_{m}(t) = 1$.
> 
> Thus,
> $$\vecbf{u}(t) = \int^t_{t_{0}} \Phi(s)^{-1}\vecbf{b}\,ds + \vecbf{c},$$
> where the lower bound of integration is chosen to be $t_{0}$ so that
> $$\begin{align}
> 	\vecbf{u}(t_{0}) &= \vecbf{c} \\
> 	\vecbf{x}(t_{0}) = \Phi(t_{0})\vecbf{u}(t_{0}) &= \Phi(t_{0})\vecbf{c}. \\
> \end{align}$$
> 
> Since $\vecbf{x}(t_{0}) = \vecbf{x}_{0}$, this gives $\vecbf{c} = \Phi(t_{0})^{-1}\vecbf{b}$. Thus, 
> $$\vecbf{x}(t) = \Phi(t)\left( \Phi(t_{0})^{-1}\vecbf{x}_{0} + \int_{t_{0}}^t \Phi(s)^{-1}\vecbf{b}\,ds \right).$$