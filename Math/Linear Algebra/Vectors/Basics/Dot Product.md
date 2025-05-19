---
tags:
  - atom
  - math
  - linear
---
The *dot product* (or *scalar/inner product*) is a measure of how similar two [[Math/Linear Algebra/Vectors/Vectors|vectors]] directions are. It is found by multiplying [[Components|components]].
$$\begin{align*}
	\vecbf{u} \cdot \vecbf{v} &= u_1v_1 + u_2v_2 + \dots \\
	&= \left\| \vecbf{u} \right\| \left\| \vecbf{v} \right\| \cos \theta && \theta \text{ is the angle between } \vecbf{u} \text{ and } \vecbf{v}
\end{align*}$$
\[[[Orthogonal Vectors]]\]

> [!notes] The *dot product* on $\R^n$ is a [[Functions|function]] $\R^n \times \R^n \to \R$.

> [!note] The *dot product* of column vectors $\vecbf{u}$ and $\vecbf{v}$ can be given by $$\vecbf{u} \cdot \vecbf{v} = \vecbf{u}^T\vecbf{v}$$
# Properties of Dot Product
1. **Commutative**
	$\vecbf u \cdot \vecbf v = \vecbf v \cdot \vecbf u$
2. **Distributive**
	$\vecbf w\cdot(\vecbf u + \vecbf v) = \vecbf w\cdot\vecbf u + \vecbf z\cdot\vecbf v$
3. **Positive Definite**
	$\vecbf{u} \cdot \vecbf{u} \ge 0$
	$\vecbf{u} \cdot \vecbf{u} = 0 \iff \vecbf{u} = \vecbf{0}$
4. ***Associative***
	$s(\vecbf u \cdot \vecbf v) = (s\vecbf u) \cdot \vecbf v = \vecbf u \cdot (s\vecbf v)$

> [!note] A function $V \times V \to \F$ which satisfies $1$ and $2$ is called a **symmetric bilinear pairing**.

> [!note] A function $V \times V \to \F$ which satisfies $1$, $2$, and $3$ is called an **inner product**.