---
tags:
  - atom
  - comp
---
*Merge sort* splits the list in the middle and [[Recursion|recursively]] performs *merge sort* on the two resulting lists. It then *merges* these two sorted halves in order.  
$$\begin{array}{rl}
\hline

\scriptsize1& \textbf{procedure} \; \text{M{\scriptsize ERGE}-S{\scriptsize ORT}}(A,l,r) \\
\scriptsize2& \hspace{1em} \textbf{if} \; l < r \\
\scriptsize3& \hspace{2em} m \leftarrow \left\lfloor \frac{l+r}{2} \right\rfloor \\
\scriptsize4& \hspace{2em} \text{M{\scriptsize ERGE}-S{\scriptsize ORT}}(A,l,m) \\
\scriptsize5& \hspace{2em} \text{M{\scriptsize ERGE}-S{\scriptsize ORT}}(A,m+1,r) \\
\scriptsize6& \hspace{2em} \text{M{\scriptsize ERGE}}(A,l,m,r) \\

\hline
\end{array}$$
The merge is normally done with a pointer in each list, taking the smaller of the two values, and incrementing the pointer forward in the list that was taken from.
- **Best Case** 
  Already sorted. Every merge increments through one list until empty, leaving the other list.
  $T(n) = 2T(\frac{n}{2}) + \frac{n}{2} = \mathcal{O}(n\log n)$ as $n \to \infty$.[^1]
- **Worst case**
  Every merge alternates between lists when incrementing.
  $T(n) = 2T(\frac{n}{2}) + n-1 = \mathcal{O}(n \log n)$ as $n \to \infty$.[^1]

*Merge sort* has an inexpensive split and a costly merge/join, while [[Quick Sort|quick sort]] has a costly split and an inexpensive join.

> [!note]- Extra Space
> In order to merge, a new list must be created in order to be $\mathcal{O}(n)$, meaning that extra space of $\mathcal{O}(n)$. #TODO 

[^1]: [[Landua's Big Oh Notation]]