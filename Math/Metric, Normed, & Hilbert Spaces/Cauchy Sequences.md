---
tags:
  - atom
  - math
---
A [[Sequences|sequence]] $(a_{n}) : \N \to M$ for some [[Metric Spaces|metric space]] $M$ is called a *Cauchy sequence* iff
$$\forall \varepsilon > 0, \exists N \in \N : \forall m,n \ge N, d(a_{n}, a_{m}) < \varepsilon$$
> [!theorem]- [[Metric Sequence Convergence|Convergent]] $\to$ *Cauchy*.
> Suppose $\left( a_{n} \right) : \N \to M$ [[Metric Sequence Convergence|converges]] to $\lambda$, meaning
> $$\forall \varepsilon > 0, \exists N \in \N : \forall n \ge N, d(a_{n},\lambda) < \varepsilon.$$
> Then for all $\varepsilon/2 > 0$, there exists $N \in \N$ such that for all $m,n \ge N$,
> $$\begin{array}{ccc}
> 	d(a_{m},L) < \dfrac{\varepsilon}{2} & \land & d(a_{n}, L) < \dfrac{\varepsilon}{2}.
> \end{array}$$
> Thus,
> $$\begin{align}
> 	d(a_{m}, L) + d(a_{n}, L) &< \varepsilon, \\
> 	d(a_{m}, a_{n}) \le d(a_{m}, L) + d(L, a_{n}) &< \varepsilon. && \triangle\le \\
> \end{align}$$
> This gives that for all $\varepsilon > 0$, there exists $N \in \N$ such that for all $m,n \ge N$, $d(a_{m}, a_{n}) < \varepsilon$. Thus, $\left( a_{n} \right)$ is a *Cauchy sequence*.
^convergent-to-cauchy

> [!theorem]- In $\R$, *Cauchy* $\to$ [[Metric Sequence Convergence|Convergent]].
> Suppose $\left( a_{n} \right) : \N \to \R$ is a *Cauchy sequence*.
> For $\varepsilon = 1$, there then exists $N \in \N$ such that for all $n \ge N$,
> $$\begin{array}{c}
> 	\left| a_{n} - a_{N} \right| < 1 \\
> 	- 1< a_{n} - a_{N} < 1 \\
> 	a_{N} - 1< a_{n} < a_{N} + 1. \\
> \end{array}$$
> Thus, $\left( a_{n} \right)$ is eventually [[Bounded Sequences|bounded]], meaning it is [[Bounded Sets|bounded]], as there are finitely many points before $N$.
> 
> Therefore, by [[Bolzano-Weierstrass|Bolzano-Weierstrass]], some subsequence $\left( a_{n(k)} \right)_{k=0}^\infty$ [[Metric Sequence Convergence|converges]] to some $\lambda$.
> 
> Let $\varepsilon > 0$ be given.
> By the [[Metric Sequence Convergence|convergence]] of $\left( a_{n(k)} \right)_{k=0}^\infty$, there exists $K \in \N$ such that for all $k \ge K$,
> $$\left| a_{n(k)} - \lambda \right| < \dfrac{\varepsilon}{2}.$$
> Since $\left( a_{n} \right)$ is *Cauchy*, there exists $N \in \N$ such that for all $m, n \ge N$,
> $$ \left| a_{m} - a_{n} \right| < \dfrac{\varepsilon}{2}. $$
> Let $k \ge K$ such that $n(k) \ge N$. Then for all $n \ge N$,
> $$\begin{array}{c}
> 	\begin{array}{ccc}
> 		\left| a_{n} - a_{n(k)} \right| < \dfrac{\varepsilon}{2} 
> 		& \land &
> 		\left| a_{n(k)} - \lambda \right| < \dfrac{\varepsilon}{2}.
> 	\end{array} \\
> 	\to \left| a_{n} - \lambda \right| \le \left| a_{n} - a_{n(k)} \right| + \left| a_{n(k)} - \lambda \right| < \varepsilon. \phantom{\to}
> \end{array}$$
> Thus, $\left( a_{n} \right)$ is [[Metric Sequence Convergence|convergent]].
^R-cauchy-to-convergent

