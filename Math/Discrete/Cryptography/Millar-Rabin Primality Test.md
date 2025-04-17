---
tags:
  - atom
  - math
  - discrete
---
The *Millar-Rabin [[Primality Test|primality test]]* is a [[Primality Test|probabilistic primality test]].
$$\begin{array}{rl}
\hline

\scriptsize1& \textbf{procedure} \; \text{MR-T{\scriptsize EST}}(n,k) \\
\scriptsize2& \hspace{1em} s \leftarrow \left\lfloor \log_{2}(n-1) \right\rfloor  \\
\scriptsize3& \hspace{1em} d \leftarrow \dfrac{n-1}{2^s}  \\
\scriptsize4& \hspace{1em} \textbf{for} \; \text{\_}  \; \textbf{from} \; 1 \; \textbf{to} \; k \\
\scriptsize5& \hspace{2em} a \leftarrow \text{random non-zero element of } \Z_{n} \\
\scriptsize6& \hspace{2em} \textbf{if} \; a^d \equiv 1 \mod n \\
\scriptsize7& \hspace{3em} \textbf{continue} \\
\scriptsize8& \hspace{2em} \textbf{for} \; r  \; \textbf{from} \; 0 \; \textbf{to} \; s-1 \\
\scriptsize9& \hspace{3em} \textbf{if} \; a^{2^{r}d} \equiv -1 \mod n \\
\scriptsize10& \hspace{4em} \textbf{continue} \\
\scriptsize11& \hspace{2em} \textbf{return} \; \text{F{\scriptsize ALSE}} \\
\scriptsize11& \hspace{1em} \textbf{return} \; \text{T{\scriptsize RUE}} \\
\hline
\end{array}$$

> [!note] $n - 1 = 2^sd$
 
> [!theorem] If $p$ is [[Primes|prime]], then the only square roots of $1$ in $\Z_{p}$ are $\pm 1$[^1]

> [!corollary]
> Let $p$ be a [[Primes|prime]], and write $p-1 = 2^sd$ with odd $d$. For any $a \in \Z_{p}^\times$, either
> - $a^d = 1 \mod p$, or
> - $a^{2^r{d}} = -1 \mod p$ for some $r = 1, \dots, s-1$.

> [!analysis] For a fixed number of iterations, *Millar-Rabin* is $\mathcal{O}(\log n)$.

\[[[Primality Test]]\]

[^1]: [[Quadratic Residues]]
