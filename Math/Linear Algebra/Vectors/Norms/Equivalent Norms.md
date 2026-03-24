---
tags:
  - atom
  - math
---
Two [[Norms|norms]] $\| \cdot \|_{1}$ and $\| \cdot \|_{2}$ on the same [[Vector Spaces|vector space]] $V$ are *equivalent* iff
$$\exists A,B \in \R_{> 0} : \forall \vecbf{v} \in V, A\| \vecbf{v} \|_{1} \le \| \vecbf{v} \|_{2} \le B\| \vecbf{v} \|_{1}.$$

> [!note] Note the similarity to [[Asymptotic Notation#$ Theta$|asymtotic notation]].

> [!theorem]- In [[Metric Spaces|metric spaces]] [[Norms#^induced-metrics|induced]] by *equivalent norms*, if a [[Sequences|sequence]] [[Metric Convergence|converges]] in one, it [[Metric Convergence|converges]] to the same thing in the others.
> Let $\| \cdot \|_{1}$ and $\| \cdot \|_{2}$ be two *equivalent* [[Norms|norms]] on the [[Vector Spaces|vector space]] $V$, meaning there exists $0 < A \le B$ such that for all $\vecbf{v} \in V$,
> $$A\| \vecbf{v} \|_{1} \le \| \vecbf{v} \|_{2} \le B\| \vecbf{v} \|_{1}.$$
> Suppose a [[Sequences|sequence]] $( \vecbf{a_{n}} )$ [[Metric Convergence|converges]] to $\vecbf{\lambda} \in V$ in the [[Metric Spaces|metric space]] [[Norms#^induced-metrics|induced]] by $\| \cdot \|_{1}$, meaning for all $\varepsilon/B > 0$, there exists $N \in \N$ such that for all $n \ge N$,
> $$\begin{align}
> 	d_{1}(\vecbf{a_{n}}, \vecbf{\lambda}) &< \dfrac{\varepsilon}{B} \\
> 	\| \vecbf{a_{n}} - \vecbf{\lambda} \|_{1} &< \dfrac{\varepsilon}{B} \\
> 	\| \vecbf{a_{n}} - \vecbf{\lambda} \|_{2} \le B\| \vecbf{a_{n}} - \vecbf{\lambda} \|_{1} &< \varepsilon \\
> 	d_{2}(\vecbf{a_{n}}, \vecbf{\lambda}) &< \varepsilon. \\
> \end{align}$$
> Thus, $( \vecbf{a_{n}} )$ [[Metric Convergence|converges]] to $\vecbf{\lambda}$ in the [[Metric Spaces|metric space]] [[Norms#^induced-metrics|induced]] by $\| \cdot \|_{2}$ as well.
^convergence

> [!example]- The [[P-Norms|1-]] [[P-Norms|2-]] and $\infty$[[P-Norms|-norms]] are all *equivalent* (in fact, all [[P-Norms|p-norms]] are *equivalent*)
> Let $\vecbf{v} \in \R^n$ for some $n \in \N$. Then
> $$\begin{array}{c}
> 	\displaystyle \max \left| v_{i} \right| \le \sum \left| v_{i} \right|  \le n\displaystyle \max \left| v_{i} \right|  \\
> 	\| \vecbf{v} \|_{\infty} \le \| \vecbf{v} \|_{1} \le n\| \vecbf{v} \|_{\infty} \\
> 	\\
> 	\displaystyle \max \left| v_{i} \right| = \sqrt{ \max \left| v_{i} \right|^2} \le \sqrt{ \sum \left| v_{i} \right|^2 } \le \sqrt{ n\max \left| v_{i} \right|^2} = \sqrt{n}\displaystyle \max_{\vecbf{v} \in \R^{n}} \\
> 	\| \vecbf{v} \|_{\infty} \le \| \vecbf{v} \|_{2} \le \sqrt{n}\| \vecbf{v} \|_{\infty} \\
> 	\\
> 	\to \dfrac{1}{n} \| \vecbf{v} \|_{1} \le \| \vecbf{v} \|_{\infty} \le \| \vecbf{v} \|_{2} \le \sqrt{n}\| \vecbf{v} \|_{\infty} \le \sqrt{ n } \| \vecbf{v} \|_{1}. \\
> 	\dfrac{1}{n} \| \vecbf{v} \|_{1} \le \| \vecbf{v} \|_{2} \le \sqrt{ n } \| \vecbf{v} \|_{1}. \\
> \end{array}$$
> Thus, all three are *equivalent*.
^p-norms