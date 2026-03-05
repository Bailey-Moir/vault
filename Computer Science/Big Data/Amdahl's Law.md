---
tags:
  - atom
  - comp
---
![600|center](amdahls-law)
If $s$ is the [[Proportion|proportion]] of program that is "inherently sequential", and $p$ is the number of processors, then the [[Parallel Speedup|speedup]] $S$ is given by
$$S = \dfrac{1}{s + \dfrac{1-s}{p}} \le \dfrac{1}{s}.$$
> [!example] If 10% of the program is "inherently sequential", even if the rest of the program ran with linear scalability (???) and infinite processors, the maximum [[Parallel Speedup|speedup]] would be $10$. #TODO