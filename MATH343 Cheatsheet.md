### Supremums
$\forall s < \sup S, \exists x \in S: s < x \le \sup S$
### Squeeze Theorem
For three [[Sequences|sequences]] $\left( a_{n} \right)$, $\left( b_{n} \right)$, and $\left( c_{n} \right)$ of $\R$ such that $a_{n} \le c_{n} \le b_{n}$ for all $n$ and $\lim a_{n} = \lim b_{n} = L$, then $\lim c_{n} = L$.
### Bolzano-Weierstrass
Every [[Bounded Sequences|bounded]] [[Sequences|sequence]] $\left( x_{n} \right)$ in $\R^n$ has a [[Limit Points###^sequence-limit-points|limit point]] (a [[Metric Convergence|convergent]] [[Sequences|subsequence]]).
### Bounded Function Set
$$B(X) := \{ f : X \to \R : \exists M \in \R : \left| f \right| < M \} \subseteq \R^X$$
### Continuity by Sequences
$f(x) : I \to M$ is *continuous* at $x_{0} \in I$ iff for any [[Sequences|sequence]] $\left( x_{n} \right)$ in $I$ that [[Metric Convergence|converges]] to $x_{0}$, the [[Sequences|sequence]] $\left( f(x_{n}) \right)$ [[Metric Convergence|converges]] to $f(x_{0})$.
### Boundedness w/ Continuity
For $f \in \mathcal{C}(I)$ for any [[Intervals|closed interval]] $I \subseteq \R$, $f$ is [[Bounded Sequences|bounded]] on $I$.
### Metric Space Definition
A *metric* of a [[Empty Set|non-empty]] [[Sets|set]] $M$ is a [[Functions|function]] $d : M \times M \to \R$ such that ($\forall x,y,z \in M$)
1. $d(x,y) = 0 \leftrightarrow x = y$ (and $d(x,y) \ge 0$),
2. $d(x, y) = d(y, x)$,
3. $d(x,z) \le d(x,y) + d(y,z)$ ([[Triangle Ineqaulity|triangle inequality]])
### Norm Definition
A *norm* of a [[Vector Spaces|vector space]] $V$ is a [[Functions|function]] $\| \cdot \| : V \to \R$ that assigns each $\vecbf{v} \in V$ a real number $\| \vecbf{v} \|$ such that for all $\vecbf{u},\vecbf{v} \in V$ and $c \in \R$,
1. **[[Inner Products|Positive Definite]]**
   $\mathit{\| \vecbf{v} \| \ge 0}$
   $\| \vecbf{v} \| = 0 \leftrightarrow \vecbf{v}=\vecbf{0}$
2. **[[Linear Maps|Absolute Homogeneity]]**
   $\| \lambda \vecbf{v} \| = \left| \lambda \right|\| \vecbf{v} \|$
3. **[[The Triangle Inequality|The Triangle Inequality]]**
   $\| \vecbf{u}+\vecbf{v} \| \le \| \vecbf{u} \|+\| \vecbf{v} \|$.
### P-Norms
For $p \in \left[ 1,\infty \right)$, the *$\it p$-norm* of $\vecbf{v} \in \R^n$ is given by
$$\| \vecbf{v} \|_{p} = \sqrt[p]{\left| v_{1} \right|^p + \left| v_{2} \right|^p + \dots + \left| v_{n} \right|^p  },$$
and the $\infty$*-norm* is given by
$$\| \vecbf{v} \|_{\infty} = \max\{ \left| v_{1} \right|,\left| v_{2} \right| ,\dots,\left| v_{n} \right|  \},$$
### Equivalent Norms
Two [[Norms|norms]] $\| \cdot \|_{1}$ and $\| \cdot \|_{2}$ on the same [[Vector Spaces|vector space]] $V$ are *equivalent* iff
$$\exists A,B \in \R_{> 0} : \forall \vecbf{v} \in V, A\| \vecbf{v} \|_{1} \le \| \vecbf{v} \|_{2} \le B\| \vecbf{v} \|_{1}.$$
> [!theorem]- In [[Metric Spaces|metric spaces]] [[Norms###^induced-metrics|induced]] by *equivalent norms*, if a [[Sequences|sequence]] [[Metric Convergence|converges]] in one, it [[Metric Convergence|converges]] to the same thing in the others.

> [!example]- The [[P-Norms|1-]] [[P-Norms|2-]] and $\infty$[[P-Norms|-norms]] are all *equivalent* (in fact, all [[P-Norms|p-norms]] are *equivalent*)
### Component-wise Convergence
A [[Sequences|sequence]] $( \vecbf{a_{n}} )$ in $\R^n$ is said to *converge component-wise* to $\vecbf{\lambda} \in \R^n$ iff
$$ \forall i \in \{ 1,\dots,n \}, \lim_{ n \to \infty } a_{n,i}= \lambda_{i}, $$
using the usual [[Topology|topology]]/[[Metric Spaces|metric]] on $\R$.

> [!theorem]- *Component-wise convergence* on $\R^n$ is equivalent to $\infty$[[P-Norms|-norm]] [[Metric Convergence|convergence]].

### Point-wise Convergence
A [[Sequences|sequence]] of [[Functions|functions]] $\left( f_{n} \right)$ in $\R^{X}$ *point-wise converges* to $g \in \R^X$ iff
$$\forall x \in X, \lim_{ n \to \infty } f_{n}(x) = g(x),$$

### Uniform Continuity
$f \in B(X)$ is *uniformly convergent* to $g \in B(X)$ iff it is [[Metric Convergence|convergent]] to $g$ in $\left( B(X),d_{\infty} \right)$, i.e. iff
$$ \forall \varepsilon > 0, \exists N \in \N : \forall n \ge N, \sup_{x \in X} \left| f(x) - g(x) \right| < \varepsilon. $$
> [!theorem]- *Uniform Convergence* $\to$ [[Point-wise Convergence|Point-wise convergence]]

> [!theorem]- *(Completeness)* If $X \ne \emptyset$, $\left( B(X),d_{\infty} \right)$ is [[Completeness|complete]].

### Completeness
A [[Metric Spaces|metric space]] is *complete* iff all [[Cauchy Sequences|Cauchy sequences]] [[Metric Convergence|converge]].

> [!example] $\R^n$ is *complete* under the $1$-, $2$- and $\infty$[[P-Norms|-norm]] [[Norms#^induced-metrics|induced metrics]].

> [!example] $\left[ a_{1},b_{1} \right] \times \left[ a_{2},b_{2} \right] \subseteq \R^2$ is *complete* under the $1$-, $2$- and $\infty$[[P-Norms|-norm]] [[Norms#^induced-metrics|induced metrics]].
