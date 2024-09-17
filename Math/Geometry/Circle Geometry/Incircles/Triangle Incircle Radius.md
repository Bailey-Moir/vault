---
tags:
  - atom
  - math
---
$$ r = \sqrt{\dfrac{(s-a)(s-b)(s-c)}{s}} $$

> [!proof] 
> Plugging in the half angles of the [[Law of Cotangents|law of cotangents]] ($\frac{1}{2}\alpha$, $\frac{1}{2}\beta$, and $\frac{1}{2}\gamma$) into the [triple cotangent identity](https://en.wikipedia.org/wiki/Proofs_of_trigonometric_identities#Miscellaneous_%E2%80%93_the_triple_cotangent_identity) (which can be proven with the [general addition formula](https://en.wikipedia.org/wiki/List_of_trigonometric_identities#Tangents_and_cotangents_of_sums)) gives:
> $$ \cot{\frac{1}{2}\alpha} \cot{\frac{1}{2}\beta} \cot{\frac{1}{2}\gamma} = \cot{\frac{1}{2}\alpha} + \cot{\frac{1}{2}\beta} + \cot{\frac{1}{2}\gamma}$$
> Applying the [[Law of Cotangents|law of cotangents]] then gives:
> $$\begin{align*}
> 	\dfrac{s-a}{r}\dfrac{s-b}{r}\dfrac{s-c}{r} &= \dfrac{s-a}{r} + \dfrac{s-b}{r} + \dfrac{s-c}{r} \\
> 	\dfrac{(s-a)(s-b)(s-c)}{r^3} &= \dfrac{3s-2s}{r} \\
> 	(s-a)(s-b)(s-c) &= sr^2 \\
> 	r &= \sqrt{\dfrac{(s-a)(s-b)(s-c)}{s}} \hspace{1em}\square \\
> \end{align*}$$
> \[[[Semiperimeter]]\]