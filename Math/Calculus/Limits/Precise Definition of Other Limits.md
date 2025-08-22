# Precise Definition of One-Sided a Limit
![1000|center](precise-definition-of-onesided-limit.excalidraw.md)
$$
\begin{alignat}{3}
	\lim_{x\to a^+}& f(x) = L \iff \forall \varepsilon>0, \exists \delta>0 :  \forall x \in \;&&\left(a, a+\delta\right), \left|f(x) - L\right| < \varepsilon)
\\
	\phantom{\lim}_{x\to a^-}& &&(a-\delta,a)
\end{alignat}
$$
# Precise Definition of a Limit at Infinity
$$\begin{alignat}{3}
	\lim_{x\to\infty}& f(x) = L \iff \forall \varepsilon > 0, \exists N : ( x &&> N \implies |f(x) - L| < \varepsilon ) 
\\
	\phantom{\lim}_{x\to-\infty}& &&< \\
\end{alignat}$$
# Precise Definition of an Infinite Limit at Infinity
$$ \lim_{x\to\infty} f(x) = \infty \iff  \forall M > 0, \exists N : ( x > N \implies f(x) > M ) $$
