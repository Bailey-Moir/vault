---
tags:
  - atom
  - comp
---
1. Run the [[Simple Closed Path Algorithm|simple closed path algorithm]], giving $P_{0},\dots,P_{n-1}$.
2. Initialise a [[Stacks|stack]] to $[P_{0}, P_{1}, P_{2}]$.
3. Traverse the [[Points|points]] in order. If the last two [[Points|points]] of the [[Stacks|stack]] with the next point make a right turn, pop the top element from the [[Stacks|stack]].
4. Repeat step $3$ until no right turns are made.

$$\begin{array}{rl}
\hline
\scriptsize1& \textbf{procedure} \; \text{G{\scriptsize RAHAM}-S{\scriptsize SCAN}}(A, d) \\
\scriptsize2& \hspace{1em} P_{0} \leftarrow \text{lowest leftmost point} \\
\scriptsize3& \hspace{1em} P \leftarrow \text{Sorted points in CCW order w.r.t } P_{0} \\
\scriptsize4& \hspace{1em} stack \leftarrow [P[0], P[1], P[2]] \\
\scriptsize5& \hspace{1em} \textbf{for} \; \text{i}  \; \textbf{from} \; 3 \; \textbf{to} \; n-1 \\
\scriptsize6& \hspace{2em} \textbf{while} \; \textbf{not} \; \text{{\scriptsize IS}CCW}(stack[-2], stack[-1], P[i]) \\
\scriptsize7& \hspace{3em} stack.\text{pop}() \\
\scriptsize8& \hspace{2em} stack.\text{push}(P[i]) \\
\hline
\end{array}$$

$$O(n\log n)$$