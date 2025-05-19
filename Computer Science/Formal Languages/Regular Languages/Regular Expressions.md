---
tags:
  - atom
  - comp
---
## Atomic Patterns
-  $a$ for $a\in\Sigma$[^1] is matched by the symbol $a$.
- $\varepsilon$ is matched by the [[Empty String|empty string]].
- $\emptyset$ is matched by nothing.
- $?$ is matched by any symbol in $\Sigma$[^1].
## Compound Patterns
- $p|q$ is matched by when $p$ is matched **or** $q$ is matched.
- $p\&q$ is matched by when $p$ is matched **and** $q$ is matched.
- $pq$ is matched by $w = xy$ where $x$ matches $p$ and $y$ matches $q$.
- $\overline p$ is matched by everything that $p$ does not.
- $[p] = p|\varepsilon$
- $p^*$ is matched by $w = w^1w^2\cdots w^n$ for $n\ge 0$ where $w_{i}$ matches $p$.
- $p^+ = pp^*$

> [!note] Precedence order is: star, concatenation, union.

[^1]: [[Alphabets]]
