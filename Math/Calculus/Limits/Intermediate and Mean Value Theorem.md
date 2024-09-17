---
tags:
  - math
  - atom
---
![800|center](mean-value-theorem.excalidraw)
Suppose $f(x)$ is continuous on $\left[a,b\right]$. The intermediate value theorem states that for every number in $\left(f(a),f(b)\right)$, there exists an input in $(a,b)$ that gives it. 

If the function is also [[Differentiability|differentiable]] on $\left(a,b\right)$, then the mean value theorem states that there exists at least one point in $\left(a,b\right)$ where the derivative matches the slope of the secant passing through $a$ and $b$.

|           | IVT                                                                                   | MVT                                                                               |
| --------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Condition | $f \in \mathcal{C}(\left[a,b\right])$                                                 | $f \in \mathcal{C}(\left[a,b\right])$,<br>$f \text{ is differentiable on } (a,b)$ |
| Theorem   | $\forall N \in \left( f(a),f(b) \right), \exists c \in \left( a,b \right) : f(c) = N$ | $\exists c \in \left(a,b\right) : f'(c) = \dfrac{f(b) - f(a)}{b - a}$             |
