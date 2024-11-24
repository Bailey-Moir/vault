---
tags:
  - atom
  - math
  - comp
---
A valid lambda calculus expression is called a *lambda term*.

The following rules given an inductive definition that can be applied to build all syntactically valid lambda terms:
- Variable $x$ is itself a *lambda term*.
- If $t$ is a *lambda term*, and $x$ is a variable, then ($\lambda x. t$) is a lambda term (called [[Lambda Abstraction|abstraction]])
- If $t$ and $s$ are *lambda terms*, then ($t\:s$) is a *lambda term* (called [[Application|application]]).

Terms are built using the following rules:
1. $x$: A variable is a character or string representing a parameter
2. $(\lambda x. M)$: A [[Lambda Abstraction|lambda abstraction]] is a function definition, taking as input the bound variable $x$ (between the $\lambda$ and the dot) and returning the body $M$.
3. $(M\:N)$: An [[Application|application]], applying a function $M$ to an argument $N$. Both $M$ and $N$ are *lambda terms*.