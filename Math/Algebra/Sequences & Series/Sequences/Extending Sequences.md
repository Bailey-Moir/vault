---
tags:
  - atom
  - math
---
Extending [[Sequences|sequences]] to [[Continuity|continuous]] [[Functions|functions]] over the [[The Real Numbers|real]] numbers allows for use of calculus techniques to infer information about the original [[Sequences|sequence]]. 

Let $f$ be a [[Continuity|continuous]] extension of some [[Sequences|sequence]] $\left\{a_n\right\}_{n=1}^\infty$ into the [[The Real Numbers|real]] numbers. Note that the below inferences are only [[Logical Implication|one way implications]].
## Inferring [[Convergence of Sequences|Convergence of Sequences]]
If $f$ is convergent to $L$, $\{a_n\}$ must also be convergent to $L$, i.e.
$$ \forall L, \left( \lim_{x \to \infty} f(x) = L \to \lim_{n\to\infty} \{a_n\} = L \right) $$
*Note that the [[Converse, Inverse, and Contrapositive|contrapositive]] must also be true:  if ${a_n}$ is divergent, $f$ must also be divergent.*
$$\small\color{gray} \forall L, \left( \lim_{n \to \infty} \{a_{n}\} \ne L \to \lim_{x\to\infty} f(x) \ne L \right) $$
## Inferring [[Monotone Sequences|Monotonicity]]
If $f$ is *monotonically*, *strictly monotonically*, *eventually monotonically*, or *eventually strictly monotonically* increasing/decreasing, then $\{a_n\}$ must be as well.