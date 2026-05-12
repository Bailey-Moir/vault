---
tags:
  - atom
  - math
---
Let $F$ be a [[Fields|field]], and let $\alpha_{1},\dots,\alpha_{n}$ be elements of some [[Subfields#^extension-field|extension field]] $E$ of $F$.
We define $F(\alpha_{1},\dots,\alpha_{n})$ to be the smallest [[Subfields|subfield]] of $E$ that contains $F$ and the set $\{ \alpha_{1},\dots,\alpha_{n}\}$.

> [!note] $F$ is a [[Subfields|subfield]] of $F(\alpha_{1},\dots,\alpha_{n})$ which is a [[Subfields|subfield]] of $E$.

> [!example]- $\Q(\sqrt{ 2 },\sqrt{ 3 }) = \Q(\sqrt{ 2 }+\sqrt{ 3 })$
> $\left( \supseteq \right)$
> $\sqrt{ 2 } + \sqrt{ 3 } \in \Q(\sqrt{ 2 },\sqrt{ 3 })$. Thus, by [[Maximal vs. Maximum|minimality]], $\Q(\sqrt{ 2 } + \sqrt{ 3 }) \subseteq \Q(\sqrt{ 2 },\sqrt{ 3 })$.
> 
> $\left( \subseteq \right)$
> Consider
> $$\begin{align}
> 	\left( \sqrt{ 2 } + \sqrt{ 3 } \right)^3
> 	&= 2\sqrt{ 2 } + 3(2)(\sqrt{ 3 }) + 3(\sqrt{ 2 })(3) + 3\sqrt{ 3 } \\
> 	&= 2\sqrt{ 2 } + 6\sqrt{ 3 } + 9\sqrt{ 2 } + 3\sqrt{ 3 } \\
> 	&= 11\sqrt{ 2 } + 9\sqrt{ 3 } \in \Q(\sqrt{ 2 } + \sqrt{ 3 }) \\
> \end{align}$$
> Note the vectors $\sqrt{ 2 } + \sqrt{ 3 }$ and $11\sqrt{ 2 } + \sqrt{ 9 }$ in $\Q(\sqrt{ 2 } + \sqrt{ 3 })$ are [[Linear Independence|linearly independent]], so $\sqrt{ 2 },\sqrt{ 3 } \in \Q(\sqrt{ 2 } + \sqrt{ 3 })$.
> Thus, by [[Maximal vs. Maximum|minimality]], $\Q(\sqrt{ 2 },\sqrt{ 3 }) \subseteq \Q(\sqrt{ 2 }+\sqrt{ 3 })$
