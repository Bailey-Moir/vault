---
tags:
  - atom
  - comp
---
A [[Languages|language]] $L$ is *semi-*[[Decidability|decidable]] (partially computable), if there is an [[Algorithms|algorithm]] that, for every input $w$, outputs `True` if $w \in L$ and does not terminate necessarily if $w \notin L$.

A [[Functions|function]] $f : A \to B$ is *partially computable* iff there is an [[Algorithms|algorithm]] that outputs $f(x)$ whenever $f(x)$ is defined.

A [[Functions|function]] $f : \Sigma^* \to \Gamma^*$ is *partially computable* iff $f = F(M)$ for some [[Turing Machines|TM]] $M$.

> [!note] The [[binary-prefix-code.excalidraw|decidable]] [[Languages|languages]] are a [[Subsets|subset]] of the *semi-decidable* [[Languages|language]] 

> [!theorem]- If $L$ and $L^c$[^1] are *semi-decidable*, $L$ is decidable.
> ![1000|center](semi-decidability-with-complement.excalidraw)

[^1]: [[Complement]]
