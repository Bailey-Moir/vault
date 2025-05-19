---
tags:
  - atom
  - comp
---
- **Step 1**
  Write the [[Divide and Conquer|D&C]]/[[Recursion|Recursive]] [[Algorithms|algorithm]]'s **recurrence equation** for the running time of a given size in terms of the running times of smaller instances.
  
  In general, **recurrence equations** can be expressed as a [[Functions|function]] with two cases:
  1. Time to solve the smallest problem (base case) $= \Theta(1)$[^1]
  2. Time to solve a bigger problem (recursive case): $\text{time to divide} +\text{time to conquer} +\text{time to combine}$[^2]
- **Step 2**
  Combine the $\text{divide}$ and $\text{combine}$ terms into one term (picking the dominant term), and replace the [[Asymptotes|asymptotic notation]] with constant coefficients of their inner [[Functions|functions]]:
$$\Theta(g) \mapsto cg$$
- **Step 3**
  Expand the **recurrence equation** into a **recurrence tree** (similar to an [[Invocation Trees|invocation tree]] for the [[Divide and Conquer|D&C]] [[Algorithms|algorithm]]).

- **Step 4**
  Find the closed-form expression for the sum of the [[Vertices|nodes]] in the tree.

> [!example]- [[Merge Sort]]
> - **Step 1**
> $$T(n) = \left\{ \begin{array}{ll}
> 	\Theta(1) & \text{if } n=1 \\
> 	\Theta(1) + 2T(\frac{n}{2}) + \Theta(n) & \text{if } n>1
> \end{array} \right. $$
> - **Step 2**
> $$T(n) = \left\{ \begin{array}{ll}
> 	\Theta(1) & \text{if } n=1 \\
> 	  2T(\frac{n}{2}) + cn & \text{if } n>1
> \end{array} \right. $$
> - **Step 3**
> ![1000|center](recurrence-tree.excalidraw.md)
> - **Step 4**
> $$T(n) = \Theta(n\log n)$$

  
[^1]: [[Asymptotic Notation]]
[^2]: [[Divide and Conquer]]
