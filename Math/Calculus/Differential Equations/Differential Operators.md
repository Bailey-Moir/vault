---
tags:
  - atom
  - math
---
The fact that $D \equiv\dfrac{d}{dx}$ is a [[Operators|linear operator]] can be leveraged to solve [[Differential Equations|DEs]] (e.g. using factorisation).

> [!example]-
> $$\begin{array}{l}
> 	\text{Solve }\dfrac{d^2y}{dx^2} + 2\dfrac{dy}{dx} + y = 0 \\
> 	\\
> 	\begin{align*}
> 		0&= D^2\:y - 2D\:y + y \\
> 		&= (D^2 - 2D + I)\:y \\
> 		&= (D-I)^2\:y =(D-I)\left(\phantom{\int}\hspace{-1em} (D-I)\:y \right) \\ 
> 		\text{let } u = (D-I)\:y \\
> 		&= (D-I)\:u \\
> 	\end{align*}\\
> 	\begin{aligned}
> 		&\begin{aligned}
> 		\therefore \dfrac{du}{dx} &= u \\
> 		u &= Ae^x && \hspace{6.6em}(1) \\
> 		\end{aligned}\hspace{2.1em}& \\
> 		&\begin{aligned}
> 		\therefore (D-I)\:y &= Ae^x \\
> 		\dfrac{dy}{dx} - y &= Ae^x \\
> 		\boldsymbol y &\boldsymbol{= (Ax + B)e^x} && (2) \\
> 		\end{aligned}
> 	\end{aligned} \\
> \end{array}$$
> \[$(1)$ [[Separation of Variables]], $(2)$ [[Integrating Factor Method]]\]

**Three useful formulae:**
1. $F(D)\:e^{ax} = e^{ax} F(a) \textcolor{gray}{\because D^n \: e^{ax} = a^ne^{ax}}$
2. $F(D)\:(e^{ax} f(x)) = e^{ax} F(D+a)\:f(x)$
3. $F(D^2) f(ax) = F(-a^2) f(ax) \text{ s.t. } f \in \left\{\sin, \cos\right\} \textcolor{gray}{\because D^2\:f(x) = -f(x)}$