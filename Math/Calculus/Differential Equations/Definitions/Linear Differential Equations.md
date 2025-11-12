---
tags:
  - atom
  - math
---
A *linear differential equation* is a [[Differential Equations|DE]] that can be written in the form
$$ a_n(t)\dfrac{d^ny}{{dt}^n} +  a_{n-1}(t)\dfrac{d^{n-1}y}{{dt}^{n-1}} + \dots + a_1(t) \dfrac{dy}{dt} + a_0(t)y = f(t),$$
where $a_n(t)$, $a_{n-1}(t)$, $\dots$, $a_1(t)$, $a_0(t)$ and $f(t)$ depend only on the [[Explanatory and Response Variables|independent variable]] $t$.

> [!formal definition]-
> A [[Differential Equations|DE]] is *linear* iff 
> - the [[Explanatory and Response Variables|dependent variable]] ($y$) and it's derivatives ($\frac{dy}{dt}$, $\frac{d^2y}{{dt}^2}$, $\dots$) only occur to the first power, and 
> - coefficients of the [[Explanatory and Response Variables|dependent variable]] and its derivatives do not involve the [[Explanatory and Response Variables|dependent variable]].

> [!theorem] If $a_{0}(t),\dots,a_{n}(t)$ and $f(t)$ are [[Continuity|continuous]] on an [[Intervals|open interval]] $I$, and $\exists i,\exists t \in I, a_{i}(t)\ne 0$, then a solution exists.