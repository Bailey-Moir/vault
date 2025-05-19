---
tags:
  - atom
  - comp
---
$L(r)$ is the *language generated* by the [[Regular Expressions|regular expression]] $r$:
- $L(a) = \{ a \}$ for $a \in \Sigma$[^1]
- $L(\varepsilon) = \{ \varepsilon \}$
- $L(\emptyset) = \emptyset$
- $L(p|q) = L(p) \cup L(q)$
- $L(pq) = L(p)L(q)$
- $L(p^*) = L(p)^*$

\[[[Regular Expressions]]\]

[^1]: [[Alphabets]]
