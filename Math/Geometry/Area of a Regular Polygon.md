---
tags:
  - atom
  - math
---
A *regular polygon* with $n$ sides and side lengths $s$ has an area given by
$$A = \dfrac{ns^2}{4\tan{\dfrac{\pi}{n}}}$$
> [!proof]-
> The polygon can be split into $n$ of the triangles below
> ![250|center](regular-polygon-area.excalidraw.md)
> By splitting this triangle down the center, the height $h$ can be calculated using basic trigonometry.
> $$\begin{align}
> 	\tan \dfrac{\pi}{n} &= \dfrac{s}{2h} \\
> 	h &= \dfrac{s}{2\tan \dfrac{\pi}{n}} \\
> \end{align}$$
> The area of the whole polygon can then by calculated as $n$ of these triangles.
> $$\begin{align}
> 	A &= n\times \dfrac{sh}{2} \\
> 	A &= \dfrac{ns^2}{4\tan \dfrac{\pi}{2}} \\
> \end{align}$$