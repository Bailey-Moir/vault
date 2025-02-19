---
tags:
  - atom
  - comp
---
# Definitions
## $O$
$O(g)$ is the [[Sets|set]] of [[Functions|functions]] that asymptotically grow **at most** as fast as $g$
$$O(g) = \{ f : \exists c > 0, x_{0} : \forall x > x_{0}, \mathbf{0 \le f(x) \le cg(x)} \}$$
*$\mathit{g}$ is an asymptotic upper bound for these [[Functions|functions]].*
## $\Omega$
$\Omega(g)$ is the [[Sets|set]] of [[Functions|functions]] that asymptotically grow **at least** as fast as $g$
$$\Omega(g) = \{ f : \exists c > 0, x_{0} : \forall x > x_{0}, \mathbf{0 \le cg(x) \le f(x)}  \}$$
*$\mathit{g}$ is an asymptotic lower bound for these [[Functions|functions]].*
## $\Theta$
$\Omega(g)$ is the [[Sets|set]] of [[Functions|functions]] that asymptotically grow as fast as $g$
$$ \Theta(g) = O(g) \cap \Omega(g)$$
*$\mathit{g}$ is an asymptotic upper and lower bound for these [[Functions|functions]].*
# Theorems

> [!note]- $f \in O(g) \land f \in \Omega(g) \iff f \in \Theta(g)$

> [!note]- $f \in \Theta(g) \iff g \in \Theta(f)$

> [!note]- $f \in O(g) \iff g \in \Omega(f)$