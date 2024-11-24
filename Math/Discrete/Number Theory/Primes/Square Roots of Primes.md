---
tags:
  - atom
  - math
  - discrete
---
$$ \forall p \in \mathbb{P}, \sqrt{p} \in \R \setminus \Q $$
> [!proof]-
> Suppose the negation is true: $\exists p \in \mathbb{P} : \sqrt{p} \notin \R \setminus \Q$. Thus
> $$\begin{align*}
> 	\sqrt{p} &= \dfrac{m}{n} && n \ne 0, m,n \in \Z \\
> 	p &= \dfrac{m^2}{n^2} \\
> 	n^2p &= m^2 \\
> \end{align*}$$
> Let $n = p^{k_n} \prod x_i$ and $m = p^{k_m} \prod y_i$ where $k_n$ and $k_m$ are the number of times $p$ occurs in the prime factorization of $n$ and $m$ respectively, and $x_1,x_2,\dots,x_i$ and $y_1,y_2,\dots,y_i$ are the remaining prime factors.  
> $$\begin{align*}
> 	n^2p &= m^2 \\
> 	\left( p^k_n \prod x_i \right)^2 p &= \left( p^k_m \prod y_i \right)^2 \\
> 	p^{2k_n+1} \prod x_i^2 &= p^{2k_m} \prod y_i^2
> \end{align*}$$
> The LHS has $p$ in its prime factorization an odd amount of times, whereas the RHS has it an even amount of times. Each integer has a unique prime factorization due to the [[Fundamental Theorem of Arithmetic]], so these numbers can not be equal, implying a contradiction. $\square$
