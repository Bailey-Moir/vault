---
tags:
  - atom
  - math
---
A [[Collections|collection]] $\mathcal{B} \subseteq \mathcal{P}(X)$ is called a *basis* on $X$ iff:
1. $\mathcal{B}$ covers $X$ ($\forall x \in X, \exists B \in \mathcal{B} : x \in B$)
2. $\forall B_{1},B_{2} \in \mathcal{B}, \forall x \in B_{1} \cap B_{2}, \exists B \in \mathcal{B} : x \in B \subseteq B_{1} \cap B_{2}$.

> [!definition] The **topology generated** by $\mathcal{B}$ is
> $$\large \mathcal{T}_{\mathcal{B}} = \left\{ \cup \mathcal{C} : \mathcal{C} \subseteq \mathcal{B} \right\}$$