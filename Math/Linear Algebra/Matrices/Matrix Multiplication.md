---
tags:
  - math
  - atom
---
In *matrix multiplication*, each entry is found using the [[Dot Product|dot product]]. The $ij$-th entry is found by getting the [[Dot Product|dot product]] of the $i$-th [[Matrices as Vectors|row vector]] of the left [[Matrices|matrix]] and the $j$-th [[Matrices as Vectors|column vector]] of the right [[Matrices|matirx]].
$$\begin{bmatrix} 
	\textcolor{lightgray}{a_{11}} & \textcolor{darkgray}{a_{12}} & \textcolor{gray}{a_{13}} \\
	a_{21} & a_{22} & a_{23} \\
\end{bmatrix}

\begin{bmatrix} 
	\textcolor{lightgray}{b_{11}} & b_{12} \\
	\textcolor{darkgray}{b_{21}} & b_{22} \\
	\textcolor{gray}{b_{31}} & b_{32} \\
\end{bmatrix}

=

\begin{bmatrix}
	\textcolor{Orchid}{c_{11}} & c_{12} \\
	c_{21} & c_{22} \\
\end{bmatrix}$$
$$\begin{align*}
\textcolor{Orchid}{c_{11}} &= \textcolor{lightgray}{a_{11}b_{11}} + \textcolor{darkgray}{a_{12}b_{21}} + \textcolor{gray}{a_{13}b_{31}} \\
c_{ij} &= \sum_{n=1} \left( a_{in} \cdot b_{nj} \right)
\end{align*}$$
This would not be possible if the left matrix's number of columns was different to the right matrix's number of rows, as **the entries must be able form pairs**. Thus, two matrices only **conform for matrix multiplication if the left matrix has as many columns as the right matrix has rows**. The result of matrix multiplication has as many rows as the left matrix, and as many columns as the right matrix.

$$\begin{array}{c}
\large A_{m_A \times n_A}B_{m_B \times n_B} = C_{m_A \times n_B} \\
\small n_{A} = m_{B} \\

\underset{\begin{array}{c} a \times b \\ 4\times2 \end{array}}{
\begin{bmatrix}
	? & ? \\
	? & ? \\
	? & ? \\
	? & ? \\
\end{bmatrix}}

\underset{\begin{array}{c} b \times c \\ 2\times5 \end{array}}{
\begin{bmatrix}
	? & ? & ? & ? & ? \\
	? & ? & ? & ? & ? \\	
\end{bmatrix}}
=
\underset{\begin{array}{c} a \times c \\ 4\times5 \end{array}}{
\begin{bmatrix}
	? & ? & ? & ? & ? \\
	? & ? & ? & ? & ? \\
	? & ? & ? & ? & ? \\
	? & ? & ? & ? & ? \\
\end{bmatrix}}

\end{array}$$

# Properties of Matrix Multiplication
- **Associative**
	$A(BC) \equiv (AB)C$
	$k(AB) \equiv (kA)B \equiv A(kB)$
- **Distributive**
	$A(B+C) \equiv AB + AC$
- **NOT** Commutative
	$AB \hspace{.1em}\not{\hspace{-.3em}\equiv}\hspace{.3em} BA$

