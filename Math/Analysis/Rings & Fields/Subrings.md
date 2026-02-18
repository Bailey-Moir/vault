---
tags:
  - atom
  - math
---
A *subring* of a [[Rings|ring]] $R$ is a [[Subsets|subset]] $S \subseteq R$ that is a [[Rings|ring]] under induced operations of $R$.

> [!theorem]- *(Subring Test)* A [[Empty Set|non-empty]] [[Subsets|subset]] of a given [[Rings|ring]] is a *subring* iff it is closed under its subtraction and multiplication.
> Let $R$ be a [[Rings|ring]], and $S \in \mathcal{P}(R)\setminus \{ \emptyset \}$.
> 
> $\left( \implies \right)$
> Suppose $S$ is a *subring* of $R$. Then every element has an inverse, and it is closed under addition, so it is closed under subtraction, and it is also closed under multiplication.
> 
> $\left( \impliedby \right)$
> Suppose $S$ is closed under subtraction and multiplication.
> All of the axioms of a [[Rings|ring]] are only refer to $R$ through a [[Universal Quantifier|universal quantifier]], so they also hold for $S$, except for: closure of addition and multiplication, inverses, and additive identity.
> - **Closure under Multiplication**
>   This is a premise, so it is given directly.
> - **Additive Identity**
>   Since $S$ is closed under subtraction, meaning $\forall a,b \in S, a-b \in S$, if you let $a = b$, this gives $0 \in S$. 
> - **Inverse**
>   Since $S$ is closed under subtraction, if you let $a = 0$ (which has been shown to be in $S$), this gives $-b \in S$.
> - **Closure under Addition**
>   For any $a,b \in S$, plugging $a$ and $-b$ (which has shown to be in $S$) into the closure under subtraction gives $a-(-b) \in S$, which by the [[Groups#^inverse-inverse|properties of groups]], gives $a + b \in S$.
  

^subring-test