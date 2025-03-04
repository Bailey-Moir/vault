---
tags:
  - atom
  - comp
---
The *extended transition function* $\hat{\delta}:Q\times\Sigma^* \to Q$ [[Induction|inductively]] extends the [[Domain|domain]] of the [[Deterministic Finite Automata|transition function]] to [[Strings|strings]].
- **Base Case**
  $\hat{\delta}(q,\varepsilon) = q$
- **Induction Step**
  $\hat{\delta}(q,ax) = \hat{\delta}(\delta(q,a),x)$ where $a \in \Sigma$[^1] and $x \in \Sigma^*$[^2]

> [!note]- *Extended Transition Functions* for [[Non-Deterministic Finite Automata|NFA]]s.
> - $\hat{\delta}:Q\times\Sigma^* \to \mathcal{P}(Q)$
> - **Base Case**
>   $\hat{\delta}(q,\varepsilon) = \{ q \}$
> - **Induction Step**
>   $\hat{\delta}(q,ax) = \bigcup_{p \in \delta(q,a)}  \hat{\delta}(p,x)$ where $a \in \Sigma$[^1] and $x \in \Sigma^*$[^2]

> [!note]- *Extended Transition Functions* for [[Non-Deterministic Finite Automata with Epsilon-Transitions|NFAs with]] $\varepsilon$[[Non-Deterministic Finite Automata with Epsilon-Transitions|-closure]].
> - **Base Case**
>   $\hat{\delta}(q,\varepsilon) = E(q)$
> - **Induction Step**
>   $\hat{\delta}(q,ax) = \bigcup_{r \in E(q)} \bigcup_{p \in \delta(r,a)} \hat{\delta}(p,x)$ where $a \in \Sigma$[^1] and $x \in \Sigma^*$[^2]


\[[[Deterministic Finite Automata]]\]

[^1]: [[Alphabets]]
[^2]: [[Concatenation of Languages and Alphabets]]
