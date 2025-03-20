---
tags:
  - atom
  - comp
---
For a [[Context-Free Grammar|context-free grammar]] $G = \left( N,\Sigma,P,S \right)$ and $x,y \in (N \cup \Sigma)^*$, $y$ is *derivable* from $x$ iff for some $n \in \N$, $x \Rightarrow_{G}^n y$, denoted
$$\large x \Rightarrow_{G}^* y$$
> [!note] *Derivability* is a [[Relations|relation]] on $(N \cup \Sigma)^*$.

> [!notation] $x \Rightarrow^n_{G} y$ means that $y$ is *derivable* from $x$ using $n$ steps/[[Context-Free Grammar#Performing Productions|productions]].

> [!alternative] $y$ is *derivable* from $x$ $\iff$ $x$ generates $y$ $\iff$ $x$ yields $y$.

> [!definition] $\Rightarrow_{G}^*$ is the **[[Reflexive Property|reflexive]]-[[Transitive Property|transitive]] closure** of the [[Relations|relation]] $\Rightarrow_{G}^1$.