---
tags:
  - atom
  - comp
---
The *modularity* of an [[Directed Graphs|undirected]], [[Weighted Graphs|unweighted graph]] $G$ measures how well it is [[Partitions|partitioned]] into [[Community Detection|communities]] by a given [[Partitions|partition]] $\mathcal{C} \subseteq \mathcal{P}(V(G))$.
$$\begin{align}
	Q(G,\mathcal{C}) &\propto \sum_{\mathcal{C}_{1} \in \mathcal{C}} \left[ \left( \text{\# edges within } \mathcal{C}_{1} \right) - \left( \text{expected \# edges within group } \mathcal{C}_{1} \right) \right] \\
	&= \dfrac{1}{2m} \sum_{\mathcal{C}_{1} \in \mathcal{C}} \sum_{\left( u,v \right) \in V(\mathcal{C})^2} \left( A_{u,v} - \dfrac{\delta(u)\delta(v)}{2m} \right).
\end{align}$$
This [[Expected Value|expected]] number of [[Edges|edges]] requires a [[Null Models|null model]]. Using the [[#^null-model|construction below]], this gives the second line.

> [!construction]- [[Null Models|Null Model]]
> Let $G$ be an [[Directed Graphs|undirected graph]] with $n$ [[Vertices|vertices]] and $m$ [[Edges|edges]].
> Construct a rewired [[Directed Graphs|undirected]] [[Multigraphs|multigraph]] $G'$ from $G$, where each [[Vertices|vertex]] has the same [[Vertex Degrees|degree]], but each [[Edges|edge]] goes to a random [[Vertices|vertex]].
> 
> Then the [[Expected Value|expected]] number of [[Edges|edges]] between $u,v \in G'$ is given by
> $$\delta(u) \times \dfrac{\delta(v)}{2m} = \dfrac{\delta(u)\delta(v)}{2m},$$
> as each [[Edges|edge]] of $u$ can connect to any end of any [[Edges|edge]] (of which there are $2m$), but it would have to connect to one of $v$'s. Thus,
> $$ \begin{align}
> 	Q(G,\mathcal{C}) 
> 	&\propto \sum_{\mathcal{C}_{1} \in \mathcal{C}} \left[ \left( \text{\# edges within } \mathcal{C}_{1} \right) - \left( \text{expected \# edges within group } \mathcal{C}_{1} \right) \right] \\
> 	&\propto \sum_{\mathcal{C}_{1} \in \mathcal{C}} \left[ 
> 	\left( \sum_{\left( u,v \right) \in V(\mathcal{C})^2} \begin{cases}
> 	1 & (u,v) \in E(G) \\
> 	0 & (u,v) \notin E(G)
> 	\end{cases} \right) 
> 	-
> 	\left( \sum_{\left( u,v \right) \in V(\mathcal{C})^2} \dfrac{\delta(u)\delta(v)}{2m} \right) 
> 	\right] \\
> 	&\propto \sum_{\mathcal{C}_{1} \in \mathcal{C}} \sum_{\left( u,v \right) \in V(\mathcal{C})^2} \left( 
> 	 A_{u,v}
> 	-
> 	\dfrac{\delta(u)\delta(v)}{2m}
> 	\right). \\
> \end{align} $$
> where $A$ is an [[Adjacency Matrices|adjacencey matrix]] of $G$. Finally, we will multiply it by $\dfrac{1}{2m}$ to normialice $Q \in \left( -1,1 \right)$, giving
> $$ Q(G,C)  = \dfrac{1}{2m} \sum_{\mathcal{C}_{1} \in \mathcal{C}} \sum_{\left( u,v \right) \in V(\mathcal{C})^2} \left( A_{u,v} - \dfrac{\delta(u)\delta(v)}{2m} \right). $$
^null-model