> [!proof]- My Shitty Proof
> Suppose $\left( x_{n} \right) : \N \to \R$ is a *Cauchy sequence*, meaning
> $$\forall \varepsilon > 0, \exists N \in \N : \forall m,n \ge N, d(x_{m}, x_{n}) < \varepsilon.$$
> Let $\varepsilon > 0$ be given. For all $k \in \N$, there then exists $N_{k} \in \N$ such that for all $n \ge N_{k}$, $d(x_{N_{k}}, x_{n}) < \dfrac{\varepsilon}{2^k}$. 
> We will [[Induction|inductively]] restrict $N_{k+1} > N_{k}$ for all $k \in \N$.
> 
> Let
> $$\begin{align}
> 	a_{n} &= \max \left\{ x_{N_{k}} - \dfrac{\varepsilon}{2^{k}} : k \in \N_{\le n} \right\}, \\
> 	b_{n} &= \min \left\{ x_{N_{k}} + \dfrac{\varepsilon}{2^{k}} : k \in \N_{\le n} \right\}.
> \end{align}$$
> > [!lemma]- $\forall k \in \N,$ <ul> <li>$\{ x_{n} \}_{n=N_{k}}^\infty \subseteq \left( a_{k},b_{k} \right)$</li><li>$b_{k}-a_{k} \le \dfrac{b_{0}-a_{0}}{2^k}$</li><li>$(a_{k+1},b_{k+1}) \subseteq (a_{k},b_{k})$.</li></ul>
> > **Base Case**
> > $\{ x_{n} \}_{n=N_{0}}^\infty \subseteq \left( x_{N_{0}}-\varepsilon, x_{N_{0}}+\varepsilon \right) = \left( a_{0},b_{0} \right)$.
> > $b_{0}-a_{0} \le \dfrac{b_{0}-a_{0}}{2_{0}} = b_{0}-a_{0}$.
> > Note
> > $$\begin{align}
> > 	b_{0} - a_{0}
> > 	&= \left( x_{N_{0}} + \varepsilon \right) - \left( x_{N_{0}} - \varepsilon \right) \\
> > 	&= 2\varepsilon. \\
> > \end{align}$$
> > **Induction Step**
> > Suppose $\{ x_{n} \}_{n=N_{k}}^\infty \subseteq \left( a_{k},b_{k} \right)$ and $b_{k}-a_{k} \le \dfrac{b_{0}-a_{0}}{2^k}$.
> > 
> > For all $n \ge N_{k+1}$, $d(x_{N_{k+1}}, x_{n}) < \dfrac{\varepsilon}{2^{k+1}}$, meaning 
> > $$ \{ x_{n} \}_{n=N_{k+1}}^\infty \subseteq \left( x_{N_{k+1}}-\dfrac{\varepsilon}{2^{k+1}}, x_{N_{k+1}}+\dfrac{\varepsilon}{2^{k+1}} \right). $$
> > Note that
> > $$\begin{align}
> > 	\left( x_{N_{k+1}}+\dfrac{\varepsilon}{2^{k+1}} \right) - \left( x_{N_{k+1}}-\dfrac{\varepsilon}{2^{k+1}} \right)
> > 	&= \dfrac{2\varepsilon}{2^{k+1}} \\
> > 	&= \dfrac{b_{0} - a_{0}}{2^{k+1}}.
> > \end{align}$$
> > Thus,
> > $$\begin{align}
> > 	\{ x_{n} \}_{n=N_{k}}^\infty \cap \{ x_{n} \}_{n=N_{k+1}}^\infty &\subseteq \left( a_{k}, b_{k} \right) \cap \left( x_{N_{k+1}}-\dfrac{\varepsilon}{2^{k+1}}, x_{N_{k+1}}+\dfrac{\varepsilon}{2^{k+1}} \right) \\
> > 	\{ x_{n} \}_{n=N_{k+1}}^\infty &\subseteq \left( \max \left\{ a_{k}, x_{N_{k+1}} - \dfrac{\varepsilon}{2^{k+1}} \right\}, \min \left\{ b_{k}, x_{N_{k+1}} + \dfrac{\varepsilon}{2^{k+1}} \right\} \right) \\
> > 	&\subseteq \left( a_{k+1}, b_{k+1} \right). \\
> > \end{align}$$
> > By the way we defined $a_{k+1}$ and $b_{k+1}$, 
> > - $\left( a_{k+1},b_{k+1} \right) \subseteq \left( x_{N_{k+1}}-\dfrac{\varepsilon}{2^{k+1}}, x_{N_{k+1}}+\dfrac{\varepsilon}{2^{k+1}} \right)$, meaning $b_{k+1} - a_{k + 1} \le \dfrac{b_{0} - a_{0}}{2^{k+1}}$
> > - $\left( a_{k+1},b_{k+1} \right) \subseteq \left( a_{k},b_{k} \right)$.
> > 
> > Further, by the way we defined $a_{k+1}$ and $b_{k+1}$, $\left( a_{k+1},b_{k+1} \right) \subseteq \left( a_{k},b_{k} \right)$.
> 
> Thus, $\left( a_{n} \right)$ and $\left( b_{n} \right)$ [[Metric Sequence Convergence|converge]] by [[Monotone Convergence Theorem|MCT]].
> 
> Further, since $b_{k}-a_{k} \le \dfrac{b_{0}-a_{0}}{2^k}$ for all $k \in \N$,
> $$\begin{align}
> 	\lim_{ k \to \infty } \left( b_{k} - a_{k} \right) &= \lim_{ k \to \infty } \dfrac{b_{0}-a_{0}}{2^k} \\
> 	\lim_{ k \to \infty } b_{k} - \lim_{ k \to \infty } a_{k} &= 0 \\
> 	\lim_{ k \to \infty } b_{k} &= \lim_{ k \to \infty } a_{k} = \lambda.
> \end{align}$$
> 
> Let $\varepsilon > 0$ be given. Let $k \in \N$ such that $\left| b_{k} - a_{k} \right| < \varepsilon$ by the [[Metric Sequence Convergence|convergence]] of $\left( b_{k} - a_{k} \right)$. Then for all $n \ge N_{k}$,
> $$\begin{array}{c}
> 	x_{n} \in \left( a_{k},b_{k} \right) \\
> 	\to \left| x_{n} - \lambda \right| <\varepsilon. && \lambda \in \left( a_{k},b_{k} \right) \\
> \end{array}$$
> Thus, $\lim x_{n} = \lambda$. $\square$