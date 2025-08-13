---
tags:
  - atom
  - math
---
Suppose $\{ \lambda_{k},\vecbf{v}_{k} \}_{k=1}^n$ are [[Eigenvectors & Eigenvalues|eigenpairs]] for $A \in \R^{m,m}$. Then
$$\vecbf{x}_{k} = e^{\lambda_{k}t}\vecbf{v}_{k}$$
is a solution to $\dfrac{d\vecbf{x}}{dt}=A\vecbf{x}$.

> [!proof]-
> $$\begin{align}
> 	\dfrac{d\vecbf{x}_{k}}{dt} &= \lambda_{k}e^{\lambda _{k}t}\vecbf{v}_{k} \\
> 	&= \lambda_{k}\vecbf{x}_{k} \\
> 	&= A(t)\vecbf{x}_{k} \\
> \end{align}$$

# Repeated Eigenvalues
Suppose $\lambda$ is an [[Eigenvectors & Eigenvalues|eigenvalue]] of $A$ with a [[Geometric and Algebraic Multiplicity|algebraic multiplicity]] of 2, but $E_{\lambda}(A) =\text{span}\{ \vecbf{v} \}$ (the [[Geometric and Algebraic Multiplicity|geometric multiplicity]] is 1). Then
$$\exists \vecbf{u} \in \R^m : \hspace{1em} (A-\lambda I)\vecbf{u} = \vecbf{v},$$
where $\vecbf{u}$ forms a solution
$$\vecbf{x} = te^{\lambda t}\vecbf{v}+e^{\lambda t}\vecbf{u}$$
