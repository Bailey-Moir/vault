---
tags:
  - atom
  - math
---
A [[Series|series]] $\Sigma a_{n}$ is said to be *absolutely convergent* iff the [[Series|series]] $\Sigma \left| a_{n} \right|$ is convergent. 
- If a [[Series|series]] is *absolutely convergent*, then the original series is convergent.
- If a [[Series|series]] is *absolutely convergent*, all rearrangements have the same sum. However, if a [[Series|series]] is *conditionally convergent*, it can be rearranged to give any real number.

> [!proof]-
> $$0\le a_{n} + \left| a_{n} \right| \le 2\left| a_{n} \right| $$
> If $\Sigma a_{n}$ is *absolutely convergent*, then $\Sigma 2| a_{n} |$ is also convergent. Therefore, by [[Comparison Theorem for Series#The Direct Comparison Test|the direct comparison test]], $\Sigma \left( a_{n} + \left| a_{n} \right| \right)$ is convergent. The original [[Sets|series]]
> $$\sum a_{n} = \sum \left( a+\left| a_{n} \right|  \right) - \sum \left| a_{n} \right| $$
> is then the difference of two convergent [[Series|series]], and is therefore convergent.

> [!note] $\Sigma a_{n}$ is **conditionally convergent** iff it is convergent but not *absolutely convergent.*