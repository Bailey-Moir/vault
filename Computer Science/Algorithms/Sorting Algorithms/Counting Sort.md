---
tags:
  - atom
  - comp
---
The *counting sort* [[Algorithms|algorithm]] assumes that each of the $n$ input elements has a key value in [[Number Sets|natural numbers]].
$$\begin{array}{rl}
\hline
\scriptsize1& \textbf{procedure} \; \text{C{\scriptsize OUNTING}-S{\scriptsize ORT}}(A, key) \\
\scriptsize2& \hspace{1em} B \leftarrow \text{array of size } n \text{ filled with N{\scriptsize ONE}} \\
\scriptsize3& \hspace{1em} P \leftarrow \text{K{\scriptsize EY}-P{\scriptsize OSITIONS}}(A,key) \\
\scriptsize4& \hspace{1em} \textbf{for} \; \text{a}  \; \textbf{in} \; A \\
\scriptsize5& \hspace{2em} B[P[key(a)]] \leftarrow a \\
\scriptsize6& \hspace{2em} P[key(a)] \leftarrow P[key(a)] + 1 \\
\scriptsize7& \hspace{1em} \textbf{return} \; B \\
\hline
\end{array}$$

$$\begin{array}{rl}
\hline
\scriptsize1& \textbf{procedure} \; \text{K{\scriptsize EY}-P{\scriptsize OSITIONS}}(A, key) \\
\scriptsize2& \hspace{1em} k \leftarrow \text{max} \{ key(a) : a \in A \} \\
\scriptsize3& \hspace{1em} C \leftarrow \text{array of size } k+1 \text{ filled with } 0 \\
\scriptsize4& \hspace{1em} \textbf{for} \; a  \; \textbf{in} \; A \\
\scriptsize5& \hspace{2em} C[key(a)] \leftarrow C[key(a)] + 1 \\
\scriptsize6& \hspace{1em} sum \leftarrow 0 \\
\scriptsize7& \hspace{1em} \textbf{for} \; i  \; \textbf{from} \; 0 \; \textbf{to} \; k \\
\scriptsize8& \hspace{2em} C[i], sum \leftarrow sum, sum + C[i] \\
\scriptsize9& \hspace{1em} \textbf{return} \; C \\
\hline
\end{array}$$

> [!note] $C$ originally gives the amount of space that elements with the given $key$ take.