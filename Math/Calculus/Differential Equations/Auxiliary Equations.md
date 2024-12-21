---
tags:
  - atom
  - math
---
The solution of [[Linear Differential Equations|linear]] [[Homogeneous Differential Equations|homogeneous]] constant coefficient DEs rely upon the *auxiliary equation*. 
$$a_n\dfrac{d^ny}{{dx}^n} + a_{n-1}\dfrac{d^{n-1}y}{{dx}^{n-1}} + \dots + a_1\dfrac{dy}{dx} + a_0y = 0 \hspace{2em}\ni \forall n, a_n \text{ is constant}$$
will have an *auxiliary equation* of
$$a_nm^n + a_{n-1}m^{n-1} + \dots + a_1m + a_0 = 0 \hspace{2em}\ni \forall n, a_n \text{ is constant}$$
The roots of this *auxiliary equation*, $m_1, m_2, \dots, m_n$, are used to form the **general solution**. The dampening names below only apply when $\text{Re}(m_1),\text{Re}(m_2) < 0$, which exception of **simple harmonic motion**. *Furthermore, for the below [[Statements and Propositions|statements]]/[[Argument|arguments]], let them be denoted by $p$, $q$, $r$, and $s$ for the sake of the proofs.*
![600|center](auxiliary-equation-graphs.excalidraw)
- **Over-damped**: $y = C_1e^{m_1x} + C_2e^{m_2x}$ if $m_1 \ne m_2$.
> [!proof]- $p \iff \T$
> You can prove this [[Argument|argument]] by [[Splitting Second Order DEs|splitting the second order DE]] (or with [[Differential Operators|differential operators]]). Note that this equation is set up such that $\alpha$ and $\beta$ are the roots of the *auxiliary* such that $\alpha \ne \beta$ (thus assuming the [[Argument|premise]]).
> $$\begin{align*}
> 	y'' + (-\alpha-\beta)y' + \alpha\beta y &= 0 \\
> 	y'' - \alpha y' - \beta y' + \alpha\beta y &= 0 \\
> 	(y' - \alpha y)' - \beta(y' - \alpha y) &= 0 \\
> \end{align*}$$
> Let $z = y' - \alpha y$
> $$z' - \beta z = 0$$
> First you can solve $z$ by [[Integrating Factor Method|integrating factor method]]:
> $$\begin{align*}
> 	e^{\beta x}z' - \beta e^{-\beta x}z &= 0e^{-\beta x} \\
> 	\dfrac{d}{dx}\left( e^{-\beta x}z \right) &= 0 \\
> 	e^{-\beta x}z &= \int 0 \, dx \\
> 	z &= Ce^{\beta x} \\
> \end{align*}$$
> Now you can substitute this into the other DE, and again apply [[Integrating Factor Method|integrating factor method]].
> $$\begin{align*}
> 		y' - \alpha y &= Ce^{\beta x} \\
> 		e^{-\alpha x}y' - \alpha e^{-\alpha x}y &= Ce^{(\beta - \alpha) x} \\
> 		\dfrac{d}{dx}\left( e^{-\alpha x}y \right) &= Ce^{(\beta - \alpha) x} \\
> 		e^{-\alpha x}y &= \int Ce^{(\beta - \alpha ) x} \, dx \\
> 		&= C_1(\alpha + \beta)e^{(\beta - \alpha)x} + C_2\\
> 		y &= C_1(\alpha + \beta)e^{\beta x} + C_2e^{\alpha x}\\
> \end{align*}$$
> Since $C_1$ can be any arbitrary constant, $\alpha - \beta$ can be absorbed into it.
> $$ y = C_1e^{\beta x} + C_2e^{\alpha x} $$
> Since $\alpha$ and $\beta$ are synonymous with $m_1$, $m_2$ (as they both represent the roots),
> $$ y = C_1e^{m_1x} + C_2e^{m_2x} $$
> Thus the [[Argument|argument]] $p$ is [[Argument|valid]].
- **Critically-damped**: $y = C_1e^{mx} + C_2xe^{mx}$ if $m_1 = m_2$
> [!proof]- $q \iff \T$
> You can prove this [[Argument|argument]] by [[Splitting Second Order DEs|splitting the second order DE]] (or with [[Differential Operators|differential operators]]). Note this equation is set up such that $\alpha$ is the repeated root of the auxiliary (thus assuming the [[Argument|premise]]).
> $$\begin{align*}
> 	y'' - 2\alpha y' + \alpha^2y &= 0 \\
> 	y'' - \alpha y' - \alpha y' + \alpha^2y &= 0 \\
> 	(y' - \alpha y)' - \alpha(y' - \alpha y) &= 0 \\
> \end{align*}$$
> Let $z = y' - \alpha y$
> $$z' - \alpha z = 0$$
> First you can solve $z$ by [[Integrating Factor Method|integrating factor method]]:
> $$\begin{align*}
> 	e^{\alpha x}z' - \alpha e^{-\alpha x}z &= 0e^{-\alpha x} \\
> 	\dfrac{d}{dx}\left( e^{-\alpha x}z \right) &= 0 \\
> 	e^{-\alpha x}z &= \int 0 \, dx \\
> 	z &= Ce^{\alpha x} \\
> \end{align*}$$
> Now you can substitute this into the other DE, and again apply [[Integrating Factor Method|integrating factor method]].
> $$\begin{align*}
> 		y' - \alpha y &= Ce^{\alpha x} \\
> 		e^{-\alpha x}y' - \alpha e^{-\alpha x}y &= Ce^{0x} \\
> 		\dfrac{d}{dx}\left( e^{-\alpha x}y \right) &= C \\
> 		e^{-\alpha x}y &= \int C \, dx  && \text{(1)}\\
> 		&= C_1x + C_2\\
> 		y &= C_1xe^{\alpha x} + C_2e^{\alpha x}\\
> \end{align*}$$
> $(1)$ This is the key difference between $p$ and $q$, as exponentials integrate very differently than constants.
> Since $\alpha$ is synonymous with $m$ (as they both represent the repeated root),
> $$ y = C_1e^{mx} + C_2xe^{mx} $$
> Thus the [[Argument|argument]] $q$ is [[Argument|valid]].
- **Under-damped**: $y = e^{ax}(C_1\cos(bx) + C_2\sin(bx))$ if $m_1 = \overline{m_2}$, where $a = \text{Re}(m_1)$ and $b = \text{Im}(m_1) \ne 0$
> [!proof]- $p \implies r$
> The [[Argument|premise]] for $r$ [[Logical Implication|logically implies]] the [[Argument|premise]] for $p$, as $m_1 = \overline{m_2} \land \text{Im}(m_1) \ne 0 \implies m_1 \ne m_2$. Thus, assuming the [[Argument|premise]] for $r$, $p$ applies.
> $$\begin{align*}
> 	y &= C_1e^{(a+bi)x} + C_2e^{(a-bi)x} \\
> 	&= C_1e^{ax} e^{bxi} + C_2e^{ax}e^{-bxi} \\
> 	&= e^{ax} \left( C_1e^{(bx)i} + C_2e^{-(bx)i} \right) \\
> 	&= e^{ax} \left( C_1(\cos bx + i\sin bx) + C_2(\cos -bx + i\sin -bx) \right) && (1) \\
> 	&= e^{ax} \left( C_1(\cos bx + i\sin bx) + C_2(\cos bx - i\sin bx) \right) && (2) \\
> 	&= e^{ax} \left( (C_1 + C_2)\cos bx + (C_1 - C_2)i\sin bx \right)\\
> \end{align*}$$
> Note $C_1 + C_2$ and $C_1 - C_2$ can be any two complex numbers, so I will rename them: $C_1 + C_2$ will become $C_1$ and $(C_1 - C_2)i$ will become $C_2$.
> $$y = e^{ax} \left( C_1\cos bx + C_2\sin bx \right) $$
> Thus $p \implies r$.
> \[$(1)$ [[De Moivre's Formula]], $(2)$ [[Even and Odd Functions]]\]
- **Simple Harmonic Motion**: $y = C_1\cos(bx) + C_2\sin(bx)$ if $m_1 = -m_2 = bi$
> [!proof]- $r \implies s$
> The [[Argument|premise]] for $s$ [[Logical Implication|logically implies]] the [[Argument|premise]] for $r$, as $m_1 = bi \land m_2 = -b_i \implies m_1 = \overline{m_2}$. Thus, assuming the [[Argument|premise]] for $s$, $r$ applies.
> $$\begin{align*}
> 	y &= e^{ax} \left( C_1\cos bx + C_2i\sin bx \right)\\
> 	&= e^{0x} \left( C_1\cos bx + C_2i\sin bx \right) && a = 0 \\
> 	&= C_1\cos bx + C_2\sin bx \\
> \end{align*}$$
> Thus $r \implies s$.
