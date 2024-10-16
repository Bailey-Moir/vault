---
tags:
  - atom
  - math
---
Spherical coordinate systems (similar to [[Polar Form|polar form]]) come in the form 
$$(\rho, \theta, \phi) \text{ for } \rho \ge 0,\, 0 \le \phi \le \pi$$
$\rho :=$ the distance from the origin (equivalent of $r$ from [[Polar Form|polar form]])
	$\rho^2 = x^2 + y^2 + z^2$
	$\rho^2 = r^2 + z^2$ where $r$ is from [[Polar Form|polar form]]
$\phi :=$ the angle from the $z$ axis
$\theta :=$  the angle of the point of the point projected onto the $xy$ plane. This theta is the same $\theta$ as that seen in [[Polar Form|polar form]].

# Cartesian coordinates
$$\begin{array}{ccc}
 x = \rho \sin \phi \cos \theta & y = \rho \sin \phi \sin \theta & z = \rho \cos \phi
\end{array}$$
> [!proof]- Proof of Cartesian Coordinate Formulae
> $\cos \phi = \dfrac{z}{\rho}$, $\sin\phi = \dfrac{r}{\rho}$
> $\implies \rho \cos \phi = z, \rho \sin \phi = r$
> Recall $x = r \cos \theta$, $y = r \sin \theta$
> $\implies x = \rho \sin \phi \cos \theta$
> $\phantom{\implies} y = \rho \sin \phi \sin \theta$
> $\phantom{\implies} z = \rho \cos \phi$

# Spherical Wedge
If $E$ is a spherical wedge given by
$$ \left\{ \left(\rho, \theta, \phi\right):\: a \le \rho \le b,\, \alpha \le \theta \le \beta,\, c \le \phi \le d \right\}$$
then
$$ \int\int\int_E f(x,y,z) \, dV = \int_c^d \int _\alpha^\beta \int_a^b f(\rho \sin \phi\cos\theta, \rho \sin \phi \sin \theta, \rho \cos \phi) \rho^2 \sin\phi \, d\rho \, d\theta \, d\phi $$
$dV = \rho \, d\phi \, d\rho \, r\,d\theta$
$dV = \rho \, d\phi \, d\rho \, \rho\sin\phi \, d\theta$
$dV = \rho^2 \sin\phi \, d\phi \, d\rho \, d\theta$

# Examples
> [!example]- Equation $\rho = c$
> This gives a sphere at the origin of radius $c$.

> [!example]- Equation $\theta = c$
> This gives a half-plane passing through the whole $z$-axis, and stopping at it. In  order to get across it with $\theta$ being constant, $\rho$ would have to flip sign, or $\phi$ would have to be in $\left(2\pi n + \pi, 2\pi (n+1) \pi\right)$, which is outside of their constraints.

> [!example]- Equation $\phi = c$
> This represents a half cone above the origin, not going below as $\rho$ would have to become negative.

