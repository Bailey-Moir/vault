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

> [!proof]- The **topology generated** by a *basis* $\mathcal{B}$ of $X$ is a [[Topology|topology]] of $X$.
> 1. **$\mathbf{\emptyset \in \mathcal{T}_{\mathcal{B}}}$ and $\mathbf{X \in \mathcal{T}_{\mathcal{B}}}$.**
>    Let $\mathcal{C} = \emptyset$. Since $\emptyset \subseteq \mathcal{B}$, $\cup \emptyset = \emptyset \in \mathcal{T}_{\mathcal{B}}$.
>    Let $\mathcal{C} = \mathcal{B}$. By the axiom that $\mathcal{B}$ covers $X$, since $\mathcal{B} \subseteq \mathcal{B}$, $\cup \mathcal{B}=X\in \mathcal{T}_{\mathcal{B}}$.
> 2. **$\mathbf{\mathcal{T}_{\mathcal{B}}}$ is closed under [[Unions & Intersections|unions]].**
>    For all $\alpha \in I$ (for some [[Indexing Set|indexing set]] $I$), let $V_{\alpha} \in \mathcal{T}_{\mathcal{B}}$. We need to show that
>    $$\bigcup_{\alpha \in I} V_{\alpha} \in \mathcal{T}_{\mathcal{B}}$$
>    By the definition of $\mathcal{T}_{\mathcal{B}}$, for each $V_{\alpha}$, there exists some $\mathcal{C}_{\alpha} \subseteq \mathcal{B}$ such that $V_{\alpha} = \cup \mathcal{C}_{\alpha}$. Thus,
>    $$\bigcup_{\alpha \in I} V_{\alpha} = \bigcup_{\alpha \in I} \left( \bigcup \mathcal{C_{\alpha}} \right) = \bigcup \left( \bigcup_{\alpha \in I} \mathcal{C_{\alpha}} \right) \in \mathcal{T}_{\mathcal{B}},$$
>    as $\bigcup_{\alpha \in I} \mathcal{C_{\alpha}} \subseteq \mathcal{B}$.
> 3. **$\mathbf{\mathcal{T}_{\mathcal{B}}}$ is closed under finite [[Unions & Intersections|intersections]].**
>    Let $U,V \in \mathcal{T}_{\mathcal{B}}$. By the definition of $\mathcal{T_{\alpha}}$, there exists $\mathcal{A},\mathcal{C} \subseteq \mathcal{B}$ such that $U = \cup \mathcal{A}$ and $V = \cup \mathcal{C}$. 
>    $$U \cap V = \left( \bigcup \mathcal{A} \right) \cap \left( \bigcup \mathcal{C} \right) = \bigcup \{ A \cap C : A \in \mathcal{A}, C \in \mathcal{C} \}$$
>    We need to show that $U \cap V \in \mathcal{T}_{\mathcal{B}}$, and then the rest is shown by [[Induction|induction]]. From above, by 2, all that remains to be shown is that: for any fixed $A, C \in \mathcal{B}$, $A \cap C \in \mathcal{T_{B}}$.
> 
>    If $A \cap C$ is non-[[Empty Set|empty]], then for any $x \in A \cap C$, there exists a *basis* element $B_{x} \in \mathcal{B}$ such that $x \in B_{x} \subseteq A \cap C$. Thus,
>    $$A \cap C \subseteq \bigcup_{x \in A \cap C} B_{x} \subseteq A \cap C,$$
>    so
>    $$A \cap C = \bigcup_{x \in A \cap C} B_{x} \in \mathcal{T}_{\mathcal{B}}.$$
>    If $A \cap C$ is [[Empty Set|empty]], then $A \cap C \in \mathcal{T}_{\mathcal{B}}$ by 1.