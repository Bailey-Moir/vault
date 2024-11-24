---
tags:
  - atom
  - math
---
$$ \int \dfrac{1}{ax^2 + bx + c} \, dx $$
When given equations in this form, you can complete the square inside the denominator, and perform a $u$-sub like so:
$$\begin{array}{l}
	\displaystyle \dfrac{1}{\gamma} \int \dfrac{1}{\left( x - \alpha \right)^2 + \beta} \, dx \\
	\begin{align*}
		\displaystyle \text{let } u &= x - \alpha \\
		\displaystyle u' &= 1 \\
	\end{align*} \\
	\displaystyle \dfrac{1}{\gamma} \int \dfrac{1}{u^2 + \beta} \, du \\
\end{array}$$
The [[Inverse Trigonometric Integration Identities|following formula]] can then be used:
$$\begin{array}{c}
	\displaystyle \int \dfrac{1}{x^2 + a^2} = \dfrac{1}{a} \tan^{-1}\left(\dfrac{x}{a}\right) + c \\
	\tiny \color{gray} \left( \dfrac{1}{\beta \gamma} \tan^{-1}\left(\dfrac{x - \alpha}{\beta}\right) + c \right) \\
\end{array}$$
**Note: completing the square like this can be used with all of the [[Inverse Trigonometric Integration Identities|inverse trigonometric integration identities]]**

> [!proof]- Full Formula with Derivation
> $$\begin{array}{l}
> 	\displaystyle \int \dfrac{1}{ax^2 + bx + c} \, dx \\
> 	\displaystyle \int \dfrac{1}{a \left( x^2 + \dfrac{b}{a}x \right) + c } \, dx \\
> 	\displaystyle \int \dfrac{1}{a \left( x + \dfrac{b}{2a} \right)^2 + c - \dfrac{b^2}{4a} } \, dx \\
> 	\displaystyle \text{let } u = x + \dfrac{b}{2a} \\
> 	\displaystyle \phantom{\text{let }} u' = 1 \\
> 	\displaystyle \int \dfrac{1}{au^2 + \left( c - \dfrac{b^2}{4a} \right) } \, du \\
> 	\displaystyle \begin{align*}
> 	\displaystyle 	\text{let } u &= \dfrac{1}{\sqrt{a}}\sqrt{c - \dfrac{b^2}{4a}}\theta \\
> 	\displaystyle 	du &=  \dfrac{1}{\sqrt{a}}\sqrt{c - \dfrac{b^2}{4a}} \, d\theta
> 	\displaystyle \end{align*} \\
> 	\displaystyle \dfrac{1}{c - \dfrac{b^2}{4a}} \int \dfrac{1}{\theta^2 + 1} \, du \\
> 	\displaystyle \dfrac{1}{\sqrt{ac - \dfrac{b^2}{4}}} \int \dfrac{1}{\theta^2 + 1} \, d\theta \\
> 	\displaystyle \dfrac{1}{\sqrt{ac - \dfrac{b^2}{4}}} \tan^{-1} \theta + c \\
> 	\displaystyle \dfrac{1}{\sqrt{ac - \dfrac{b^2}{4}}} \tan^{-1} \left( \dfrac{\sqrt{a}}{\sqrt{c - \dfrac{b^2}{4a}}} u \right) + c \\
> 	\displaystyle \dfrac{1}{\sqrt{ac - \dfrac{b^2}{4}}} \tan^{-1} \left( \dfrac{x + \dfrac{b}{2a}}{\sqrt{\dfrac{c}{a} - \left(\dfrac{b}{2a}\right)^2 }} \right) + c \\
> 	\displaystyle \dfrac{2}{\sqrt{4ac - b^2}} \tan^{-1} \left( \dfrac{2ax + b}{\sqrt{4ac - b^2}} \right) + c \\
> \end{array}$$
> $$ \large \displaystyle \dfrac{2}{\sqrt{-\Delta}} \tan^{-1} \left( \dfrac{2ax + b}{\sqrt{-\Delta}} \right) + c $$
