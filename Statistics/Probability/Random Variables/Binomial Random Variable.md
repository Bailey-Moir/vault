---
tags:
  - atom
  - stats
  - discrete
  - math
---
A *binomial random variable* $X \sim \text{Bin}(n,p)$ is a [[Random Variables|discrete random variable]] that counts the number of successes in $n$ [[Independent Events|independent]] trials, where each trial is a [[Bernoulli Random Variables|Bernoulli random variable]] with probability $p$.
$$ P(X=k) = \begin{pmatrix}
	n \\ k
\end{pmatrix} p^k (1-p)^{n-k} \hspace{2em} \forall k \in \Z_{n+1} $$
\[[[Binomial Coefficient]], [[Probability Function]], [[Residue Classes]]\]
# Mean and Variance of Binomial Random Variable
$$\begin{array}{ccc} 
	\mu_{X} = np &&
	\sigma_{X}^2 = np(1-p)
\end{array} $$
\[[[Mean of a Discrete Random Variable]], [[Variance of a Discrete Random Variable]]\]