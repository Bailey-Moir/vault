---
tags:
  - atom
  - math
  - linear
  - discrete
---
A finite *matrioid* $M$ is a pair $\left( E,\mathcal{I} \right)$ , where $E$ the finite **ground** [[Sets|set]], and $\mathcal{I}\subseteq\mathcal{P}(E)$[^1] is called the **independent sets**, with the following properties:
- **Empty Set**
  $\emptyset \in \mathcal{I}$.
- **Hereditary Property** - Every [[Subsets|subset]] of an **independent set** is **independent**;
  $\forall A \in \mathcal{I}, \mathcal{P}(A) \subseteq \mathcal{I}$[^1].
- **Expansion/Augmentation/Exchange Property**
  $\forall A,B \in \mathcal{I}, \left( \left| A \right| > \left| B \right| \to \exists x \in A \setminus B : B \cup \{ x \} \in \mathcal{I}\right)$.

> [!example] $\left( \{ a,b,c,d \},\{ \emptyset, \{ a \},\{ b \},\{ c \},\{ d \},\{ a,b \},\{ a,c \},\{ a,d \},\{ b,c \},\{ b,d \},\{ c,d \} \} \right)$

> [!note] Without the **expansion property**, this defines an [independence system](https://en.wikipedia.org/wiki/Independence_system).

> [!theorem] An **independent set** is [[Maximal vs. Maximum|maximum]] iff it is [[Maximal vs. Maximum|maximal]].

[^1]: [[Power Sets]]