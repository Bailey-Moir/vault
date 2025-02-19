---
tags:
  - atom
  - comp
---
*Concatenate [[Languages|languages]]* $A,B$ by [[Concatenate lines|concatenating]] each [[Strings|string]] from $A$ with each from $B$;
$$AB=\{ xy : x \in A \land y \in B \}.$$
Just like [[Concatenation of Strings|concatenation of strings]], this is associative, and $\{ \varepsilon \}$[^1] is the identity.
- **Associative**
	$A(BC) \equiv (AB)C \equiv ABC$
- **Set with [[Empty String]] as Identity**
	$\{\varepsilon\} A \equiv A \equiv A\{\varepsilon\}$
- **Exponentiation**
	$A^0 = \{\varepsilon\}, A^{n+1} = A^nA$
	$A^* = \bigcup_{n \in \N} A^n$
	$A^+ = \bigcup_{n \in \Z^+} A^n$

> [!note] This is similar to $A\times B$[^2], but instead of forming an [[Ordered Sets|ordered pair]], the [[Strings|strings]] are [[Concatenation of Strings|concatenated]].
# Theorems
- $A^*A^* \equiv A^* \equiv A^{**}$
- $\emptyset A \equiv \emptyset \equiv A\emptyset$
- $A(B \cup C) \equiv AB \cup AC$
	$(A \cup B)C \equiv AC \cup BC$
- $AB \not\equiv BA$

[^1]: [[Empty String]]
[^2]: [[Cartesian Product]]
