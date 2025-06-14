---
tags:
  - atom
  - comp
---
The [[Components of Graphs|components]] of a [[Graphs|graph]] can be found by repeatedly using **[[Breadth First Search|BFS]] or [[Depth First Search|DFS]]**, storing [[Graph Traversal|discovered vertices]] by each [[Graph Traversal|traversal]] as one [[Components|components]], and taking a [[Vertices|vertex]] in the remaining [[Vertices|vertices]] to do the next [[Tree Traversal|traversal]].
$$\begin{array}{rl}
\hline

\scriptsize1& \textbf{procedure} \; \text{C{\scriptsize ONNECTED}-C{\scriptsize ONNECTED}}(Adj) \\
\scriptsize2& \hspace{1em} n \leftarrow \text{number of vertices (the length of }Adj\text{)} \\
\scriptsize3& \hspace{1em} state \leftarrow \text{an array of length } n \text{ filled with U{\scriptsize NDISCOVERED}} \\
\scriptsize4& \hspace{1em} Q \leftarrow \text{an empty queue}\\
\scriptsize5& \hspace{1em} components \leftarrow \left\{  \right\} \\
\scriptsize6& \hspace{1em} \textbf{for} \; i \; \textbf{from} \; 0 \; \textbf{to} \; n-1 \\
\scriptsize7& \hspace{2em} \textbf{if} \; state[i] = \text{U{\scriptsize NDISCOVERED}} \\
\scriptsize8& \hspace{3em} previous\text{-}state \leftarrow state \\
\scriptsize9& \hspace{3em} state[i] \leftarrow \text{D{\scriptsize ISCOVERED}} \\
\scriptsize10& \hspace{3em} \text{E{\scriptsize NQUEUE}}(Q,i) \\
\scriptsize11& \hspace{3em} \text{BFS-L{\scriptsize OOP}}(Adj,Q,state) \\
\scriptsize12& \hspace{3em} new\text{-}component \leftarrow \text{all vertices whose state has changed} \\
\scriptsize13& \hspace{3em} component \leftarrow components \;\cup\; \{ new\text{-}component \}  \\
\scriptsize14& \hspace{1em} \textbf{return} \; components \\

\hline
\end{array}$$
> [!analysis]- $\Theta(n^2)$
> Line $12$ is $\Theta(n)$, and it is ran inside of an $\Theta(n)$ for loop (line $6$).

\[[[Breadth First Search]], [[Queues]]\]