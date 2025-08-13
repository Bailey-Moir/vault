---
tags:
  - atom
  - math
  - linear
---
If $A$ is a [[The Real Numbers|real]] square [[Matrices|matrix]] with an [[Eigenvectors & Eigenvalues|eigenpair]]  $\{ \mu+i\omega; \vecbf{u}+i\vecbf{v} \}$, then its [[Complex Conjugates|complex conjugate]] $\{ \mu-i\omega; \vecbf{u}-i\vecbf{v} \}$ is also an [[Eigenvectors & Eigenvalues|eigenpair]].

> [!proof]-
> Since $\{ \mu+i\omega; \vecbf{u}+i\vecbf{v} \}$ is an [[Eigenvectors & Eigenvalues|eigenpair]] of $A$,
> $$\begin{align}
> 	A(\vecbf{u}+i\vecbf{v}) &= \left( \mu+i\omega \right)\left( \vecbf{u}+i\vecbf{v} \right) \\
> 	&= \left( \mu \vecbf{u}- \omega \vecbf{v} \right) + i\left( \mu \vecbf{v}+\omega \vecbf{u} \right). \\
> \end{align}$$
> Since $A$ is a [[Matrices|real matrix]], this can be split into
> $$\begin{align}
> 	A \vecbf{u} &= \mu \vecbf{u} - \omega \vecbf{v} &&\Re \\
> 	A \vecbf{v} &= \mu \vecbf{v} + \omega \vecbf{u}. && \Im \\
> \end{align}$$
> Then by [[Linear Maps|linearity]],
> $$\begin{align}
> 	A(\vecbf{u}-i\vecbf{v}) &= \left( \mu \vecbf{u}- \omega \vecbf{v} \right) - i\left( \mu \vecbf{v}+\omega \vecbf{u} \right). \\
> 	&= \left( \mu-i\omega \right)\left( \vecbf{u}-i\vecbf{v} \right). \\
> \end{align}$$
> Thus, $\{ \mu-i\omega; \vecbf{u}-i\vecbf{v} \}$ is also an [[Eigenvectors & Eigenvalues|eigenpair]] of $A$.
