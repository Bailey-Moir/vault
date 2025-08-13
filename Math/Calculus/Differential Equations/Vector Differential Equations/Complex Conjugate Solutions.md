---
tags:
  - atom
  - math
---
Suppose $A$ is a [[The Real Numbers|real]] square [[Matrices|matrix]] with two [[Eigenvectors & Eigenvalues|eigenpairs]]  $\{ \mu \pm i\omega; \vecbf{u} \pm i\vecbf{v} \}$, then $\vecbf{x}' = A\vecbf{x}$ has solutions
$$\begin{align}
	\vecbf{x}_{1} &= e^{\mu t}\cos(\omega t)\vecbf{u} \\
	\vecbf{x}_{2} &= e^{\mu t}\sin(\omega t)\vecbf{v}, \\
\end{align}$$
or
$$\begin{align}
	\vecbf{x}_{1} &= e^{\mu t}\left( \cos(\omega t)\vecbf{u}-\sin(\omega t)\vecbf{v} \right) \\
	\vecbf{x}_{2} &= e^{\mu t}\left( \cos(\omega t)\vecbf{u}+\sin(\omega t)\vecbf{v} \right) \\
\end{align}$$

> [!proof]-
> $$\begin{align}
> 	\vecbf{x}_\pm &=e^{(\mu \pm i\omega)t}\left( \vecbf{u} \pm i\vecbf{v} \right) \\
> 	&= e^{\mu t}\left( \cos(\omega t) \pm i\sin(\omega t) \right)\left( \vecbf{u} \pm i\vecbf{v} \right) \\
> 	&= e^{\mu t}\left( \cos(\omega t)\vecbf{u} - \sin(\omega t)\vecbf{v} \right) \pm ie^{\mu t}\left( \cos(\omega t)\vecbf{v} + \sin(\omega t)\vecbf{u} \right) \\
> \end{align}$$
> Since other solutions can be written as $c_{+}\vecbf{x}_{+} + c_{-}\vecbf{x}_{-}$, it can be shown that $c_{+} = \overline{c_{-}}$ (as all solutions must be [[The Real Numbers|real]]). If $c_{\pm}  = \dfrac{1}{2}$, then
> $$\begin{align}
> 	\dfrac{1}{2}\vecbf{x}_{+} + \dfrac{1}{2}\vecbf{x}_{-}
> 	&= \dfrac{1}{2}\left[ e^{\mu t}\left( \cos(\omega t)\vecbf{u} - \sin(\omega t)\vecbf{v} \right) + ie^{\mu t}\left( \cos(\omega t)\vecbf{v} + \sin(\omega t)\vecbf{u} \right) \right] \\
> 	&+\dfrac{1}{2}\left[ e^{\mu t}\left( \cos(\omega t)\vecbf{u} - \sin(\omega t)\vecbf{v} \right) - ie^{\mu t}\left( \cos(\omega t)\vecbf{v} + \sin(\omega t)\vecbf{u} \right) \right] \\
> 	&= e^{\mu t}\left( \cos(\omega t)\vecbf{u} - \sin(\omega t)\vecbf{v} \right) \\
> 	&= \vecbf{x}_{1},
> \end{align}$$ 
> and if $c_{\pm} = \mp \dfrac{i}{2}$
> $$\begin{align}
> 	-\dfrac{i}{2}\vecbf{x}_{+} + \dfrac{i}{2}\vecbf{x}_{-}
> 	&= -\dfrac{i}{2}\left[ e^{\mu t}\left( \cos(\omega t)\vecbf{u} - \sin(\omega t)\vecbf{v} \right) + ie^{\mu t}\left( \cos(\omega t)\vecbf{v} + \sin(\omega t)\vecbf{u} \right) \right] \\
> 	&+\dfrac{i}{2}\left[ e^{\mu t}\left( \cos(\omega t)\vecbf{u} - \sin(\omega t)\vecbf{v} \right) - ie^{\mu t}\left( \cos(\omega t)\vecbf{v} + \sin(\omega t)\vecbf{u} \right) \right] \\
> 	&= e^{\mu t}\left( \cos(\omega t)\vecbf{v} + \sin(\omega t)\vecbf{u} \right) \\
> 	&= \vecbf{x}_{1},
> \end{align}$$ 
> Since $\vecbf{x}_{1}$ and $\vecbf{x}_{2}$ are [[Linear Independence|linearly independent]] in $\text{span}\{ \vecbf{x}_{+},\vecbf{x}_{-} \}$, they must be a [[Basis|basis]], meaning they can be used to represent the same [[Sets|set]] of solutions.

\[[[Complex Conjugate Eigenpairs]]\]