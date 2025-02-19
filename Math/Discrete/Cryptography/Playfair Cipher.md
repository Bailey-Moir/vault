---
tags:
  - atom
  - math
  - discrete
  - comp
---
Like [[Substitution Ciphers|substitution ciphers]], this can be solved with frequency analysis.
# Key
Fill in a $5\times 5$ grid with your [[Key|key]]word followed by the rest of the alphabet, deleting repeats and combining `i` and `j`.
$$\begin{matrix}
	\text{m}&\text{a}&\text{n}&\text{c}&\text{h} \\
	\text{e}&\text{s}&\text{t}&\text{r}&\text{b} \\
	\text{d}&\text{f}&\text{g}&\text{i/j}&\text{k} \\
	\text{l}&\text{o}&\text{n}&\text{q}&\text{u} \\
	\text{v}&\text{w}&\text{x}&\text{y}&\text{z} \\
\end{matrix}$$
# Encryption
Break the [[Plaintext|plaintext]] into pairs, padding with `x` in the case of repeats/singletons.

To encrypt each pair, find the first letter in the [[#Key|key square]] and locate the letters at the opposite corners of the rectangle they form. If they are on the same row, use a shift instead
$$\begin{array}{rlrlrl}
	\text{th} \mapsto \text{bn} &
	\begin{matrix}
		\text{.}&\text{.}&\text{n}&\text{.}&\text{h} \\
		\text{.}&\text{.}&\text{t}&\text{.}&\text{b} \\
		\text{.}&\text{.}&\text{.}&\text{.}&\text{.} \\
		\text{.}&\text{.}&\text{.}&\text{.}&\text{.} \\
		\text{.}&\text{.}&\text{.}&\text{.}&\text{.} \\
	\end{matrix} &
	\text{cr} \mapsto \text{ri} &
	\begin{matrix}
		\text{.}&\text{.}&\text{.}&\text{c}&\text{.} \\
		\text{.}&\text{s}&\text{.}&\text{r}&\text{.} \\
		\text{.}&\text{.}&\text{.}&\text{i/j}&\text{.} \\
		\text{.}&\text{.}&\text{.}&\text{.}&\text{.} \\
		\text{.}&\text{.}&\text{.}&\text{.}&\text{.} \\
	\end{matrix} &
\end{array}$$