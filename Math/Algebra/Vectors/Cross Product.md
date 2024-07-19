---
tags:
  - atom
  - math
we:
---
$$ \mathbf{\underline{a}} \times \mathbf{\underline{b}} = \mathbf{\underline{c}} \implies \mathbf{\underline{c}} \:\bot\: \mathbf{\underline{a}} \land \mathbf{\underline{c}} \:\bot\: \mathbf{\underline{b}} $$

$$\mathbf{\underline{a}} \times \mathbf{\underline{b}} = \left\langle a_2b_3 - a_3b_2, a_3b_1, - a_1b_3, a_1b_2 - a_2b_1 \right\rangle$$

> [!proof]
> $$\begin{array}{l}
> 	\mathbf{\underline{c}} \cdot \mathbf{\underline{a}} = 0 \land \mathbf{\underline{c}} \cdot \mathbf{\underline{b}} = 0 \\
> 	\begin{array}{ll}
> 		0 = c_1a_1 + c_2a_2 + c_3a_3 &
> 		0 = c_1b_1 + c_2b_2 + c_3b_3 \\
> 		c_3 = -\dfrac{1}{a_3}\left( c_1a_1 + c_2a_2 \right) &
> 		c_3 = -\dfrac{1}{b_3}\left( c_1b_1 + c_2b_2 \right) \\
> 	\end{array} \\
> 	\dfrac{1}{a_3}\left( c_1a_1 + c_2a_2 \right) = \dfrac{1}{b_3}\left( c_1b_1 + c_2b_2 \right) \\
> 	c_1a_1b_3 + c_2a_2b_3 = c_1a_3b_1 + c_2a_3b_2 \\
> 	c_1(a_1b_3 - b_1a_3) = c_2(a_3b_2 - a_2b_3) \\
> 	c_1(a_1b_3 - a_3b_1) + c_2(a_2b_3 - a_3b_2) = 0 \\
> 	\text{This is in the form $pc_1 + qc_2 = 0$, for which} \\
> 	\text{an obvious solution is $c_1 = q$ and $c_2 = -p$.} \\
> 	\begin{array}{ll}
> 		c_1 = a_2b_3 - a_3b_2 & c_2 = a_3b_1 - a_1b_3
> 	\end{array} \\
> 	\therefore c_3 = a_1b_2 - a_2b_1 \\
> 	\langle c_1,c_2,c_3 \rangle = \langle a_2b_3 - a_3b_2, a_3b_1 - a_1b_3, a_1b_2 - a_2b_1 \rangle
> \end{array}$$
Note: the cross product is only defined for three-dimensional vectors.

$$\begin{align*}
	\mathbf{\underline{a}} \times \mathbf{\underline{b}} &= \begin{vmatrix} a_2 & a_3 \\ b_2 & b_3 \end{vmatrix} \mathbf{\underline{i}} - \begin{vmatrix} a_1 & a_3 \\ b_1 & b_3 \end{vmatrix} \mathbf{\underline{j}} + \begin{vmatrix} a_1 & a_2 \\ b_1 & b_2 \end{vmatrix} \mathbf{\underline{k}} \\
	&= \begin{vmatrix}
		\mathbf{\underline{i}} & \mathbf{\underline{j}} & \mathbf{\underline{k}} \\
		a_1 & a_2 & a_3 \\
		b_1 & b_2 & b_3
	\end{vmatrix}
\end{align*}$$
\[[[Determinants|determinants]], [[Determinant of a 2x2 Matrix|determinant of a 2x2 matrix]]\].

> [!example]
> $$\begin{align*}
> 	\mathbf{\underline{a}} \times \mathbf{\underline{b}} &= \begin{vmatrix}
> 		\mathbf{\underline{i}} & \mathbf{\underline{j}} & \mathbf{\underline{k}} \\
> 		a_1 & a_2 & a_3 \\
> 		b_1 & b_2 & b_3
> 	\end{vmatrix} \\
> 	&= \begin{vmatrix} a_2 & a_3 \\ b_2 & b_3 \end{vmatrix} \mathbf{\underline{i}} - \begin{vmatrix} a_1 & a_3 \\ b_1 & b_3 \end{vmatrix} \mathbf{\underline{j}} + \begin{vmatrix} a_1 & a_2 \\ b_1 & b_2 \end{vmatrix} \mathbf{\underline{k}} \\
> 		&= (a_2b_3 - a_3b_2) \mathbf{\underline{i}} - (a_1b_3 - a_3b_1)\mathbf{\underline{j}} + (a_1b_2 - a_2b_1)\mathbf{\underline{k}} \\
> \end{align*}$$