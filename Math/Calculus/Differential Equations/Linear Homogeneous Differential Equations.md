---
tags:
  - atom
  - math
---
The solutions to a given *[[Linear Differential Equations|linear]] [[Homogeneous Systems|homogeneous]] [[Differential Equations|DE]]* on a given [[Math/Algebra/Basics/Intervals|interval]] form a [[Vector Spaces|vector space]].

> [!note] The [[Dimension|dimension]] of this solution [[Vector Spaces|space]] is the [[Order|order]] of the [[Differential Equations|DE]].

> [!proof]-
> Given a [[Linear Differential Equations|linear]] *homogeneous DE*
> $$ a_n(t)\dfrac{d^ny}{{dt}^n} +  a_{n-1}(t)\dfrac{d^{n-1}y}{{dt}^{n-1}} + \dots + a_1(t) \dfrac{dy}{dt} + a_0(t)y = 0,$$
> the [[Sets|set]] of solutions $U$ on an [[Math/Algebra/Basics/Intervals|interval]] $I$ is a [[Subsets|subset]] of $\F^I$[^1] (a [[Vector Spaces|vector space]] over $\F$), meaning $U$ is a [[Vector Spaces|vector space]] iff it is a [[Subspaces|subspace]] of $\F^I$.
> 
> **Identity**
> Substituting $y = 0$ gives 
> $$\begin{align}
> 	a_n(t)\dfrac{d^n}{{dt}^n}(0) +  a_{n-1}(t)\dfrac{d^{n-1}}{{dt}^{n-1}}(0) + \dots + a_1(t) \dfrac{d}{dt}(0) + 0a_0(t) &= 0 \\
> 	a_n(t)(0) +  a_{n-1}(t)(0) + \dots + a_1(t) \dfrac{d}{dt}(0) + 0a_0(t) &= 0 \\
> 	0 &= 0 \\
> \end{align}$$
> Thus, $0$ is a solution, meaning $0 \in U$.
> 
> **Closed Under Addition**
> Suppose $y_{1},y_{2} \in U$, meaning $y_{1}$ and $y_{2}$ are solutions to the [[Differential Equations|DE]]. Then
> $$\begin{align}
> 	a_n(t)\dfrac{d^n}{{dt}^n}(y_{1}) +  a_{n-1}(t)\dfrac{d^{n-1}}{{dt}^{n-1}}(y_{1}) + \dots + a_1(t) \dfrac{d}{dt}(y_{1}) + a_0(t)(y_{1}) &= 0 \\
> 	a_n(t)\dfrac{d^n}{{dt}^n}(y_{2}) +  a_{n-1}(t)\dfrac{d^{n-1}}{{dt}^{n-1}}(y_{2}) + \dots + a_1(t) \dfrac{d}{dt}(y_{2}) + a_0(t)(y_{2}) &= 0 \\
> \end{align}$$
> By [[Fields|distributivity]] and the [[Linear Maps|linearity]] ([[Additive Property|additivity]]) of differentiation, adding these equations together gives
> $$\begin{alignat}{3}
> 	a_n(t)\dfrac{d^n}{{dt}^n}(y_{1} + y_{2}) &+  a_{n-1}(t)\dfrac{d^{n-1}}{{dt}^{n-1}}(y_{1} + y_{2}) + \dots \\
> 	&k+ a_1(t) \dfrac{d}{dt}(y_{1} + y_{2}) + a_0(t)(y_{1} + y_{2}) = 0 \\
> \end{alignat}$$
> Thus, $y_{1}+y_{2}$ is a solution, meaning $y_{1}+y_{2} \in U$.
> 
> **Closed Under Scalar Multiplication**
> Suppose $y \in U$ and $\lambda \in \F$, meaning $y$ is a solution to the [[Differential Equations|DE]]. Then
> $$\begin{align}
> 	a_n(t)\dfrac{d^n}{{dt}^n}(y) + a_{n-1}(t)\dfrac{d^{n-1}}{{dt}^{n-1}}(y) + \dots + \lambda a_1(t) \dfrac{d}{dt}(y) + a_0(t)(y) &= 0 \\
> 	\lambda a_n(t)\dfrac{d^n}{{dt}^n}(y) +  \lambda a_{n-1}(t)\dfrac{d^{n-1}}{{dt}^{n-1}}(y) + \dots + \lambda a_1(t) \dfrac{d}{dt}(y) + \lambda a_0(t)(y) &= 0 \\
> \end{align}$$
> By the [[Linear Maps|linearity]] (homogeneity) of differentiation,
> $$\begin{alignat}{3}
> 	a_n(t)\dfrac{d^n}{{dt}^n}(\lambda y_{1}) +  a_{n-1}(t)\dfrac{d^{n-1}}{{dt}^{n-1}}(\lambda y_{1}) + \dots + a_1(t) \dfrac{d}{dt}(\lambda y_{1}) + a_0(t)(\lambda y_{1}) &= 0 \\
> \end{alignat}$$
> Thus, $\lambda y$ is a solution, meaning $\lambda y \in U$.

\[[[Wronskian Determinant]]\]

[^1]: [[Sets of Functions]]