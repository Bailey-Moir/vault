---
tags:
  - atom
  - math
  - linear
---
A *norm* of a [[Vector Spaces|vector space]] $V$ is a [[Functions|function]] $\| \cdot \| : V \to \R$ that assigns each $\vecbf{v} \in V$ a real number $\| \vecbf{v} \|$ such that for all $\vecbf{u},\vecbf{v} \in V$ and $c \in \R$,
1. **[[Inner Products|Positive Definite]]**
   $\| \vecbf{v} \| \ge 0$
   $\| \vecbf{v} \|=0\iff \vecbf{v}=0$
2. **[[Linear Maps|Absolute Homogeneity]]**
   $\| \lambda \vecbf{v} \| = \left| \lambda \right|\| \vecbf{v} \|$
3. **[[The Triangle Inequality|The Triangle Inequality]]**
   $\| \vecbf{u}+\vecbf{v} \| \le \| \vecbf{u} \|+\| \vecbf{v} \|$

> [!definition] Induced Norms
> In an [[Inner Products|inner product space]], an **induced norm** is the *norm* given by
> $$\| \vecbf{v} \|^2 = \left< \vecbf{v},\vecbf{v} \right> $$