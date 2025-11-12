---
tags:
  - atom
  - math
---
*Integration by substitution* is the integration equivalent of the [[Differentiation Rules|chain rule]]. Note that if you change from $dx$ to $du$, $x$ can not be treated as a constant.
$$\int y\, dx = \int \dfrac{y}{\dfrac{du}{dx}} du$$
> [!example]-
> $$\begin{array}{l}
> 	\displaystyle\int \sqrt{ 2x + 1 } \, dx = \int \sqrt{ u } \, dx \\
> 	\dfrac{du}{dx} = 2 \\
> 	dx = \dfrac{du}{2} \\
> 	\displaystyle \int \sqrt{ u } \, dx = \int \sqrt{ u }\, \dfrac{du}{2} \\
> 	\displaystyle\phantom{\displaystyle \int \sqrt{ u } \, dx} = \int \dfrac{\sqrt{ u }}{2} du \\
> 	\phantom{\displaystyle \int \sqrt{ u } \, dx} = \dfrac{\sqrt{ u^3 }}{3} + c \\
> 	\phantom{\displaystyle \int \sqrt{ u } \, dx} = \dfrac{\sqrt{ (2x+1)^3 }}{3} + c \\
> \end{array}$$

# Reverse Chain Rule
The *reverse chain rule* is the reverse of the [[Differentiation Rules|chain rule]], derived directly from *integration by substitution*.
$$\int u'y\, dx = \int y \, du$$