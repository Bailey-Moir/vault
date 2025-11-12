---
tags:
  - atom
  - math
---
Suppose $f$ is [[Integrability|integrable]] on $\left[ a,b \right]$, and define
$$F(x) = \int_{a}^x f(t) \, dt.$$
Then $F$ is [[Continuity|continuous]] on $\left[ a,b \right]$.

> [!proof]-
> Suppose $f$ is [[Bounded Sets|bounded]] and [[Integrability|integrable]] on $\left[ a,b \right]$. Let $M \in \R^+$ be such that
> $$\begin{align}
> 	\left| f(x) \right| \le M && \forall x \in \left[ a,b \right]
> \end{align}$$
> If $h > 0$, then
> $$\begin{align}
> 	F(c+h) - F(c) &= \int_{a}^{c+h} f(t) \, dt - \int_{a}^c f(t) \, dt \\
> 	&= \int_{a}^{c+h} f(t) \, dt + \int_{c}^a f(t) \, dt \\
> 	&= \int_{c}^{c+h} f(t) \, dt. && (1) \\
> \end{align}$$
> \[$(1)$ [[Splitting Bounds]]\]
> 
> Then by an unknown theorem,
> $$-Mh \le \int_{c}^{c+h} f(t) \, dt \le Mh$$
> If $h < 0$, we get
> $$-M(-h) \le \int_{c}^{c+h} f(t) \, dt \le M(-h)$$
> Thus,
> $$\left| F(c+h) - F(c) \right| \le M\left| h \right|,$$
> meh