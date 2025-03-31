---
tags:
  - atom
  - math
  - discrete
  - comp
---
A [[Primality Test|deterministic primality test]] for all [[Primes|primes]] up to $n$, with a time complexity of $\mathcal{O}(n\log\log n)$. 
$$\begin{array}{rl}
\hline

\scriptsize1& \textbf{procedure} \; \text{S{\scriptsize IEVE}-O{\scriptsize F}-E{\scriptsize RATOSTHENES}}(n) \\
\scriptsize2& \hspace{1em} is\text{-}prime \leftarrow \text{array of length } n+1 \text{ filled with T{\scriptsize RUE}} \\
\scriptsize2& \hspace{1em} is\text{-}prime[0] \leftarrow \text{F{\scriptsize ALSE}} \\
\scriptsize8& \hspace{1em} \textbf{for} \; i \; \textbf{from} \; 2 \; \textbf{to} \; n  \\
\scriptsize8& \hspace{2em} \textbf{if} \; is\text{-}prime(i) \; \textbf{and} \; i^2 \le n \\
\scriptsize8& \hspace{3em} \textbf{for} \; j \; \textbf{from} \; i^2 \; \textbf{to} \; n, \textbf{ step } i  \\
\scriptsize2& \hspace{4em} is\text{-}prime[j] \leftarrow \text{F{\scriptsize ALSE}} \\

\hline
\end{array}$$

> [!implementation]- C++
> ```cpp
> int n;
> vector<bool> is_prime(n+1, true);
> is_prime[0] = is_prime[1] = false;
> for (int i = 2; i <= n; i++) 
> 	if (is_prime[i] && (long long) i * i <= n) 
> 		for (int j = i * i; j <= n; j += i) 
> 			is_prime[j] = false;
> ```