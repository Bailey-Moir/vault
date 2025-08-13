---
tags:
  - math
  - atom
---
![500|center](squeeze-theorem.excalidraw.md)
For three [[Sequences|sequences]] $\left( a_{n} \right)$, $\left( b_{n} \right)$, and $\left( c_{n} \right)$ such that $a_{n} \le c_{n} \le b_{n}$ for all $n$ and $\lim a_{n} = \lim b_{n} = L$, then $\lim c_{n} = L$.

> [!proof]- **2.9**
> Let $\varepsilon > 0$ be given. Then, there are $N_{a},N_{b}$ such that
> $$\begin{array}{rl}
> 	\forall n \ge N_{a},&\left| a_{n}-L \right| < \varepsilon \\
> 	\forall n \ge N_{b},&\left| b_{n}-L \right| < \varepsilon. \\
> \end{array}$$
> Thus, for all $n \ge \max\{ N_{a},N_{b} \}$, $L - \varepsilon < a_{n}$ and $b_{n} < L+\varepsilon$. Thus,
> $$\begin{array}{c}
> 	L-\varepsilon < a_{n} \le c_{n} \le b_{n} < L + \varepsilon \\
> 	L-\varepsilon < c_{n} < L + \varepsilon \\
> 	\left| c_{n} - L \right| < \varepsilon \\
> \end{array}$$