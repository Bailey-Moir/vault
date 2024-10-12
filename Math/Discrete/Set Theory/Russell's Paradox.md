---
tags:
  - atom
  - math
  - discrete
---
Note that [[Sets|sets]] can contain sets as elements. Making up a property, we will call a [[Sets|set]] "normal" iff it does not contain itself. Let
$$ R = \left\{ x : x \text{ is a normal set} \right\} $$
Is $R$ normal?

If $R$ is not normal, $R \in R$ (by definition of normality), but $R$ contains all normal sets, hence $R \notin R$, implying a [[Contradictions|contradiction]].
If $R$ is normal, $R \notin R$ (by definition of normality), but $R$ contains all normal sets, hence $R \in R$, implying a [[Contradictions|contradiction]].

Thus the existence of $R$ is a [[Contradictions|contradiction]].