---
tags:
  - atom
  - comp
---
A *Turing machine* (*TM*) is a structure $M = \left( Q,\Sigma,\Gamma,\delta,q_{0},\_, q_{a}, q_{r} \right)$.
- $Q$, $\Sigma$, $q_{0}$ are the same as in a [[Deterministic Finite Automata|DFA]].
- $\Gamma$ is a finite [[Sets|set]] $\Sigma \subseteq \Gamma$, the **tape [[Alphabets|alphabet]]**.
- $\_ \in \Gamma \setminus \Sigma$ is the **blank symbol**.
- $q_{a} \in Q$ is the accept state.
- $q_{r} \in Q$ (with $q_{a} \ne q_{r}$) is the reject state.
- $\delta : \left( Q \setminus \{ q_{a},q_{r} \} \right) \times \Gamma \to Q \times \Gamma \times \{ L,R,N \}$ is the transition [[Functions|function]]

These are very similar to [[Pushdown Automata|PDAs]].

> [!machine]-
> An infinite tape is added, consisting of cells that store a symbol. The input is the initial state of the tape, and the output is the final state of the tape. The machine has a read/write head over one cell on the tape, which can move along the tape.

> [!note]- *Turing machines* are deterministic.
> Thus, every state in $Q\setminus \{ q_{a},q_{r} \}$ must have a transition for every element in $\Gamma$ (just like [[Deterministic Finite Automata|DFA]]s).

>[!example]- Add 1 to a binary number
> ![1000|center](add-1-tm.excalidraw)

> [!definition]- A *Turing machine* is said to be **total** iff it halts (accepts or rejects) on all inputs $w \in \Sigma^*$.