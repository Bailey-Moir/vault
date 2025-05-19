---
tags:
  - atom
  - math
  - linear
---
The *direction angles* of a non-zero vector $\vecbf{a}$ are the angles $\alpha$, $\beta$, and $\gamma$ (on the interval $[0,\pi]$) that $\vecbf{a}$ makes with the positive $x$-, $y$-, and $z$-axes respectively. The cosines of these angles ($\cos\alpha$, $\cos\beta$, and $\cos\gamma$) are called the *direction cosines* of the vector $\vecbf{a}$. Using the [[Cosine Similarity Formula|cosine similarity formula]] where $\vecbf{b}$ is replaced by the [[Basis|basis vectors]] $\vecu{i}$, $\vecu{j}$, and $\vecu{k}$ gives the result: 
$$\begin{array}{ccc} \cos\alpha = \dfrac{a_1}{\left| \vecbf{a} \right|} & \cos\beta = \dfrac{a_2}{\left| \vecbf{a} \right|} & \cos\gamma = \dfrac{a_3}{\left| \vecbf{a} \right|} \end{array}$$
From these formulae, it can be shown that:
$$ \cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1 $$
They also imply that:
$$\begin{align*} \vecbf{a} &= \left\langle a_1, a_2, a_3 \right\rangle \\ &= \left| \vecbf{a} \right| \left\langle \cos\alpha, \cos\beta, \cos\gamma \right\rangle \end{align*}$$
Therefore,
$$ \dfrac{\vecbf{a}}{\left| \vecbf{a} \right|} = \left\langle \cos\alpha, \cos\beta, \cos\gamma \right\rangle $$
Meaning the direction cosines of a vector are the components of it's unit vector.