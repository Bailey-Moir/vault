---
tags:
  - atom
  - math
---
For a [[Continuity|continuous]] [[Functions|function]] $f$ defined on $\left[ 0,T \right]$ such that $\int_{0}^Tf^2(t)\,dt < \infty$, the $n$-th order [[Periodic Functions|periodic]] *Fourier approximation* of $f$ is
$$F_{n} = \text{proj}_{\text{span}\,S_{n}}(f)$$
where $S_{n} = \{ 1,\cos \dfrac{2\pi}{T}t,\sin \dfrac{2\pi}{T}t,\dots,\cos \dfrac{2\pi n}{T}t,\sin \dfrac{2\pi n}{T}t \}$ is a **Fourier basis**.

\[[[Distance to a Subspace]], [[Vector Projection]], [[Inner Products]]\]

> [!lemma]- $S_{n}$ is [[Orthogonal Vectors|orthogonal]] \[see [[Subspace Projection]]\]
> The [[Inner Products|inner product]] of any two [[Math/Linear Algebra/Vectors/Vectors|vectors]] in $S_{n}$ can be given by one of
> $$\begin{array}{ccc}
> 	\left< \text{cos} \dfrac{2\pi}{T}jt,\cos \dfrac{2\pi}{T}kt \right> &
> 	\left< \text{sin} \dfrac{2\pi}{T}jt,\cos \dfrac{2\pi}{T}kt \right> &
> 	\left< \text{sin} \dfrac{2\pi}{T}jt,\sin \dfrac{2\pi}{T}kt \right>
> \end{array}$$
> for $j,k \in \N \le n$.
> $$\begin{align}
> 	\left< \sin \dfrac{2\pi}{T}jt,\cos \dfrac{2\pi}{T}kt \right> &= \int_{-\pi}^\pi \sin \dfrac{2\pi}{T}jt \cos \dfrac{2\pi}{T}kt \, dt \\
> 	&= \dfrac{1}{2}\int_{-\pi}^\pi \sin\left(\dfrac{2\pi}{T}jt-\dfrac{2\pi}{T}kt\right) + \sin\left(\dfrac{2\pi}{T}jt+\dfrac{2\pi}{T}kt\right) \, dt && (1) \\
> 	&= \dfrac{1}{2}\int_{-\pi}^\pi \sin\left[\dfrac{2\pi}{T}(j-k)t\right] + \sin\left[\dfrac{2\pi}{T}(j+k)t\right] \, dt \\
> 	&= 0 && (2) \\
> \end{align}$$
> If $j \ne k$,
> $$\begin{align}
> 	\left< \sin \dfrac{2\pi}{T}jt,\sin \dfrac{2\pi}{T}kt \right> &= \int_{-\pi}^\pi \sin \dfrac{2\pi}{T}jt \sin \dfrac{2\pi}{T}kt \, dt \\
> 	&= \dfrac{1}{2}\int_{-\pi}^\pi \cos\left(\dfrac{2\pi}{T}jt-\dfrac{2\pi}{T}kt\right) - \cos\left(\dfrac{2\pi}{T}jt+\dfrac{2\pi}{T}kt\right) \, dt && (1) \\
> 	&= \int_{0}^\pi \cos \left[ \dfrac{2\pi}{T}(j-k)t \right] - \cos \left[ \dfrac{2\pi}{T}(j+k)t \right] \, dt && (2) \\
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

> [!note] ***Fourier* Coefficients**
> $$\begin{align}
> 	F_{n} = \dfrac{1}{2}a_{0} + a_{1}\cos\left( \dfrac{2\pi}{T} t \right) + b_{1}\sin \left( \dfrac{2\pi}{T}t \right) + \cdots  \\
> 	+\; a_{n}\cos\left( n\dfrac{2\pi}{T}t \right) + b_{n}\sin\left(  n\dfrac{2\pi}{T}t \right)
> \end{align}$$
> where
> - $\displaystyle a_{k} = \dfrac{\left< \cos \frac{2\pi}{T}kt,f \right>}{\left< \cos \frac{2\pi}{T}kt, \cos \frac{2\pi}{T}kt \right>} = \dfrac{2}{T}\int_{0}^T \cos\left(\dfrac{2\pi}{T}kt\right)f(t) \, dt$,
> - $\displaystyle b_{k} = \dfrac{\left< \sin \frac{2\pi}{T}kt,f \right>}{\left< \sin \frac{2\pi}{T}kt, \sin \frac{2\pi}{T}kt \right>} = \dfrac{2}{T}\int_{0}^T \sin\left(\dfrac{2\pi}{T}kt\right)f(t) \, dt$.
> 
> \[[[Vector Projection]]\]

> [!note]- ***Fourier* Coefficients** (when $T = 2\pi$)
> $$F_{n} = a_{0} + a_{1}\cos t + b_{1}\sin t + \dots + a_{n}\cos nt+b_{n}\sin nt$$
> where
> - $\displaystyle a_{0} = \dfrac{\left< 1,f \right>}{\left< 1,1 \right>} = \dfrac{1}{2\pi}\int_{-\pi}^\pi f(t) \, dt$,
> - $\displaystyle a_{k} = \dfrac{\left< \cos kt,f \right>}{\left< \cos kt,\cos kt \right>} = \dfrac{1}{\pi}\int_{-\pi}^\pi \cos(kt)f(t) \, dt$,
> - $\displaystyle b_{k} = \dfrac{\left< \sin kt,f \right>}{\left< \sin kt,\sin kt \right>} = \dfrac{1}{\pi}\int_{-\pi}^\pi \sin(kt)f(t) \, dt$,
> 
> \[[[Vector Projection]]\]