---
tags:
  - atom
  - comp
---
A *pushdown automaton* (*PDA*, sometimes called a *stack automaton*) is a structure $M = \left( Q,\Sigma,\Gamma,\delta,q_{0},F \right)$. This is defined the same as a [[Deterministic Finite Automata|DFA]]/[[Non-Deterministic Finite Automata|NFA]], except
- $\Gamma$ is a finite [[Sets|set]], the **[[Stacks|stack]] alphabet**.
- $\varepsilon \notin \Sigma \cup \Gamma$.
- $\delta : Q\times \left( \Sigma\cup \{ \varepsilon \} \right) \times \Gamma^* \to \mathcal{P}\left( Q\times\Gamma^* \right)$


> [!example]-
> $L(M)=A$ for $M = \left( \{ q_{0},q_{1} \}, \{ a,b \},\{ 0 \},\delta,q_{0},\{ q_{1} \} \right)$, where $\delta$ returns $\emptyset$ except for
> $$\begin{align}
> 	\delta(q_{0},a,\varepsilon) &= \{ \left( q_{0},0 \right) \} \\
> 	\delta(q_{0},\varepsilon,\varepsilon) &= \{ \left( q_{1},\varepsilon \right) \} \\
> 	\delta(q_{1},b,\varepsilon) &= \{ \left( q_{1},\varepsilon \right) \} \\
> \end{align}$$
> ![300|center](pushdown-automata.excalidraw)
> 
> | **State** | **Input**     | **Stack** ($\mapsto$) |
> | --------- | ------------- | --------------------- |
> | $q_{0}$   | $aabb$        | $\varepsilon$         |
> | $q_{0}$   | $abb$         | $0$                   |
> | $q_{0}$   | $bb$          | $00$                  |
> | $q_{1}$   | $bb$          | $00$                  |
> | $q_{1}$   | $b$           | $0$                   |
> | $q_{1}$    | $\varepsilon$ | $\varepsilon$         |

> [!note] [[Non-Deterministic Finite Automata with Epsilon-Transitions|Epsilon-transitions]] (on the [[Stacks|stack]]) allow any item on the top of the [[Stacks|stack]].

> [!note] A [[Strings|string]] is accepted iff it can reach a final state with an empty [[Stacks|stack]].