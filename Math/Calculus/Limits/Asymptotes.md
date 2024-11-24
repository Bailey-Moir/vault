---
tags:
  - atom
  - math
---
# Vertical Asymtote
A *vertical asymptote* occurs at $x=a$ on $f$ iff $\displaystyle\lim_{x\to a^\pm} f(x) = \pm\infty$ (where the $\pm$ are unlinked).

# Horizontal Asymtote
A horizontal asymtote occurs  at $f(x) = a$ on $f$ iff $\displaystyle\lim_{x\to\pm\infty} f(x) = a$.

# Oblique Asymtote
An oblique asymtote occurs on the line $y=ax+b$ if $\displaystyle\lim_{x\to\pm\infty} \left[ f(x) - (ax + b) \right] = 0$

If $f$ is a [[Types of Functions|rational function]] where the degree of the numerator exceeds the degree of the denominator by one, then an oblique asymtote will be present. 
$$\begin{array}{c}
	\begin{align*}
		f(x) &= \dfrac{P(x)}{Q(x)} \hspace{2em}\text{s.t. } \text{deg}(P) = \text{deg}(Q) + 1 \\
		&= (ax + b) + \dfrac{R(x)}{Q(x)} \\
	\end{align*} \\
	\displaystyle \lim_{x\to\pm\infty} \left[ f(x) - (ax-b) \right] = \lim_{x\to\pm\infty} \dfrac{R(x)}{Q(x)} = 0 \hspace{1em}(1) 
\end{array}$$
\[$(1)$ [[Rational Limits at Infinity]]\]