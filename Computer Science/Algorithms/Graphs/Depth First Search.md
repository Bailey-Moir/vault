---
tags:
  - atom
  - comp
---
A *DFS* of a [[Graphs|graph]] traverses each [[Vertices|vertex]], increasing in depth whenever possible using [[Recursion|recursion]] or a [[Stacks|stack]].
$$\begin{array}{rl}
\hline

\scriptsize1& \textbf{procedure} \; \text{DFS-T{\scriptsize REE}}(Adj,s) \\
\scriptsize2& \hspace{1em} n \leftarrow \left| Adj \right|  \\
\scriptsize3& \hspace{1em} state \leftarrow n\text{-array filled with U{\scriptsize NDISCOVERED}}  \\
\scriptsize4& \hspace{1em} parent \leftarrow n\text{-array filled with {\scriptsize NULL}}  \\
\scriptsize5& \hspace{1em} state[s] \leftarrow \text{D{\scriptsize ISCOVERED}}  \\
\scriptsize6& \hspace{1em} \text{DFS-L{\scriptsize OOP}}(Adj,s,state,parent) \\
\scriptsize7& \hspace{1em} \textbf{return} \; parent \\

\hline
\end{array}$$

$$\begin{array}{rl}
\hline

\scriptsize1& \textbf{procedure} \; \text{DFS-L{\scriptsize OOP}}(Adj,u,state,parent) \\
\scriptsize2& \hspace{1em} \textbf{for} \; v \; \textbf{in} \; Adj[u]  \\
\scriptsize3& \hspace{2em} \textbf{if} \; state[v] = \text{U{\scriptsize NDISCOVERED}}  \\
\scriptsize4& \hspace{3em} state[v] \leftarrow \text{D{\scriptsize ISCOVERED}}  \\
\scriptsize5& \hspace{3em} parent[v] \leftarrow u \\
\scriptsize6& \hspace{3em} \text{DFS-L{\scriptsize OOP}}(Adj,v,state,parent) \\
\scriptsize7& \hspace{1em} state[u] \leftarrow \text{P{\scriptsize ROCESSED}}  \\

\hline
\end{array}$$
$$\mathcal{O}(\left|V\right|+\left|E\right|)$$

> [!implementation]- Sudo-python
 >```
 >set all vertices to unvisited
 >stack.push(start)
 >
 >while stack is not empty:
 >   v = stack.pop()
 >
 >   if v is unvisited:
 >       mark v visited
 >       for each neighbour u of v:
 >		   if u is unvisited:
 >			   stack.push(u)
 >```