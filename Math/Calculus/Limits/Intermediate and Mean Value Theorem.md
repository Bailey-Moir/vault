---
tags:
  - math
  - atom
---
![800|center](mean-value-theorem.excalidraw.md)
Suppose $f(x)$ is [[Definition of Continuity|continuous]] on $\left[a,b\right]$. The intermediate value theorem states that for every output in $\left(f(a),f(b)\right)$, there exists an input in $(a,b)$ that maps to it. 

If the function is also [[Differentiability|differentiable]] on $\left(a,b\right)$, then the mean value theorem states that there exists at least one point in $\left(a,b\right)$ where the derivative matches the slope of the secant passing through $a$ and $b$.

|            | IVT                                                                                   | MVT                                                                               |
| ---------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Premise    | $f \in \mathcal{C}(\left[a,b\right])$                                                 | $f \in \mathcal{C}(\left[a,b\right])$,<br>$f \text{ is differentiable on } (a,b)$ |
| Conclusion | $\forall N \in \left( f(a),f(b) \right), \exists c \in \left( a,b \right) : f(c) = N$ | $\exists c \in \left(a,b\right) : f'(c) = \dfrac{f(b) - f(a)}{b - a}$             |