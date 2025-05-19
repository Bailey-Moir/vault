---
tags:
  - atom
  - comp
---
$L(M)$ is the [[Languages|language]] defined as the [[Sets|set]] of **accepted strings** of $M$.
- If $M$ is a [[Deterministic Finite Automata|DFA]], $L(M) := \{ w \in \Sigma^* : \hat{\delta}(q_{0},w) \in F\}$[^1]
- If $M$ is an [[Non-Deterministic Finite Automata|NFA]], $L(M) := \{ w \in \Sigma^* : \hat{\delta}(q_{0},w) \cap F \ne \emptyset\}$[^1]

[^1]: [[Extended Transition Function]]
