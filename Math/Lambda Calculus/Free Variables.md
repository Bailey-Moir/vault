---
tags:
  - atom
  - math
  - comp
---
The *free variables* of a [[Lambda Terms|term]] are those variables not bound by an [[Lambda Abstraction|abstraction]]. The set of *free variables* of a [[Lambda Terms|term]] is defined inductively:
- The *free variables* of $x$ are just $x$.
- The set of *free variables* of $\lambda x. M$ is the set of free variables of $M$, but with $x$ removed.
- The set of *free variables* of $M\:N$ is the union of the set of *free variables* of $M$ and the set of *free variables* of $N$.