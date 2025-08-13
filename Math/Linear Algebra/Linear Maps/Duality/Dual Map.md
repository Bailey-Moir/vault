---
tags:
  - atom
  - math
  - linear
---
The *dual map* of $T \in \mathcal{L}(V,W)$ is the [[Linear Maps|linear map]] $T' \in \mathcal{L}(W',V')$[^1], defined such that for each $\varphi \in W'$
$$T'(\varphi) = \varphi T,$$
meaning $T'$ maps the output of $T$ into $\F$ using the [[Linear Functionals|linear functional]] $\varphi$.

> [!example]
> Suppose $\varphi$ is the [[Linear Functionals|linear functional]] on $\mathcal{P}(\R)$ defined by $\varphi(p) = p(3)$ ($\varphi$ subs in $3$). Then $D'(\varphi)$[^2] is given by
> $$\begin{align}
> 	(D'(\varphi))(p) &= (\varphi D)(p) \\
> 	&= \varphi (p') \\
> 	&= p'(3), \\
> \end{align}$$
> i.e., $D'(\varphi)$ subs $3$ into the derivative.


[^1]: [[Dual Space]]
[^2]: [[D-operators]]
