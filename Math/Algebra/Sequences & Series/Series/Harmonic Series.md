---
tags:
  - atom
  - math
---
$$ \sum_{k=1}^\infty \dfrac{1}{k} = 1 + \dfrac{1}{2} + \dfrac{1}{3} + \dfrac{1}{4}+ \cdots $$
has terms that approach zero but the [[Series|series]] diverges.

> [!proof]- Proof of Divergence
> $$\begin{array}{l}
> 	a_n = \dfrac{1}{n} \\
> 	\begin{align*}
> 		\dfrac{a_{n+1}}{a_n} &= \dfrac{n}{n+1} \\
> 		&= \dfrac{n+1}{n+1} - \dfrac{1}{n+1} \\
> 		&= 1 - \dfrac{1}{n+1} \\
> 	\end{align*} \\
> 	\displaystyle\lim_{n\to\infty} \dfrac{a_{n+1}}{a_n} = 1 \\
> \end{array}$$
> Therefore, [[The Ratio Test|the ratio test]] is inconclusive. #TODO
