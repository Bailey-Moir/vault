---
tags:
  - atom
  - math
---
Using an [[Augmented Matrices|augmented matrix]],  you can [[Linear Map Invertibility|invert]] any given [[Matrices|matrix]] via an extended version of [[Gaussian Elimination|Gaussian elimination]], called Gauss–Jordan elimination, where the [[Matrices|matrix]] is transformed into into [[EF & REF#RREF|RREF]] instead of [[EF & REF|REF]].

> [!example]-
> $$\begin{align*}
> 	[A|I] &=
> 	\left[
> 		\begin{matrix}
> 			 2 & -1 &  3 \\
> 			-5 &  3 &  1 \\
> 			-3 &  2 &  3 \\
> 		\end{matrix}
> 		\:
> 		\left|
> 		\:
> 		\begin{matrix}
> 			 1 &  0 &  0 \\
> 			 0 &  1 &  0 \\
> 			 0 &  0 &  1 \\
> 		\end{matrix}
> 		\right.
> 	\right] \\
> 	
> 	&R_3 \leftarrow R_3 - R_1 \\
> 	
> 	&= \left[
> 		\begin{matrix}
> 			 2 & -1 &  3 \\
> 			-5 &  3 &  1 \\
> 			-5 &  3 &  0 \\
> 		\end{matrix}
> 		\:
> 		\left|
> 		\:
> 		\begin{matrix}
> 			 1 &  0 &  0 \\
> 			 0 &  1 &  0 \\
> 			-1 &  0 &  1 \\
> 		\end{matrix}
> 		\right.
> 	\right] \\
> 	
> 	&R_2 \leftarrow R_2 - R_3 \\
> 	
> 	&= \left[
> 		\begin{matrix}
> 			 2 & -1 &  3 \\
> 			 0 &  0 &  1 \\
> 			-5 &  3 &  0 \\
> 		\end{matrix}
> 		\:
> 		\left|
> 		\:
> 		\begin{matrix}
> 			 1 &  0 &  0 \\
> 			 1 &  1 & -1 \\
> 			-1 &  0 &  1 \\
> 		\end{matrix}
> 		\right.
> 	\right] \\
> 	
> 	&R_1 \leftarrow R_1 - 3R_2 \\
> 	 
> 	&= \left[
> 		\begin{matrix}
> 			 2 & -1 &  0 \\
> 			 0 &  0 &  1 \\
> 			-5 &  3 &  0 \\
> 		\end{matrix}
> 		\:
> 		\left|
> 		\:
> 		\begin{matrix}
> 			-2 & -3 &  3 \\
> 			 1 &  1 & -1 \\
> 			-1 &  0 &  1 \\
> 		\end{matrix}
> 		\right.
> 	\right] \\
> 	
> 	&R_3 \leftarrow R_3 + 3R_1 \\
> 	 
> 	&= \left[
> 		\begin{matrix}
> 			 2 & -1 &  0 \\
> 			 0 &  0 &  1 \\
> 			 1 &  0 &  0 \\
> 		\end{matrix}
> 		\:
> 		\left|
> 		\:
> 		\begin{matrix}
> 			-2 & -3 &  3 \\
> 			 1 &  1 & -1 \\
> 			-7 & -9 & 10 \\
> 		\end{matrix}
> 		\right.
> 	\right] \\ 
> 
> 	&R_1 \leftarrow -R_1 + 2R_3 \\
> 	 
> 	&= \left[
> 		\begin{matrix}
> 			 0 &  1 &  0 \\
> 			 0 &  0 &  1 \\
> 			 1 &  0 &  0 \\
> 		\end{matrix}
> 		\:
> 		\left|
> 		\:
> 		\begin{matrix}
> 			-12 &-15 & 17\\
> 			  1 &  1 & -1 \\
> 			 -7 & -9 & 10 \\
> 		\end{matrix}
> 		\right.
> 	\right] \\
> 	
> 	&R_1 \leftrightarrow R_3, \: R_3 \leftrightarrow R_2 \\
>  
> 	&= \left[
> 		\begin{matrix}
> 			 1 &  0 &  0 \\
> 			 0 &  1 &  0 \\
> 			 0 &  0 &  1 \\
> 		\end{matrix}
> 		\:
> 		\left|
> 		\:
> 		\begin{matrix}
> 			-7 & -9 & 10 \\
> 			-12 &-15 & 17\\
> 			 1 &  1 & -1 \\
> 		\end{matrix}
> 		\right.
> 	\right] \\
> 	
> 	&= [I|A^{-1}]
> \end{align*}$$

\[[[Row Reduction]]\]