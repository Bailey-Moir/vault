---
tags:
  - atom
  - comp
---
*Radix sort* is a method for extending [[Counting Sort|counting sort]] to work for large values of $k$. For each digit, starting from the least significant, the list is sorted using a [[Stable Sorts|stable sort]] (such as [[Counting Sort|counting sort]]).
$$\begin{array}{rl}
\hline
\scriptsize1& \textbf{procedure} \; \text{R{\scriptsize ADIX}-S{\scriptsize ORT}}(A, d) \\
\scriptsize2& \hspace{1em} \textbf{for} \; \text{i}  \; \textbf{from} \; 1 \; \textbf{to} \; d \\
\scriptsize3& \hspace{2em} \text{use a stable sort to sory array } A \text{ on digit } i \\
\hline
\end{array}$$

> [!example]- `[329, 457, 657, 839, 436, 720, 355]`
> - **Iteration 1**
>   `[720, 355, 436, 457, 657, 329, 839]`
> - **Iteration 2**
>   `[720, 329, 436, 839, 355, 457, 657]`
> - **Iteration 3**
>   `[329, 355, 436, 457, 657, 720, 839]`
