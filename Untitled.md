Let $\left( f_{n} \right)$ be a Cauchy sequence of functions in the metric space $\left( X, d_{\infty} \right)$. 

$X$ is a set of bounded functions as $\forall g \in X, \sup \left| g \right| \le 1$, so $X \subseteq B((0,1))$. Since $\left( 0,1 \right) \ne \emptyset$, $\left( B((0,1)) ), d_{\infty} \right)$ is complete, so $\left( f_{n} \right)$ converges to some $f_{*} \in B\left( (0,1) \right)$.

We will show $f_{*} \in X$. In order to do this, we need to prove $f_{*}$ is continuous, and $\sup \left| f_{*}(x) \right| \le 1$.

$\left( f_{n} \right)$ is a sequence of continuous and bounded functions that uniformly converge to $f_{*}$, so $f_{*}$ is continuous.

For all $x \in \left( 0,1 \right)$ and $n \in \N$, $\left| f_{n}(x) \right| \le 1$, so
$$ \lim_{ n \to \infty } \left| f_{n}(x) \right| \le 1. $$
By the continuity of $\left| \cdot \right|$ on $\R$, and specifically the sequence definition of continuity with $\left( f_{n} \right)$,
$$ \left| f_{*}(x) \right| = \lim_{ n \to \infty } \left| f_{n}(x) \right| \le 1.$$
Since this was for all $x \in \left( 0,1 \right)$, $\sup \left| f_{*}(x) \right| \le 1$.

Thus, $f_{*} \in X$, meaning if a sequence $\left( f_{n} \right)$ in $\left( X, d_{\infty} \right)$ is Cauchy, it is convergent in that same space, so $\left( X,d_{\infty} \right)$ is complete.