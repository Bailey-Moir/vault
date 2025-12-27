---
tags:
  - atom
  - math
---
For $f \in \mathcal{C}_{X}^Y$[^1],
> $f$ is *open* iff $\forall U \in \mathcal{T}_{X}, f(U) \in \mathcal{T}_{Y}$.

> $f$ is *closed* iff $\forall U^c \in \mathcal{T}_{X}, f(U)^c \in \mathcal{T}_{Y}$[^2].

> [!theorem-1]- If $f:X \to Y$ is [[Bijective Functions|bijective]], then $f$ is a [[Homeomorphisms|homeomorphism]] iff it is *open* and iff it is *closed* (they are all equivalent).
> $(\text{open}\implies \text{homeomorphism})$
> $$\begin{align}
> 	& f \text{ is open} \land f \text{ is continuous} \\
> 	\iff & \forall U \in \mathcal{T}_{X}, f(U)\in \mathcal{T}_{Y} \land \forall V \in \mathcal{T}_{Y}, f^{-1}(V) \in \mathcal{T}_{X} \\
> 	\iff & \left( \forall U \in X, \left( U \in \mathcal{T}_{X} \to  f(U)\in \mathcal{T}_{Y} \right) \right)  \\
> 	& \hspace{2em} \land \left( \forall U \in X, \left( f(U) \in \mathcal{T}_{Y} \to U \in \mathcal{T}_{X} \right) \right) && \text{Surjectivity} \\
> 	\iff & \forall U \in X, U \in \mathcal{T}_{X} \leftrightarrow f(U) \in \mathcal{T}_{Y} \\
> 	\iff & f \text{ is a homeomophism} && \text{(1)}
> \end{align}$$
> 
> $(\text{homeomorphism}\implies \text{closed})$
> $$\begin{align}
> 	& f \text{ is a homeomophism} \\
> 	\iff & \forall U \in X, U \in \mathcal{T}_{X} \leftrightarrow f(U) \in \mathcal{T}_{Y} && \text{(1)} \\
> 	\implies & \forall U \in \mathcal{T}_{X}, f(U) \in \mathcal{T}_{Y} \\
> 	\iff & \forall U^c \in \mathcal{T}_{X}, f(U^c) \in \mathcal{T}_{Y} \\
> 	\iff & \forall U^c \in \mathcal{T}_{X}, f(U)^c \in \mathcal{T}_{Y} && (2) \\
> 	\iff & f \text{ is closed} \\
> \end{align}$$
> $(\text{closed}\implies \text{open})$
> $$\begin{align}
> 	& f \text{ is closed} \\
> 	\iff & \forall U^c \in \mathcal{T}_{X}, f(U)^c \in \mathcal{T}_{Y} \\
> 	\iff & \forall U^c \in X, \left( U \in \mathcal{T}_{X} \to f(U^c)^c \in \mathcal{T}_{Y} \right) \\
> 	\iff & \forall U^c \in X, \left( U \in \mathcal{T}_{X} \to f(U) \in \mathcal{T}_{Y} \right) && (2) \\
> 	\iff & f \text{ is open} \\
> \end{align}$$
> \[$(1)$ [[Homeomorphisms]], Theorem 1, $(2)$ [[Injective Functions#Properties of Injections]]\]


[^1]: [[Continuous Maps]]
[^2]: [[Closed Sets]]