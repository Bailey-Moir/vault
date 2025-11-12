---
tags:
  - atom
  - math
---
*Modified Euler's method* is [[Euler's Method|Euler's method]], except the slope used is the average of the current slope and the slope one step ahead.
$$y_{n+1} = y_{n} + \dfrac{k_{1}+k_{2}}{2}h$$
where $k_{1} = f(t_{n},y_{n}))$ and $k_{2}$ = $f(t_{n+1},y_{n+1}^*)$, with $y^*$ being the height given by normal [[Euler's Method|Euler's method]].

> [!-] This is $\mathcal{O}(h^2)$[^1].

[^1]: [[Landua's Big Oh Notation]]
