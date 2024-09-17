---
tags:
  - atom
  - math
---
Defined as a function of the differential operator. It is helpful to consider differentiation as an abstract operation, accepting a function and returning another. *Differential operators* are operators, and therefore must be followed by an expression to operator on.
$$ D^n \equiv \dfrac{d^n}{dx^n} $$
```sheet
|               | - | Distributive Law       | Commutative Law                    | Index Law                             |
| ------------- | - | ---------------------- | ---------------------------------- | ------------------------------------- |
| Variables     | - | $m(a+b) = ma + mb$     | $ab = ba$                          | $a^m \times a^n = a^\left(m+n\right)$ |
| $D$-operators | - | $D(u+v) = D\:u + D\;v$ | $D(uv) \textcolor{red}{\ne} uD\:v$ | $D^m\left( D^n \left( u \right)\right) = D^{\left(m+n\right)}\:u$ |
```

> [!example]-
> $$\begin{array}{l}
> 	\text{Solve }\dfrac{d^2y}{dx^2} + 2\dfrac{dy}{dx} + y = 0 \\
> 	\\
> 	\begin{align*}
> 		0&= D^2\:y - 2D\:y + y \\
> 		&= (D^2 - 2D + 1)\:y \\
> 		&= (D-1)^2\:y =(D-1)\left(\phantom{\int}\hspace{-1em} (D-1)\:y \right) \\ 
> 		\text{let } u = (D-1)\:y \\
> 		&= (D-1)\:u \\
> 	\end{align*}\\
> 	\begin{aligned}
> 		&\begin{aligned}
	> 		\therefore \dfrac{du}{dx} &= u \\
	> 		u &= Ae^x && \hspace{6.6em}(1) \\
> 		\end{aligned}\hspace{2.1em}& \\
> 		&\begin{aligned}
	> 		\therefore (D-1)\:y &= Ae^x \\
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