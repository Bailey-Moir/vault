---
tags:
  - atom
  - math
  - discrete
  - comp
---
The *Vigenère cipher* is a different [[Caesar Cipher|Caesar cipher]] $x \mapsto x + \beta$ is applied to each letter. The [[Key|key]] is a word of length $n$. The [[Plaintext|plaintext]] is folded into rows of length $n$, and for each character in row $i$, $\beta$ is given by the value of the $i$-th character in the [[Key|key]].

> [!Example] **[[Plaintext]]**: Hello world** [[Key]]**: Key
> $$\begin{array}{c}
> 	\begin{matrix}
> 		\text{H}&\text{E}&\text{L} \\
> 		\text{L}&\text{O}&\text{W} \\
> 		\text{O}&\text{R}&\text{L} \\
> 		\text{D}
> 	\end{matrix}  \\
> 	\hline
> 	\begin{matrix}
> 		\text{K}&\text{E}&\text{Y} \\
> 	\end{matrix}
> \end{array}\hspace{2em}\begin{array}{c}
> 	\begin{matrix}
> 		\text{7}&\text{4}&\text{11} \\
> 		\text{11}&\text{14}&\text{22} \\
> 		\text{14}&\text{17}&\text{11} \\
> 		\text{3}
> 	\end{matrix}  \\
> 	\hline
> 	\begin{matrix}
> 		\text{10}&\text{4}&\text{24} \\
> 	\end{matrix}
> \end{array}\hspace{2em}\begin{array}{c}
> 	\begin{matrix}
> 		\text{7}&\text{4}&\text{11} \\
> 		\text{11}&\text{14}&\text{22} \\
> 		\text{14}&\text{17}&\text{11} \\
> 		\text{3}
> 	\end{matrix}  \\
> 	\phantom{\text{1}}
> \end{array}$$

> [!note]
> The *Vigenère cipher* will only be secure if
>  - the [[Key|key]] length is long compared to the [[Plaintext|plaintext]], and
>   - the [[Key|key]] is random.