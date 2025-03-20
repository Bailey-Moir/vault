---
tags:
  - atom
  - math
  - discrete
---
Each [[Vertices|vertex]] on a [[Network|network]]
1. Chooses two large distinct [[Primes|primes]] $p$ and $q$, and computes $n = pq$ and $\phi(n) = (p-1)(q-1)$[^1].
2. Chooses element $e \in \Z_{\phi(n)}^\times$[^1][^4].
3. Computes $e^{-1} \in \Z_{\phi(n)}^\times$[^1][^4].

The [[Vertices|vertices']] **public key** is then $(n,e)$, and its **private key** is then $e^{-1}$.

**Sending**
A sender wants to send a message. The sender breaks the message up into [[Network|packets]].  The sender [[Encryption|encrypts]] $m \in \Z_n$ (a [[Network|packet]]) into a [[Ciphertext|ciphertext]]
$$ C = m^e \mod n $$
using the receivers **public key**.

**Receiving**
The receiver wants to [[Decryption|decrypt]] the [[Ciphertext|ciphertext]] $C$, which they do by computing 
$$ m = C^{e^{-1}} \mod n $$
using their own **public** and **private key**.

> [!proof]- $C \equiv m^e \pmod n \implies C^{e^{-1}} \equiv m \pmod n$
> $$\begin{array}{l}
> 	\begin{align*}
> 		e^{-1}e \equiv 1 \pmod {\phi(n)} \\
> 	\end{align*} \\
> 	e^{-1}e - 1 = k\phi(n) && \exists k \in \Z \\
> 	e^{-1}e = k\phi(n) + 1 \\
> \end{array}$$
> Note that $C^{e^{-1}} \equiv \left(m^{e}\right)^{e^{-1}} \equiv m^{k\phi(n) + 1} \pmod n$, so by the [[#Lemma|lemma]], $C^d \equiv m \pmod n$.

> [!note] The security of this algorithm relies on the difficulty of prime factorisation (for $\phi(n)$) and finding roots (for solving $m$ from $m^e$).
# Lemma
For distinct [[Primes|primes]] $p,q$, if $n = pq$, for all integers $M$ and $k$, 
$$ M^{k\phi(n) + 1} \equiv M \pmod n $$
> [!proof]-
> By [[Lagrange's Theorem|Lagrange's theorem]], the order of each element, such as $M$, must have an order that divides $\left| \Z_{n}^\times \right| = \phi(n)$[^1]. Thus,
> $$\begin{align}
> 	M^{\frac{\phi(n)}{c}} &\equiv 1 \pmod n \\
> 	M^{k\phi(n)} &\equiv 1^{kc} \pmod n \\
> 	M^{k\phi(n)+1} &\equiv M \pmod n \\
> \end{align}$$

> [!proof]- 120
> **Case $\mathbf{I}$: $\mathbf{\textbf{gcd}(M,n) = 1}$**
> [[Euler's Theorem|Euler's theorem]] states that 
> $$\begin{align*}
> 	M^{\phi(n)} &\equiv 1 \pmod n \\
> 	M^{k\phi(n)} &\equiv 1 \pmod n \\
> 	M^{k\phi(n)+1} &\equiv M \pmod n \\
> \end{align*}$$
> 
> **Case $\mathbf{II}$: $\mathbf{\textbf{gcd}(M,n) \ne 1}$**
> Since $n = pq$ and $p,q \in \mathbb{P}$, $\gcd(M,n)$ is either $p$, $q$, or $pq$.
> 
> **Case $\mathbf{IIa}$: $\mathbf{\textbf{gcd}(M,n) = pq = n}$** 
> Since $n|M$[^3],
> $$\begin{align*}
> 	M &\equiv 0 \pmod n \\
> 	M^{k\phi(n)+1} &\equiv 0 \equiv M \pmod n \\
> \end{align*}$$
> **Case $\mathbf{IIb}$: $\mathbf{\textbf{gcd}(M,n) = p}$** $\hspace{2em}$ ($q$ analogous) 
> Since $p|M$[^3],
> $$\begin{align*}
> 	M &\equiv 0 \pmod p \\
> 	M^{k\phi(n) + 1} &\equiv 0 \pmod p \\
> \end{align*}$$
> Since $p|M$[^3] and $p|M^{k\phi(n)+1}$[^3] (see [[Congruence]]), $p|M^{k\phi(n)+1} - M$[^3].
> 
> We know that $\gcd(M,q) = 1$, as otherwise $\gcd(M,n) = pq$. Using [[Fermat's Little Theorem|Fermat's little theorem]],
> $$\begin{align*}
> 	M^{q-1} &\equiv 1 \pmod q \\
> 	\left(M^{q-1}\right)^{k(p-1)} &\equiv 1 \pmod q \\
> 	M^{k\phi(n)} &\equiv 1 \pmod q \\
> 	M^{k\phi(n)+1} &\equiv M \pmod q \\
> \end{align*}$$
> Thus both $p$ and $q$ [[Divisibility|divide]] $M^{k\phi(n)+1} - M$, so $pq$ must as well, meaning
> $$ M^{k\phi(n)+1} \equiv M \pmod n $$
> 
> \[[[Congruence]]\]


[^1]: [[Euler's Totient Function]]
[^3]: [[Divisibility]]
[^4]: [[Invertible Groups of Residue Classes]]