---
tags:
  - atom
  - math
---
The *nabla operator* ($\nabla$) is a vector of partial differential operators, with the 3 dimensional *nabla operator* defined as:
$$ \nabla = \left\langle \dfrac{\partial}{\partial x},\, \dfrac{\partial}{\partial y},\, \dfrac{\partial}{\partial z}\right\rangle $$

- The [[Gradient|gradient]] of a [[Scalar Fields|scalar field]] $f$ can be defined as [[Vector Scalar Multiplication|scalar multiplication]] of $\nabla$ with $f$, giving a [[Vector Fields|vector field]].
$$(\nabla f)(x)$$
$$\begin{array}{ccc}
	f : \R^n \to \R && (\nabla f ): \R^n \to \R^n
\end{array}$$
- The [[Divergence|divergence]] of a [[Vector Fields|vector field]] $\vecbf{f}$ can be defined as the [[Dot Product|dot product]] of $\nabla$ with $\vecbf{f}$, giving a [[#Scalar Fields|scalar field]].
$$(\nabla \cdot \vecbf{f})$$
$$\begin{array}{ccc}
	\mathbf{f} : \R^n \to \R^n && (\nabla \cdot \mathbf{f} ): \R^n \to \R
\end{array}$$
- The [[Curl|curl]] of [[Vector Fields|vector field]] $\vecbf{f}$ can be defined as the [[Cross Product|cross product]] of $\nabla$ with $\vecbf{f}$, giving a [[Vector Fields|vector field]].
$$(\nabla \times \vecbf{f})$$
$$\begin{array}{ccc}
	f : \R^n \to \R^n && (\nabla \times f): \R^n \to \R^n
\end{array}$$
