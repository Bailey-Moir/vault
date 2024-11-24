---
tags:
  - atom
  - math
  - discrete
---

| Name                | Definition     |
| ------------------- | -------------- |
| $q \to p$           | Converse       |
| $\neg p \to \neg q$ | Inverse        |
| $\neg q \to \neg p$ | Contrapositive |

- An [[Implication|implication]] is [[Logical Equivalence|logically equivalent]] to its *contrapositive*.
$$p \to q \iff \neg q \to \neg p$$
> [!proof]-
> | $p$ | $q$ | $\neg q$ | $\neg p$ | $p \to q$ | $\neg q \to \neg p$ | $(p \to q) \leftrightarrow (q \to \neg p)$ |
> | --- | --- | -------- | -------- | --------- | ------------------- | ------------------------------------------ |
> | 0   | 0   | 1        | 1        | 1         | 1                   | 1                                          |
> | 0   | 1   | 0        | 1        | 1         | 1                   | 1                                          |
> | 1   | 0   | 1        | 0        | 0         | 0                   | 1                                          |
> | 1   | 1   | 0        | 0        | 1         | 1                   | 1                                          |

- The *converse* of an [[Implication|implication]] is [[Logical Equivalence|logically equivalent]] to the *inverse*.
$$q \to p \iff \neg p \to \neg q$$
> [!proof]-
> Swapping the [[Statements and Propositions|statement]] variable names $p$ and $q$ gives the exact same expression as the [[Logical Equivalence|equivalence]] between the [[Implication|implication]] and its **contrapositive**
