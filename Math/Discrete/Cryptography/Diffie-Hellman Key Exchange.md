---
tags:
  - atom
  - math
  - discrete
---
1. Alice and Bob agree on a finite [[Cyclic Groups|cyclic group]] $G$ and a [[Group Generators|generator]] $g \in G$.
2. Alice chooses a random integer $a \in \Z_{\left| G \right|}$, which she keeps secret. She computes $A = g^a$ and sends this to Bob.
3. Likewise, Bob chooses a random integer $b \in \Z_{\left| G \right|}$ and sends $B = g^b$ to Alice.
4. Alice computes $K = B^a$ and Bob computes $K=A^b$.
$$ K = B^a = \left( g^b \right)^a = g^{ab} = \left( g^a \right)^b = A^b = K $$

> [!note] $G,g,A,$ and $B$ are known to Eve

> [!note]- Reliance on Difficulty of the [[Discrete Logarithm Problem]]
> If Eve can efficiently solve the [[Discrete Logarithm Problem|DLP]] in $G$, then this is not secure, as Eve can compute
> $$\begin{array}{ccc}
> 	\log_{g}(A) = a && \log_{g}(B) = b,
> \end{array}$$
> revealing the [[Key|secret key]] $K = g^{ab}$.

