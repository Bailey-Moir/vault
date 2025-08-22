---
tags:
  - atom
  - math
---
For a [[Continuity|continuous]] [[Functions|function]] $f$ defined on $\left[ -\pi,\pi \right]$, the $n$-th order *Fourier approximation* of $f$ is
$$F_{n} = \text{proj}_{\text{span}\,S_{n}}(f)$$
where $S_{n} = \{ 1,\cos t,\sin t,\dots,\cos nt,\sin nt \}$.

\[[[Distance to a Subspace]], [[Vector Projection]], [[Inner Products]]\]

> [!lemma]- $S_{n}$ is [[Orthogonal Vectors|orthogonal]] \[see [[Subspace Projection]]\]
> The [[Inner Products|inner product]] of any two [[Math/Linear Algebra/Vectors/Vectors|vectors]] in $S_{n}$ can be given by one of
> $$\begin{array}{ccc}
> 	\left< \text{cos} jt,\cos kt \right> &
> 	\left< \text{sin} jt,\cos kt \right> &
> 	\left< \text{sin} jt,\sin kt \right>
> \end{array}$$
> for $j,k \in \N \le n$.
> $$\begin{align}
> 	\left< \sin jt,\cos kt \right> &= \int_{-\pi}^\pi \sin jt \cos kt \, dt \\
> 	&= \dfrac{1}{2}\int_{-\pi}^\pi \sin(jt-kt) + \sin(jt+kt) \, dt && (1) \\
> 	&= \dfrac{1}{2}\int_{-\pi}^\pi \sin((j-k)t) + \sin((j+k)t) \, dt \\
> 	&= 0 && (2) \\
> \end{align}$$
> If $j \ne k$,
> $$\begin{align}
> 	\left< \sin jt,\sin kt \right> &= \int_{-\pi}^\pi \sin jt \sin kt \, dt \\
> 	&= \dfrac{1}{2}\int_{-\pi}^\pi \cos(jt-kt) - \cos(jt+kt) \, dt && (1) \\
> 	&= \int_{0}^\pi \cos((j-k)t) - \cos((j+k)t) \, dt && (2) \\
> 	&= \left[ \dfrac{1}{j-k}\sin((j-k)t) - \dfrac{1}{j+k}\sin((j+k)t) \right]^\pi_{0} \\
> 	&= \dfrac{1}{j-k}\sin(\pi(j-k)) - \dfrac{1}{j+k}\sin(\pi(j+k)) && j \pm k \in \Z \\
> 	&= 0 - 0 = 0 \\
> \end{align}$$
> and
> $$\begin{align}
> 	\left< \cos jt,\cos kt \right> &= \int_{-\pi}^\pi \cos jt \cos kt \, dt \\
> 	&= \dfrac{1}{2}\int_{-\pi}^\pi \cos(jt-kt) + \cos(jt+kt) \, dt && (1) \\
> 	&= \int_{0}^\pi \cos((j-k)t) + \cos((j+k)t) \, dt && (2) \\
> 	&= \left[ \dfrac{1}{j-k}\sin((j-k)t) + \dfrac{1}{j+k}\sin((j+k)t) \right]^\pi_{0} \\
> 	&= \dfrac{1}{j-k}\sin(\pi(j-k)) + \dfrac{1}{j+k}\sin(\pi(j+k)) && j \pm k \in \Z \\
> 	&= 0 + 0 = 0 \\
> \end{align}$$
> \[$(1)$ [[Product to Sum Identities]], $(2)$ [[Even and Odd Functions]]\]


> [!note] *Fourier* Coefficients
> $$F_{n} = a_{0} + a_{1}\cos t + b_{1}\sin t + \dots + a_{n}\cos nt+b_{n}\sin nt$$
> where
> - $\displaystyle a_{0} = \dfrac{\left< 1,f \right>}{\left< 1,1 \right>} = \dfrac{1}{2\pi}\int_{-\pi}^\pi f(t) \, dt$,
> - $\displaystyle a_{k} = \dfrac{\left< \cos kt,f \right>}{\left< \cos kt,\cos kt \right>} = \dfrac{1}{\pi}\int_{-\pi}^\pi \cos(kt)f(t) \, dt$,
> - $\displaystyle b_{k} = \dfrac{\left< \sin kt,f \right>}{\left< \sin kt,\sin kt \right>} = \dfrac{1}{\pi}\int_{-\pi}^\pi \sin(kt)f(t) \, dt$,
> 
> \[[[Vector Projection]]\]