---
tags:
  - atom
  - comp
---
*Backtracking* is an algorithmic technique for generating solutions of a computational problem.

$$\begin{array}{rl}
\hline

\scriptsize1& \textbf{procedure} \; \text{DFS-B{\scriptsize ACKTRACK}}(candidate, input, output) \\
\scriptsize2& \hspace{1em} \textbf{if} \; \text{I{\scriptsize S}-S{\scriptsize OLUTION}}(candidate,input) \\
\scriptsize3& \hspace{2em} \text{A{\scriptsize DD}-T{\scriptsize O}-O{\scriptsize UTPUT}}(candidate,output) \\
\scriptsize4& \hspace{1em} \textbf{else} \\
\scriptsize5& \hspace{2em} \textbf{for} \; child\text{-}candidate  \; \textbf{in} \; \text{C{\scriptsize HILDREN}}(candidate,input) \\
\scriptsize6& \hspace{3em} \text{DFS-B{\scriptsize ACKTRACK}}(child\text{-}candidate, input, output) \\

\hline
\end{array}$$

> [!examples]
> - Generating [[Permutations|permutations]] of a [[Sets|set]] of items.
> - Generating [[Subsets|subsets]] of a [[Sets|set]].
> - Generating a Sudoku puzzle.
> - Placing 8 queens on a chess board so that they do not attack each other.
