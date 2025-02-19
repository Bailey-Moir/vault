---
tags:
  - atom
  - comp
---
For a given [[Algorithms|algorithm]], let
- $\chi$ be the [[Sets|set]] of all possible inputs,
- $\text{size}:\chi\to\N$ be a [[Functions|function]] that measures the size of the input $\in \chi$.
- $\text{time}:\chi\to\N$ be a [[Functions|function]] that measures the time taken for an input $\in \chi$.
## Worst Case
$$ \large T_{WC}(n) = \max_{x \in \{ x \in \chi : \text{size}(x) = n \}} \text{time}(x) $$
## Best Case
$$\large T_{BC}(n) = \min_{x \in \{ x \in \chi : \text{size}(x) = n \}} \text{time}(x) $$