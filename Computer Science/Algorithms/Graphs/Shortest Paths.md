---
tags:
  - atom
  - comp
---
Given a [[Predecessor Tree|predecessor tree]]/[[Parent Arrays|parent array]] (e.g. generated by a [[Breadth First Search|BFS]] from $s$), the *shortest path* between two vertices $s$ and $t$ can be found using the following [[Algorithms|algorithm]].
$$\begin{array}{rl}
\hline

\scriptsize1& \textbf{procedure} \; \text{T{\scriptsize REE}-P{\scriptsize ATH}}(parent, s, t) \\
\scriptsize2& \hspace{1em} \textbf{if} \; s = t \\
\scriptsize3& \hspace{2em} \textbf{return} \; \text{the single-vertex path } s,t \\
\scriptsize4& \hspace{1em} \textbf{else} \\
\scriptsize5& \hspace{2em} \textbf{return} \; \text{the path T{\scriptsize REE}-P{\scriptsize ATH}}(parent,s,parent[t]) \text{ followed by } t \\

\hline
\end{array}$$