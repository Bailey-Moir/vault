---
tags:
  - atom
  - math
  - discrete
---
Every integer $n \ge 2$ can be written as a product of [[Primes|primality]]. This factorization is unique up to reordering.
$$ \forall n \in \Z_{\ge 2}, \exists! P \subset \mathbb{P} : n = \prod P $$
where $P$ is a [[Multi-sets|multi-set]].

> [!proof]-
> **Base Case**
> For $n=2$, $2$ is [[Primes|prime]], is only a multiple of itself (excluding $1$). Thus $P = \{2\}$, proving the base case.
> 
> **Induction Step**
> Assume the theorem holds $\forall i \in \Z, 2 \le i < k$ (we need to show the theorem for $k$).
> 
> If $k$ is [[Primes|prime]], $k$ is only a multiple of itself (excluding $1$). Thus $P = \{k\}$.
> 
> If $k$ is not [[Primes|prime]], $\exists a,b \in \Z : 2 \ge a,b < k \land k = ab$. Note that the theorem is assumed to be true for $a$ and $b$ as part of our induction hypothesis. Since $a$ and $b$ are products of primes, $k = ab$ must also be a product of primes.
> 
> If the prime factors of $k$ weren't unique, it would have two representations:
> $$k = p_1p_2 \dots p_r = q_1q_2 \dots q_s$$
> Then $p_1|q_1 \dots q_s$ and since $p_1$ is prime, $p_1|q_j$ for some $1 \le j \le s$ (see [[Euclid's Lemma]]). Since $q_j$ is also prime, $p_1 = q_j$. Dividing through by this factor gives
> $$p_2 \dots p_r = q_1 \dots q_{j-1}q_{j+1} \dots q_s = t$$
> Since $2 \le t < k$, it follows by the induction hypothesis that $t$ must be unique, and since $p_1 = q_j$, $k$ must be unique as well.
> 
> \[[[Strong Induction]]\]