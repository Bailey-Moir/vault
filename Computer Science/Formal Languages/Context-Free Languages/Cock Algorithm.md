---
tags:
  - atom
  - comp
---
The *Cock algorithm* tests the membership of a [[Strings|string]] $w$ in a [[Context-Free Languages|CFL]].

- Assume that $G$ is in [[Chomsky Normal Form|Chomsky normal form]].
- Let $n = \left| w \right|$.
- Let $w_{ij}$ be the substring of $w$ between on $i$ (inclusive) and $j$ (exclusive)[^1].
- $N_{ij} = \{ A \in N : A \Rightarrow^* w_{ij} \}$ contains the non-terminals that [[Derivability|generate]] $w_{ij}$.
- The *Cock algorithm* calculate $N_{ij}$ for each $0 \le i < j \le n$.
- Then, $w \in L(G)$ $\iff$ $S \in N_{0n}$.

$$N_{ij} = \{ A \in N : \exists k : \exists B \in N_{ik}, C \in N_{kj} :  A \to BC \in P \}$$

> [!example]-
>  ![1000|center](cock-algo.excalidraw.md)

> [!Note] This has a time complexity of $O(n^3)$.

[^1]: [[Basic Python#Slicing]]
