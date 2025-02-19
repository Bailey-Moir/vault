---
tags:
  - atom
  - math
---
![200|center](gaussian-elimination.excalidraw)
1. **Augmented Matrix**
   Write the linear system as an [[Augmented Matrices|augmented matrix]].
2. **Row Reduction**
   Use a sequence of elementary row operations to put the [[Matrices|matrix]] in [[EF & REF|REF]].
3. **Solve the System**
   Write out the equivalent system in [[EF & REF|EF]] and solve by back-substitution.

> [!example]- $$\left[ \left. \begin{matrix} 1 & 1 & 1 & -1 \\ 0 & 0 & 2 & 2 \end{matrix} \hspace{0.4em} \right| \hspace{0.4em} \begin{matrix} 2 \\ 0 \end{matrix}	 \right]$$
> $x_{1}$ and $x_{3}$ are [[Pivots and Free Variables|pivot variables]], and $x_{2}$ and $x_{4}$ are [[Pivots and Free Variables|free variables]]. let $x_{2} = s$ and $x_{4} = t$ for $s,t \in \R$.
> $$\begin{array}{c|c}
> 	\begin{aligned}
> 		2x_{3} + 2x_{4} &= 0 \\
> 		2x_{3} + 2t &= 0 \\
> 		x_{3} &= -t
> 	\end{aligned}
> 	&
> 	\begin{aligned}
> 		x_{1} + x_{2} + x_{3} - x_{4} &= 2 \\
> 		x_{1} + s - t - t &= 2 \\
> 		x &= 2 + 2t - s
> 	\end{aligned}
> \end{array}$$


> [!example]- $$\left[ \left. \begin{matrix} 1 & 2 \\ 3 & 4 \end{matrix} \hspace{0.4em} \right| \hspace{0.4em} \begin{matrix} 2 \\ 12 \end{matrix}	 \right]$$
> $$\begin{array}{l}
> 	R_2 \leftarrow  R_2 - 3R_1 \\
> 	\left[
> 		\left.
> 		\begin{matrix}
> 			1 & 2 \\
> 			0 & -2
> 		\end{matrix}
> 		\hspace{0.4em}
> 		\right|
> 		\hspace{0.4em}
> 		\begin{matrix}
> 			2 \\
> 			6
> 		\end{matrix}	
> 	\right]
> \end{array}$$
> In [[EF & REF|REF]], and all variables in the system are [[Pivots and Free Variables|pivots]], meaning there will be a unique solution.
> $$\begin{array}{l}
> 	x_{2} = -3 \\
> 	\begin{align*}
> 		x_{1} &= 2 - 2x_{2} \\
> 		x_{1} &= 2 + 6 \\
> 		&= 8 \\ 
> 	\end{align*}
> \end{array}$$