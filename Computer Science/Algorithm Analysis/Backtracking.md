---
tags:
  - atom
  - comp
---
*Backtracking* is an algorithmic technique for generating solutions of a computational problem.

$$\begin{array}{rl}
\hline

\scriptsize1& \textbf{procedure} \; \text{DFS-B{\scriptsize ACKTRACK}}(candidate, input, output) \\
\scriptsize2& \hspace{1em} \textbf{if} \; \text{S{\scriptsize HOULD}-P{\scriptsize RUNE}}(candidate) \\
\scriptsize3& \hspace{2em} \textbf{return} \\
\scriptsize4& \hspace{1em} \textbf{if} \; \text{I{\scriptsize S}-S{\scriptsize OLUTION}}(candidate,input) \\
\scriptsize5& \hspace{2em} \text{A{\scriptsize DD}-T{\scriptsize O}-O{\scriptsize UTPUT}}(candidate,output) \\
\scriptsize6& \hspace{2em} \textbf{return} \\
\scriptsize7&\\
\scriptsize8& \hspace{1em} \textbf{for} \; child\text{-}candidate  \; \textbf{in} \; \text{C{\scriptsize HILDREN}}(candidate,input) \\
\scriptsize9& \hspace{2em} \text{DFS-B{\scriptsize ACKTRACK}}(child\text{-}candidate, input, output) \\

\hline
\end{array}$$

> [!examples]
> - Generating [[Permutations|permutations]] of a [[Sets|set]] of items.
> - Generating [[Subsets|subsets]] of a [[Sets|set]].
> - Generating a Sudoku puzzle.
> - Placing 8 queens on a chess board so that they do not attack each other.
