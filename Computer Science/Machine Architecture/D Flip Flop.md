---
tags:
  - atom
  - comp
---
![300|center](d-flip-flop.excalidraw)
A *D flip flop* stores a single bit in $Q$ (and $\overline Q$) from $D$ when the clock is on.

When the clock is off, $Q$ is unaffected, but when the clock is on:

| $D$ | $Q_{k}$ | $\overline{Q_{k}}$ | $Q_{k+1}$ | $\overline{Q_{k+1}}$ |
| --- | ------- | ------------------ | --------- | -------------------- |
| 0   | 0       | 1                  | 0         | 1                    |
| 0   | 1       | 0                  | 0         | 1                    |
| 1   | 0       | 1                  | 1         | 0                    |
| 1   | 1       | 0                  | 1         | 1                    |
