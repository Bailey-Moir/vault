A *non-deterministic finite automaton* (*NFA*) is a structure $M = \left( Q,\Sigma,\delta,q_{0},F \right)$ defined the same as a [[Deterministic Finite Automata|DFA]], except
- the [[Codomain|codomain]] of $\delta$ is $\mathcal{P}(Q)$[^2] instead of $Q$ as $\delta$ maps to a [[Sets|sets]] of states (including [[Empty Set|empty sets]]).

$M$ can move to any state in $\delta(q,a)$, and if $\delta(q,a) = \emptyset$, $M$ gets stuck. 

[^1]: [[Relations]]
[^2]: [[Power Sets]]
[^3]: [[Functions]]