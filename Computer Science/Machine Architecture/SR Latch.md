---
tags:
  - atom
  - comp
---
![500|center](sr-latch.excalidraw)
We can use an *SR Latch* to store an individual bit of memory ($Q$).

| S   | R   | $Q_{k}$ | $\overline{Q_{k}}$ | $Q_{k+1}$ | $\overline{Q_{k+1}}$ |
| --- | --- | ------- | ------------------ | --------- | -------------------- |
| 0   | 0   | 1       | 0                  | 1         | 0                    |
| 0   | 0   | 0       | 1                  | 0         | 1                    |
| 0   | 1   | 1       | 0                  | 0         | 1                    |
| 0   | 1   | 0       | 1                  | 0         | 1                    |
| 1   | 0   | 1       | 0                  | 1         | 0                    |
| 1   | 0   | 0       | 1                  | 1         | 0                    |
> [!intuition] If $R$ is on, $Q$ is set to false, and if $S$ is on, $Q$ is set to true.

> [!note] $S \to \neg R$ and $R \to \neg S$[^1]

> [!note]- Alternative *SR Latch*
>  ![500|center](sr-latch-2.excalidraw)

[^1]: [[Converse, Inverse, and Contrapositive]], Contrapositive
