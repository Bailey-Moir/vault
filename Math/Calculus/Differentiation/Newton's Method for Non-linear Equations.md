---
tags:
  - atom
  - math
---
**A root-finding algorithm for non-linear functions**, where an initial approximation of a root ($x_0$) is used to generate an increasingly better approximation. This initial guess is chosen such that $f'(x_0) \ne 0$. A tolerance is often used to determine when to stop iterating: $\left| x_{n+1} - x_n \right| < \varepsilon$ and or $\left|f(x_n)\right| < \varepsilon$.
This has many applications, but notably, it can be used to find approximations for unknown [[Math/Discrete/Set Theory/Functions/Inverse Functions|inverse functions]] such as $\ln\square$ from $e^\square$ or $\sqrt\square{}$ from $\square^2$.
This method may fail if:
- $\exists n, f'(x_n) = 0$
- It overlooks a root and tries to converge on a different root.
- It does not converge (e.g. $\sqrt[3]{x}$)
![240|center](newtons-method.excalidraw)
$$\Large \textcolor{orange}{x_{n+1}} = \textcolor{green}{x_n} - \dfrac{f(\textcolor{green}{x_n})}{f'(\textcolor{green}{x_n})}, \:\:\:\:\:\: \normalsize f'(\textcolor{green}{x_n}) \ne 0 $$
$$\tiny \begin{array}{c}
\text{Derived from}\\
f'(\textcolor{green}{x_n}) = \dfrac{f(\textcolor{green}{x_n}) - 0}{\textcolor{green}{x_n} - \textcolor{orange}{x_{n+1}}}
\end{array}$$
```rust 
    fn my_sqrt(n: f64) -> f64 {
        let mut x = n; // inital guess is also n
        
        while x*x - n > 0.001 { x = 0.5*(x + n/x); }

        return x;
    }
```