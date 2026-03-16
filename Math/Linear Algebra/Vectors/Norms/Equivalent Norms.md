---
tags:
  - atom
  - math
---
Two [[Norms|norms]] $\| \cdot \|_{1}$ and $\| \cdot \|_{2}$ on the same [[Vector Spaces|vector space]] $V$ are *equivalent* iff
$$\exists A,B \in \R_{> 0} : \forall \vecbf{v} \in V, A\| \vecbf{v} \|_{1} \le \| \vecbf{v} \|_{2} \le B\| \vecbf{v} \|_{1}.$$

> [!note] Note the similarity to [[Asymptotic Notation#$ Theta$|asymtotic notation]].

> [!theorem]- In [[Metric Spaces|metric spaces]] [[Norms#^induced-metrics|induced]] by *equivalent norms*, if a [[Sequences|sequence]] [[Metric Sequence Convergence|converges]] in one, it [[Metric Sequence Convergence|converges]] to the same thing in the others.
> Let $\| \cdot \|_{1}$ and $\| \cdot \|_{2}$ be two *equivalent* [[Norms|norms]] on the [[Vector Spaces|vector space]] $V$, meaning there exists $0 < A \le B$ such that for all $\vecbf{v} \in V$,
> $$A\| \vecbf{v} \|_{1} \le \| \vecbf{v} \|_{2} \le B\| \vecbf{v} \|_{1}.$$
> Suppose a [[Sequences|sequence]] $( \vecbf{a_{n}} )$ [[Metric Sequence Convergence|converges]] to $\vecbf{\lambda} \in V$ in the [[Metric Spaces|metric space]] [[Norms#^induced-metrics|induced]] by $\| \cdot \|_{1}$, meaning for all $\varepsilon/B > 0$, there exists $N \in \N$ such that for all $n \ge N$,
> $$\begin{align}
> 	d_{1}(\vecbf{a_{n}}, \vecbf{\lambda}) &< \dfrac{\varepsilon}{B} \\
> 	\| \vecbf{a_{n}} - \vecbf{\lambda} \|_{1} &< \dfrac{\varepsilon}{B} \\
> 	\| \vecbf{a_{n}} - \vecbf{\lambda} \|_{2} \le B\| \vecbf{a_{n}} - \vecbf{\lambda} \|_{1} &< \varepsilon \\
> 	d_{2}(\vecbf{a_{n}}, \vecbf{\lambda}) &< \varepsilon. \\
> \end{align}$$
> Thus, $( \vecbf{a_{n}} )$ [[Metric Sequence Convergence|converges]] to $\vecbf{\lambda}$ in the [[Metric Spaces|metric space]] [[Norms#^induced-metrics|induced]] by $\| \cdot \|_{2}$ as well.
^convergence