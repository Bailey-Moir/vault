---
tags:
  - atom
  - comp
---
The *halting problem* $HP = \{ \left< M \right>\#w : M \text{ halts on input } w \}$ is [[Decidability|undecidable]].

> [!proof]-
> Assume $HP = L(M_{HP})$ for some **[[Turing Machines|total]]** [[Turing Machines|TM]].
> 
> Construct a [[Turing Machines|TM]] $M_{SHP}$ that writes a copy of its input separated by $\#$ (i.e. $\left< M \right>\#\left< M \right>$, and then behaves like $M_{HP}$.
> ![1000|center](hp-from-shp.excalidraw)
> Then this [[Decidability|decides]] $SHP$, a [[Contradictions|contradiction]]. $SHP$ is just a special case of $HP$.

> [!proof]- The *special halting problem* $SHP = \{ \left< M \right> : M \text{ halts on input } \left< M \right> \}$ is [[Decidability|undecidable]].
> Assume the [[Proof by Contradiction|contrary]], that $SHP$ is [[Decidability|decidable]]. Then $SHP = L(M_{SHP})$ for some **[[Turing Machines|total]]** [[Turing Machines|TM]].
> 
> Construct a [[Turing Machines|TM]] $M'$ that behaves like $M_{SHP}$, but goes into an endless loop if $M_{SHP}$ accepts.
> ![1000|center](shp.excalidraw)
> Then,
> $$\begin{align}
> 	&M' \text{ halts on input } \left< M' \right>  \\
> 	\iff&M_{SHP} \text{ rejects } \left< M' \right>   \\
> 	\iff&\left< M' \right> \notin M_{SHP}    \\
> 	\iff&M' \text{ does not halt on input } \left< M' \right>     \\
> \end{align}$$
> This is a [[Contradictions|contradiction]], thus, $SHP$ must be [[Decidability|undecidable]].