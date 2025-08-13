---
tags:
  - atom
  - math
  - discrete
  - stats
---
![500|center](geometric-random-variable.excalidraw.md)
A *geometric random variable* $X \sim\text{Geom}(p)$ is a [[Random Variables|discrete random variable]] that counts the number of [[Independent Events|independent]] trials until the first success, where each trial is a [[Bernoulli Random Variables|Bernoulli random variable]] with probability $p$.
$$P(X=k) = p(1-p)^{k-1} \hspace{2em} \forall k \in \Z_{n+1}$$
# Mean of a Geometric Random Variable
$$\mu_{X} = \dfrac{1}{p}$$
> [!proof]-
> $$\begin{align*}
> 	\mu_{X} &= \sum_{k=1}^\infty kP(x=k) \\
> 	 &= \sum_{k=1}^\infty kp(1-p)^{k-1} \\
> 	 &= p\sum_{k=1}^\infty k(1-p)^{k-1} \\
> 	 &= -p\sum_{k=1}^\infty \dfrac{d}{dp} \left( (1-p)^{k} \right) \\
> 	 &= -p\dfrac{d}{dp}\sum_{k=1}^\infty (1-p)^{k} \\
> 	 &= -p\dfrac{d}{dp}\left( \dfrac{1-p}{1-(1-p)} \right) \\
> 	 &= -p\dfrac{d}{dp}\left( \dfrac{1-p}{p} \right) \\
> 	 &= -p\dfrac{d}{dp}\left( \dfrac{1}{p} - 1 \right) \\
> 	 &= -p\left( -\dfrac{1}{p^2} \right) \\
> 	 &= \dfrac{1}{p} \\
> \end{align*}$$
> \[[[Series]]\]

\[[[Mean of a Discrete Random Variable]]\]