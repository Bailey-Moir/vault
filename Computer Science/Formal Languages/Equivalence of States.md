---
tags:
  - atom
  - comp
---
Two states $p,q \in Q$ of a [[Deterministic Finite Automata|DFA]] are *equivalent*, notated $p \sim q$, iff for all $w \in \Sigma^*$, $\hat{\delta}(p,w) \in F$ iff $\hat{\delta}(q,w) \in F$;
$$ p\sim q \iff \forall w \in \Sigma^*, \left( \hat{\delta}(p,w) \in F \iff \hat{\delta}(q,w) \in F \right)$$

> [!definition] Two states are **distinguishable** iff they are not *equivalent*.

\[[[Equivalence Relations]]\]
# Algorithm
To find [[Equivalence of States|equivalent states]]:
1. Create a table of pairs $\{ p,q \}$ with $p,q \in Q$ and $p\ne q$.
2. Mark all $\{ p,q \}$ such that $p \in F$ and $q \notin F$ or vice  versa.
3. If there is an unmarked $\{ p,q \}$ and an $a \in \Sigma$ such that $\{ \delta(p,a), \delta(q,a) \}$ is marked, then mark $\{ p,q \}$.
4. Repeat (3) until no changes occur.
5. Any states $p$ and $q$ with unmarked $\{ p,q \}$ are equivalent.

> [!note]- The mark given is the iteration of (3).
