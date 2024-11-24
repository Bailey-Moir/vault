---
tags:
  - atom
  - math
---
The *curl* measures how much a [[Vector Fields|vector field]] spreads out from a given point. It can be defined as the [[Cross Product|cross product]] with the [[Nabla Operator|nabla operator]]:
$$\begin{align*}
	\text{curl}\,\vecbf{f} = \nabla \times \vecbf{f} &= \left( \dfrac{\partial \vecbf{f}_y}{\partial x} - \dfrac{\partial \vecbf{f}_x}{\partial y} \right) \vecu{e}_3 && \text{in } \R^2 \\
	&= \left\langle \dfrac{\partial \vecbf{f}_z}{\partial y} - \dfrac{\partial \vecbf{f}_y}{\partial z}, \dfrac{\partial \vecbf{f}_x}{\partial z} - \dfrac{\partial \vecbf{f}_z}{\partial x}, \dfrac{\partial \vecbf{f}_y}{\partial x} - \dfrac{\partial \vecbf{f}_x}{\partial y} \right\rangle && \text{in } \R^3
\end{align*}$$
