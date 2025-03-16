---
tags:
  - atom
  - comp
---
The *shuffle operation* describes two [[Independent Processes|independent processes]].

The *shuffle* $x\|y$ of two [[Strings|strings]] $x,y\in\Sigma^*$ contains all possible inter-leavings of their symbols:
- $\varepsilon \|w = w \| \varepsilon = \{ w \}$[^1] for $w \in \Sigma^*$
- $ax\|by = \{ a \}(x\|by)\cup \{ b \}(ax|y)$ for $a,b \in \Sigma$
- $A\|B = \bigcup \{ x\|y : x \in A \land y \in B \}$ for $A,B \subseteq \Sigma^*$

> [!example] $ab\|cd = \{ abcd,acbd,acdb,cabd,cadb, cdab \}$

> [!note] [[Regular Languages|Regular languages]] are closed under *shuffle*.

[^1]: [[Empty String]]
