---
tags:
  - atom
  - math
  - linear
---
For $A \in \R^{n,n}$[^1], every [[Eigenvectors & Eigenvalues|eigenvalue]] of $A$ is contained within a **Gerschgorin disk**.
![600|center](gerschgorins-theorem.excalidraw.md)

> [!definition] Gerschgorin disk
> Let $A \in \R^{n,n}$[^1] with entries $a_{ij}$, and let $r_i = \sum_{j\ne i}\left| a_{ij} \right|$.
> The $i$-th *Gerschgorin disk* is the circular disk $D_{i}$ in the [[Complex Numbers|complex plane]] with centre $a_{ii}$ and radius $r_{i}$;
> $$D_{i} = \{ z \in \C : \left| z - a_{ii} \right| \le r_{i} \}$$

> [!theorem]- Each [[Disjoint Sets|disjoint]] [[Unions and Intersections|union]] of $k$ **Gerschgorin disks** contains exactly $k$ [[Eigenvectors & Eigenvalues|eigenvalues]].

> [!theorem] [[Complex Numbers|Complex]] [[Eigenvectors & Eigenvalues|eigenvalues]] come in [[Complex Conjugates|conjugate]] pairs. 

[^1]: [[Sets of Matrices]]