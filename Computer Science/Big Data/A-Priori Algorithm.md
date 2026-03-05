---
tags:
  - atom
  - comp
---
The *A-Priori [[Algorithms|algorithm]]* finds [[Market-Basket Model#^support-and-frequent|frequent]] [[Market-Basket Model|itemsets]] using two passes:
1. Read each [[Market-Basket Model|basket]] and count the occurrences of each item, and then
2. Read each [[Market-Basket Model|basket]] and only count [[Market-Basket Model|itemsets]] made up of frequent items.

> [!note] This two-pass [[Algorithms|algorithm]] is needed, as counting every [[Market-Basket Model|itemset]] would be $O(n^2)$[^1] in memory.

[^1]: [[Asymptotic Notation]]
