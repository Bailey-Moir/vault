Conic sections are called *conic* sections because they are defined by the intersection of a plane and a *cone*.
![700|center](conic-sections.excalidraw.md)
# Conditions by Angle
Let $\phi$ be the angle between the $z$-axis and the top of the cone, and $\theta$ be the angle between the $z$-axis and the [[Vector Point-Normal Planes|normal vector]] of the plane. Then:
- when $\theta < \phi$, an [[Ellipse|ellipse]] (or [[Circle|circle]]) forms,
- when $\theta = \phi$, a [[Parabolas|parabola]] forms, and
- when $\theta > \phi$, a [[Hyperbola|hyperbola]] forms.

> [!note]- Alternative Definition by Gradients
> Let $P(x,y)$ define the plane, and $C(x,y)$ define the cone. Then:
> - an [[Ellipse|ellipse]] (or [[Circle|circle]]) forms iff $\left\| \nabla P \right\| < \left\| \nabla C \right\|$,
> - a [[Parabolas|parabola]] forms iff $\left\| \nabla P \right\| = \left\| \nabla C \right\|$, and
> - a [[Hyperbola|hyperbola]] forms iff $\left\| \nabla P \right\| > \left\| \nabla C \right\|$.

# Finding $\boldsymbol\phi$
The [[Level Curves|level curves]] of a cone are [[Circle|circles]] centered at the origin, with radii proportional to $z$[^1]. Thus, the cone can be defined as
$$x^{2}+y^{2} = (kz)^2$$
where $k$ is a scaling factor. Thus, the angle $\phi$ between the cone and the $z$-axis can be found using basic trigonometry.
![400|center](z-axis-to-cone.excalidraw)
$$\begin{align*}
	\tan \phi &= \dfrac{kz}{z} \\
	\phi &= \tan^{-1} k
\end{align*}$$
Alternatively, this can be found in terms of $\cos^{-1}$ like so:
$$\begin{align*}
	\tan \phi &= \dfrac{kz}{z} \\
	\tan^2 \phi &= k^2 \\
	\sec^2 \phi - 1 &= k^2 \\
	\dfrac{1}{\cos^2 \phi} &= k^2 + 1 \\
	\cos \phi &= \dfrac{1}{\sqrt{ k^2 + 1 }} \\
	\phi &= \cos^{-1}\dfrac{1}{\sqrt{ k^2 + 1 }} \\
\end{align*}$$
# Finding $\boldsymbol\theta$
If the [[Vector Point-Normal Planes|point-normal form]] of the plane is $\left( \vecbf{r} - \vecbf{r}_{0} \right) \cdot \vecbf{n}  = 0$, the angle between the normal and the $z$-axis can be found using the [[Cosine Similarity Formula|cosine similarity formula]]:
$$\begin{align*}
	\theta = \cos^{-1} \dfrac{\vecbf{n} \cdot \vecu{e}_{3}}{\left\| \vecbf{n} \right\| \left\| \vecu{e}_{3} \right\|} \\
	\theta = \cos^{-1} \dfrac{\vecbf{n}_{z}}{\left\| \vecbf{n} \right\|} \\
\end{align*}$$
# Conditions by Eccentricity
Instead of stating the conditions in terms of $\theta \gtrless \phi$, this can be substituted for
$$\begin{align*}
	\theta &\gtrless \phi \\
	\cos^{-1} \dfrac{\vecbf{n}_{z}}{\| \vecbf{n} \|} &\gtrless \cos^{-1} \dfrac{1}{\sqrt{ k^2 + 1 }} \\
	\dfrac{\vecbf{n}_{z}}{\| \vecbf{n} \|} &\gtrless \dfrac{1}{\sqrt{ k^2 + 1 }} \\
	\dfrac{\vecbf{n}_{z}}{\| \vecbf{n} \|}\sqrt{ k^2 + 1 } &\gtrless 1 \\
\end{align*}$$
In the field of conics, conic sections are defined by their **eccentricity** ($e$), which has its own definition, but: 
- when $e < 1$, an [[Ellipse|ellipse]] (or [[Circle|circle]]) forms,
- when $e = 1$, a [[Parabolas|parabola]] forms, and
- when $e > 1$, a [[Hyperbola|hyperbola]] forms,

Thus, $e = \dfrac{\vecbf{n}_{z}}{\| \vecbf{n} \|}\sqrt{ k^2 + 1 }$.

[^1]: [[Elliptic Cone]]