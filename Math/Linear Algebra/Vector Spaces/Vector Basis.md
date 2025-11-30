---
tags:
  - atom
  - math
  - linear
---
![400|center](basis-vectors.excalidraw.md)
A *basis* of $V$ is a [[Span|spanning list]] of $V$ that is [[Linear Independence|linearly independent]].

> [!note] Condition for Basis
> $\vecbf{v}_1, \dots, \vecbf{v}_n$ is a *basis* of $V$ iff every $\vecbf{v} \in V$ can be written **uniquely** in the form
> $$ \vecbf{v} = a_1 \vecbf{v}_1 + \dots + a_n \vecbf{v}_n, $$
> where $a_1, \dots, a_n \in \F$.
> > [!proof]-
> > ($\implies$)
> > Suppose $\vecbf{v}_{1}, \dots, \vecbf{v}_{n}$ is a *basis* of $V$.
> > 
> > Let $\vecbf{v} \in V$. Since $\vecbf{v}_{1} \dots, \vecbf{v}_{n}$ [[Span|spans]] $V$,there exists $a_{1}, \dots, a_{n} \in \F$ such that
> > $$ \vecbf{v} = a_1 \vecbf{v}_1 + \dots + a_n \vecbf{v}_n. $$
> > Since $\vecbf{v}_{1}, \dots, \vecbf{v}_{n}$ is [[Linear Independence|linearly independent]] and $\vecbf{v}$ is in their [[Span|span]], by the definition of [[Linear Independence|linear independence]], the coefficients $a_{1},\dots,a_{n}$ must be unique.
> > 
> > ($\impliedby$)
> > Suppose every $\vecbf{v} \in V$ can be written uniquely in the form
> > $$ \vecbf{v} = a_1 \vecbf{v}_1 + \dots + a_n \vecbf{v}_n, $$
> > where $a_1, \dots, a_n \in \F$. By their respective definitions, $\vecbf{v}_{1}, \dots, \vecbf{v}_{n}$ must [[Span|span]] $V$ and be [[Linear Independence|linearly independent]], meaning it is a [[Vector Basis|basis]] of $V$.

> [!proof]- Every [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]] has a *basis*.
> By definition, every [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]] has a finite [[Span|spanning list]]. 
> This [[Span|spanning list]] can be reduced to a *basis*[^1], meaning every [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]] has a *basis*.

> [!proof]- All *bases* of a [[Finite-Dimensional Vector Spaces|finite-dimensional vector space]] have the same length.
> Suppose you have two *bases* $B_1$ and $B_2$.
> 
> $B_1$ is [[Linear Independence|linearly independent]] and $B_2$ is a [[Span|spanning list]], so $B_1$ is at most the same size as $B_2$[^1]. Reversing the roles gives that they are the same size.

\[[[Standard Basis Vectors]]\]

[^1]: [[Linear Independence and Span with Dimension]]