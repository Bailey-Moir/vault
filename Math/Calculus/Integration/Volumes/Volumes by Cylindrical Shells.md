---
tags:
  - atom
  - math
---
A method of [[Volumes of Revolution]] using sums of cylindrical shells. Note this method **rotates around the $\bf{y}$-axis**.
![350|center](cylindrical-volume.excalidraw)
$$ V = 2\pi \int_a^b xf(x) \, dx $$
> [!proof]-
> For a given point $x$, the circle formed when rotating around the $y$-axis has the circumference $2\pi x$. For each of these 1-dimensional points, we need to add a volume. This is achieved by multplying a height of $f(x)$, and a depth of $\Delta x$. Note that this can also be thought of as summing the areas (just like in $\int f(x) \, dx$), but each area is made into a volume by multiplying it by the circumference of a circle about the $y$-axis at that point. 
> $$ \lim_{n\to\infty} \sum_{i=0}^{n} 2\pi x_i^* f(x_i^*) \Delta x = 2\pi \int xf(x) \, dx $$
> \[[[Integration by First Principals]]\]

\[[[Volumes by Disks]]\]