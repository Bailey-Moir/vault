---
tags:
  - atom
  - math
  - discrete
  - c
---

The *composition* of $f$ and $g$ ($g \circ f$) is defined as
$$ \left( g \circ f \right)(a) = g(f(a)) \hspace{2em} a \in A$$
- $f : A \to B$, $g : B \to C$, $g \circ f : A \to C$
  Note [[Math/Discrete/Set Theory/Functions/Domain|domain]] of $g$ can be any [[Supersets|superset]] of the [[Math/Discrete/Set Theory/Functions/Codomain|codomain]] of $f$.
- $g \circ f$ is read as "$g$ follows $f$".

\[[[Math/Discrete/Set Theory/Functions/Functions|Functions]]\]

# Properties of Composite Functions
$\forall f: A \to B, g : B \to C$
- If $f$ and $g$ are both [[Surjective Functions|surjective]], then $g \circ f$ is [[Surjective Functions|surjective]].
- If $f$ and $g$ are both [[Injective Functions|injective]], then $g \circ f$ is [[Injective Functions|injective]].
- If $f$ and $g$ are both [[Bijective Functions|bijective]], then $g \circ f$ is [[Bijective Functions|bijective]].