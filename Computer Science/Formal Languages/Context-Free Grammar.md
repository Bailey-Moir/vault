---
tags:
  - atom
  - comp
---
A *context-free grammar* (*CFG*) is a structure $G = \left( N,\Sigma,P,S \right)$ where
- $N$ is the **non-terminals**, a finite [[Sets|set]],
- $\Sigma$ is the **terminals**, a finite [[Sets|set]] [[Disjoint Sets|disjoint]] from $N$,
- $P \subseteq N \times (N \cup \Sigma)^*$ is a finite [[Sets|set]] of **productions**,
- $S \in N$ is the **start symbol**.

> [!example]- Arithmetic Expressions
> $$\begin{align}
> 	\Sigma &= \{ +,*,(,),n \} && \text{Terminals}\\
> 	N &= \{ E,T,F \} && \text{Non-terminals}\\
> 	S &= E && \text{Start symbol}
> \end{align}$$
> With the **productions** defined as
> $$\begin{align}
> 	E &\to T | E + T \\
> 	T &\to F | T * F \\
> 	F &\to E | n \\
> \end{align}$$

> [!definition] A non-terminal $A \in N$ is **generating** iff $A \Rightarrow^* w$[^1] for some $w \in \Sigma^*$

> [!definition] A non-terminal $A \in N$ is **reachable** iff $S \Rightarrow^* uAv$[^1] for some $u,v \in (\Sigma\cup N)^*$
# Performing Productions
Let $u,v,w \in (N \cup \Sigma)^*$ and $A \to w \in P$.
- $uAv$ yields $uwv$ in one step, by replacing $A$ with $w$; this is denoted
$$uAv \Rightarrow_G^1 uwv$$
- Alternatively, $uwv$ is **derivable** from $uAv$ in one step.

[^1]: [[Derivability]]
