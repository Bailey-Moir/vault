---
tags:
  - atom
  - math
---
A *category* consists of:
1. a [[Classes|class]] $\mathcal{C}$ of **objects**,
2. for each pair $x,y \in \mathcal{C}$, a [[Sets|set]] $\mathcal{C}(x,y)$ of pairwise [[Disjoint Sets|disjoint]] **morphisms**, and
3. for each triple $x,y,z \in \mathcal{C}$, a [[Functions|map]] $\mathcal{C}(x,y)\times \mathcal{C}(y,z) \to \mathcal{C}(x,z)$, called a **[[Composite Functions|composition]]** and denoted $\left( \alpha,\beta \right) \to \beta\alpha$, such that
	- *(Associativity)* $\gamma(\beta\alpha) = (\gamma\beta)\alpha$ for all **morphisms** $\alpha,\beta,\gamma$, and
	- *(Identity)* for all $x \in \mathcal{C}$, there exists an **identity morphism** $1_{x} \in \mathcal{C}(x,x)$ such that $1_{x}\alpha = \alpha$ and $\beta 1_{x} = \beta$ for any **morphisms** $\alpha,\beta$ where the indicated **[[Composite Functions|composition]]** is defined.