---
tags:
  - atom
  - comp
---
A *configuration* in a [[Turing Machines|Turing machine]] is an element $\left( x,q,y \right) \in \Gamma^* \times Q \times \Gamma^*$. A *configuration* describes a snapshot of a [[Turing Machines|Turing machine]] during a computation, with
- $q$ being the current state,
- $x$ being the tape contents to the left of the head, and
- $y$ being the tape contents under the head and to its right.

>[!note] Blank symbols can be added or removed from either end:$$\left( \_{x,p,y} \right) = \left( x,p,y \right) = \left( x,p,y\_{} \right)$$
# Next-Configuration Relation ($\to$)
The *next-configuration [[Relations|relation]]* gives the possible transitions from the input *configuration*. This is very similar to [[Derivability|derivability]].
$$\left( xa,p,by \right) \to \left\{\begin{array}{ll}
	\left( x,q,acy \right) & \text{if } \delta(p,b)=\left( q,c,L \right) \\
	\left( xa,q,cy \right) & \text{if } \delta(p,b)=\left( q,c,N \right) \\
	\left( xac,q,y \right) & \text{if } \delta(p,b)=\left( q,c,R \right)
\end{array}\right.$$
where $a,b,c \in \Gamma$, $x,y \in \Gamma^*$, and $p,q \in Q$.