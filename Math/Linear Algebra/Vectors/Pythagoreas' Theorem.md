---
tags:
  - atom
  - math
  - linear
---
For $\vecbf{u},\vecbf{v}$ in an [[Inner Products|inner product space]] $V$,
$$\| \vecbf{u} \|^2 + \| \vecbf{v} \|^2 = \| \vecbf{u} + \vecbf{v} \|^2 \iff \left< \vecbf{u},\vecbf{v} \right> = 0$$

> [!proof]-
> Using the definition of [[Vector Length|norm]] and [[Linear Maps|linearity]] of [[Inner Products|inner products]], we get
> $$\begin{align}
> 	\| \vecbf{u}+\vecbf{v} \|^{2} &= \left< \vecbf{u}+\vecbf{v},\vecbf{u}+\vecbf{v} \right> \\
> 	&= \left< \vecbf{u},\vecbf{u} \right> + 2\left< \vecbf{u},\vecbf{v} \right> + \left< \vecbf{v},\vecbf{v} \right>  \\
> 	&= \| \vecbf{u} \|^{2}+2\left< \vecbf{u},\vecbf{v} \right> +\| \vecbf{v} \|^{2}  \\
> 	&= \| \vecbf{u} \|^{2} +\| \vecbf{v} \|^{2} & \left< \vecbf{u},\vecbf{v} \right> = 0 \\
> \end{align}$$