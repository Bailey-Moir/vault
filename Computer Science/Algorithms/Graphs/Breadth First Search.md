---
tags:
  - atom
  - comp
---
A *BFS* of a [[Graphs|graph]] traverses each [[Vertices|vertex]] in ascending order of depth using a [[Queues|queue]].
$$\begin{array}{rl}
\hline

\scriptsize1& \textbf{procedure} \; \text{BFS-T{\scriptsize REE}}(Adj,s) \\
\scriptsize2& \hspace{1em} n \leftarrow \left| Adj \right|  \\
\scriptsize3& \hspace{1em} state \leftarrow n\text{-array filled with U{\scriptsize NDISCOVERED}}  \\
\scriptsize4& \hspace{1em} parent \leftarrow n\text{-array filled with {\scriptsize NULL}}  \\
\scriptsize5& \hspace{1em} q \leftarrow \text{an empty queue}  \\
\scriptsize6& \hspace{1em} state[s] \leftarrow \text{D{\scriptsize ISCOVERED}}  \\
\scriptsize7& \hspace{1em} \text{E{\scriptsize NQUEUE}}(q,s) \\
\scriptsize8& \hspace{1em} \textbf{return} \; \text{BFS-L{\scriptsize OOP}}(Adj,q,state,parent) \\

\hline
\end{array}$$

$$\begin{array}{rl}
\hline

\scriptsize1& \textbf{procedure} \; \text{BFS-L{\scriptsize OOP}}(Adj,Q,state,parent) \\
\scriptsize2& \hspace{1em} \textbf{while} \; \left| Q \right| \ne 0  \\
\scriptsize3& \hspace{2em} u \leftarrow \text{D{\scriptsize EQUEUE}}(Q)  \\
\scriptsize4& \hspace{2em} \textbf{for} \; v \; \textbf{in} \; Adj[u]  \\
\scriptsize5& \hspace{3em} \textbf{if} \; state[v] = \text{U{\scriptsize NDISCOVERED}}  \\
\scriptsize6& \hspace{4em} state[v] \leftarrow \text{D{\scriptsize ISCOVERED}}  \\
\scriptsize7& \hspace{4em} parent[v] \leftarrow u \\
\scriptsize8& \hspace{4em} \text{E{\scriptsize NQUEUE}}(Q,v) \\
\scriptsize9& \hspace{2em} state[u] \leftarrow \text{P{\scriptsize ROCESSED}}  \\
\scriptsize10& \hspace{1em} \textbf{return} \; parent \\

\hline
\end{array}$$
$$\mathcal{O}(\left|V\right|+\left|E\right|)$$
