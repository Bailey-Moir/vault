---
tags:
  - atom
  - math
---
The [[Math/Algebra/Basics/Intervals|closed interval]] $[0,1]$ is [[Countably Infinite Sets|uncountable]].

> [!proof]-
> Suppose the [[Math/Algebra/Basics/Intervals|interval]] is [[Countably Infinite Sets|countable]], and let $\left( a_{n} \right)$ be a [[Sequences|sequence]] that gives every element in it.
> 
> Let $I_{0} = [0,1]$, and $n = 0$.
> 
> 1. Divide $I_{n}$ into three (e.g.  if $n=0$, then $[0, \frac{1}{3}]$, $[\frac{1}{3}, \frac{2}{3}]$, and $[\frac{2}{3}, 1]$).
> 2. Select $I_{n+1}$ to be one of these [[Math/Algebra/Basics/Intervals|subintervals]] that **does not** contain $a_{1}$.
> 3. Increment $n$ and repeat.
> 
> By theorem 2.21, there is a $p \in \R$ such that $p \in I_{n}$ for all $n$, meaning the [[Sequences|sequence]] does not contain all [[The Real Numbers|the real numbers]] in $[0,1]$, so it is [[Countably Infinite Sets|uncountable]].