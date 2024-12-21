---
tags:
  - atom
  - comp
---
Quadratic probing is a form of [[Open Addressing|open addressing]], the same as [[Linear Probing|linear probing]] except instead of just checking the next slot, quadratic probing uses the square to generate the index.
$$i,i+1^2,i+2^2, i+3^2, \cdots$$
> [!note]- Trick for Calculating
> You can use the fact that $\forall x \in \Z^+, x^2 = \sum_{k=1}^x(2k-1)$ to calculate the next index [[Recursion|recursively]]. If $f(x)$ calculates the index after $x$ collisions, $i$ is the starting index, and $n$ is the number of slots,
> $$\begin{align*}
> 	f(x) &= i + x^2 &&\text{in } \Z_{n} \\
> 	&= i + \sum_{k=1}^x(2k-1),
> \end{align*}$$
> which gives
> $$\begin{align*}
> 	f(x) - f(x-1) &\equiv i + \sum_{k=1}^x(2k-1) - i - \sum_{k=1}^{x-1}(2k-1) \\
> 	&= \sum_{k=1}^x(2k-1) - \sum_{k=1}^{x-1}(2k-1) \\
> 	&= 2x-1 \\
> 	f(x)&= f(x-1) + 2x-1
> \end{align*}$$
> Thus, the indices in *quadratic probing* can be calculated by adding the odd numbers to the current index.
> $$ f(x) = f(x-1) + 2x-1 \text{ in } \Z_{n} \hspace{2em}f(0)=i$$
> $$\begin{array}{ccccc}
> 	\tiny\text{Collision \#1} &&
> 	\tiny\text{Collision \#2} &&
> 	\tiny\text{Collision \#3} &&
> 	\\
> 	i \leftarrow i + 1 &&
> 	i \leftarrow i + 3 &&
> 	i \leftarrow i + 5 &&
> 	\cdots &&
> \end{array}$$
> \[[[Modular Arithmetic]]\]

\[[[Hash Tables]]\]