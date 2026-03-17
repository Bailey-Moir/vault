---
tags:
  - atom
  - math
---
The *Jaccard similarity* between two [[Sets|sets]] is the [[Cardinality|cardinality]] of [[Unions & Intersections|intersection]] divided by that of their [[Unions & Intersections|union]] (the % of elements shared). The *Jaccard distance* is the complement of this,
$$d_{J}(A,B) = 1 - \dfrac{\left| A \cap B \right|}{\left| A \cup B \right| }.$$
*i.e. the % of elements not shared*

> [!theorem]- The *Jaccard distance* is a [[Metric Spaces|metric]] on any [[Classes|class]] of **finite** [[Sets|sets]].
> Let $X$ be a [[Classes|class]] of [[Sets|sets]].
> 
> (M1)
> $\left( \implies \right)$
> Suppose $d(A,B) = 0$ for some $A,B \in X$. Then
> $$\begin{align}
> 	d(A,B) = 1 - \dfrac{\left| A \cap B \right|}{\left| A \cup B \right| } &= 0 \\
> 	\dfrac{\left| A \cap B \right|}{\left| A \cup B \right| } &= 1 \\
> 	\left| A \cap B \right| &= \left| A \cup B \right|. \\
> \end{align}$$
> Thus, since $A,B$ are finite, $A \cup B \subseteq A \cap B$, so $A\subseteq B$ and $B\subseteq A$, meaning $A = B$.
> 
> $\left( \impliedby \right)$
> $$\begin{array}{l|l}
> 	d(A,A) = 1 - \dfrac{\left| A \cap A \right|}{\left| A \cup A \right| }  & = 1 - 1 \\
> 	\phantom{d(A,A)} = 1 - \dfrac{\left| A \right|}{\left| A \right| } & = 0 \\
> \end{array}$$
> (M2)
> $d$ is [[Symmetric Property|symmetric]] by the [[Symmetric Property|symmetry]] of $\cup$ and $\cap$.
> 
> (M3)
> $$\begin{align}
> 	d(A,B) &\le d(A,C) + d(C,B) \\
> 	 1 - \dfrac{\left| A \cap B \right|}{\left| A \cup B \right| } & \le 1 - \dfrac{\left| A \cap C \right|}{\left| A \cup C \right| } + 1 - \dfrac{\left| C \cap B \right|}{\left| C \cup B \right| }\\
> 	 -\dfrac{\left| A \cap B \right|}{\left| A \cup B \right| } & \le 1 - \dfrac{\left| A \cap C \right|}{\left| A \cup C \right|} - \dfrac{\left| C \cap B \right|}{\left| C \cup B \right| } \\
> 	 \dfrac{\left| A \cap C \right|}{\left| A \cup C \right|} - \dfrac{\left| A \cap B \right|}{\left| A \cup B \right| } &\le 1 - \dfrac{\left| C \cap B \right|}{\left| C \cup B \right| } \\
> \end{align}$$
> no idea dude