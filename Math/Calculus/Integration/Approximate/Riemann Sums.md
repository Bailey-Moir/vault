---
tags:
  - math
  - atom
---
The most basic form of [[Approximate Integration|approximate integration]], used in [[Integration by First Principals|integration by first principles]].
![800|center](riemann-sums.excalidraw)
$$
\begin{align*}
	L_n &= {\tiny(x_1 - x_0)f(x_\textcolor{red}0) + \dots + (x_n + x_{n-1})f(x_\textcolor{red}{n-1})} &
	R_n &= {\tiny(x_1 - x_0)f(x_\textcolor{CornflowerBlue}1) + \dots + (x_n + x_{n-1})f(x_\textcolor{CornflowerBlue}n)} \\
	&= \sum_{i=1}^n (x_i-x_{i-1})f(x_\textcolor{red}{i-1}) & &= \sum_{i=1}^n (x_i-x_{i-1}) f(x_\textcolor{CornflowerBlue}{i})	
\end{align*}
$$
<iframe src="https://www.desmos.com/calculator/unto1kpcxt?embed" height="300" style="width:100%; margin-bottom: -20px;"></iframe>
