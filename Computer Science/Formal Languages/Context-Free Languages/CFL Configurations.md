---
tags:
  - atom
  - comp
---
A *configuration* in a [[Pushdown Automata|pushdown automata]] is an element $\left( q, x, \alpha \right) \in Q\times\Sigma^*\times\Gamma^*$. A *configuration* describes a snapshot of a [[Pushdown Automata|pushdown automata]] during a computation, with
- $q$ being the current state,
- $x$ being the remaining input/[[Strings|string]].
- $\alpha$ being the content of the [[Stacks|stack]].

# Next-Configuration Relation ($\to$)
The *next-configuration [[Relations|relation]]* gives the possible transitions from the input *configuration*. This is very similar to [[Derivability|derivability]].
$$L(M) = \{ x \in \Sigma^* : \exists q \in Q :  \left( q_{0},x,\varepsilon \right) \to^* \left( q, \varepsilon, \varepsilon \right) \}$$