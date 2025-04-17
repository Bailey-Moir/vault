---
tags:
  - atom
  - comp
---
*Huffman coding* uses a "bottom-up" [[Greedy Algorithms|greedy]] approach to generate codes based on frequency.
$$\begin{array}{rl}
\hline
\scriptsize1& \textbf{procedure} \; \text{H{\scriptsize UFFMAN}-C{\scriptsize ODING}}(text) \\
\scriptsize2& \hspace{1em} freq \leftarrow \text{F{\scriptsize REQUENCY}-D{\scriptsize ICTIONARY}} \\
\scriptsize3& \hspace{1em} trees \leftarrow \text{mininum heap} \\
\scriptsize4& \hspace{1em} \textbf{for} \; c  \; \textbf{in} \; text \\
\scriptsize5& \hspace{2em} trees.\text{insert}(\text{L\scriptsize EAF}(freq[c], c)) \\
\scriptsize6& \hspace{1em} \textbf{while} \; \text{len}(trees) > 1 \\
\scriptsize7& \hspace{2em} l \leftarrow trees.\text{pop}() \\
\scriptsize8& \hspace{2em} r \leftarrow trees.\text{pop}() \\
\scriptsize9& \hspace{2em} trees.\text{insert}(\text{N\scriptsize ODE}((freq[l] + freq[r], l, r))) \\
\scriptsize_{1}0& \hspace{1em} \textbf{return} \; trees.\text{pop}() \\
\hline
\end{array}$$
This always yields an optimal result.

> [!example]-
> ![1000|center](huffman-coding.excalidraw)

> [!note] To ensure determinism, if multiple [[Trees|trees]] have the same frequency, they are ordered alphabetically by their smallest leaf node.

> [!analysis]- $O(n \log n)$
> - $trees$ can be implemented with a [[Heaps|min-heap]], which has operations all in $O(\log n)$.
> - Each iteration removes two elements, and a new element is added back, reducing the size by one, which takes $O(n)$.

> [!disadvantages]-
> - Whole document must be processed.
> - No local optimisation.
> - Encoding table must be included.
> - can't recognize macro patterns (like words).