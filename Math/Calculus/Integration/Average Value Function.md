---
tags:
  - math
  - atom
---
If $f \in \mathcal{C}(\left[ a,b \right])$[^1],
$$ \displaystyle f_{\text{avg}} = \dfrac{1}{b-a} \int_a^b f(x) \, dx $$
> [!proof]
> $$\begin{array}{l}
>	\begin{align*}
>		f_\text{avg} &= \lim_{n\to\infty} \sum_{i=1}^n \dfrac{1}{n} f(x_i) \\
>		&= \lim_{n\to\infty} \sum_{i=1}^n \dfrac{1}{n\Delta x} f(x_i) \Delta x \\
>		&= \lim_{n\to\infty} \sum_{i=1}^n \dfrac{1}{n\dfrac{b-a}{n}} f(x_i) \Delta x \\
>		&= \dfrac{1}{b-a} \lim_{n\to\infty} \sum_{i=1}^n f(x_i) \Delta x \\
>		&= \dfrac{1}{b-a} \int_a^b f(x) \, dx && (1) \\
>	\end{align*}
> \end{array}$$
> \[$(1)$ [[Integration by First Principals]]\]

[^1]: [[Math/Calculus/Limits/Continuity/Continuity]]
