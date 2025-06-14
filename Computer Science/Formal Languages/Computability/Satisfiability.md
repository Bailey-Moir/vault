---
tags:
  - atom
  - comp
---
The *satisfiability* problem (*SAT*) asks if a given a logical formula such as
$$\left( A \lor \neg B \right) \land \neg \left( B \lor \left( C \land \neg \left( A \lor B \right) \right) \right),$$
is a [[Contradictions|contradiction]] or not (if it can have its variables set so that it evaluates to true).

> [!naive algorithm]- $O(2^n)$
> The naive approach is to check every row of the corresponding [[Truth Tables|truth table]], but each variable can have $2$ possible values, meaning this would be $O(2^n)$ .

$$\begin{align}
	\text{Formula} &= \text{Formula} \land \text{Formula} \\
	&\hspace{0.5em}|\hspace{0.5em} \text{Formula} \lor \text{Formula} \\
	&\hspace{0.5em}|\hspace{0.5em} \neg \text{Formula} \\
	&\hspace{0.5em}|\hspace{0.5em} \text{variable} \\
\end{align}$$

> [!theorem] *SAT* (and *3-SAT*) is [[NP-complete]]. #TODO2 why?

> [!theorem]- $\text{3-SAT} =_{p} \text{SAT}$
> $\left( \text{3-SAT} \le_{p} \text{SAT} \right)$
> *SAT* is a more general version of *3-SAT*, so *SAT* decides *3-SAT*.
> 
> $\left( \text{SAT} \le_{p} \text{3-SAT} \right)$
> 1. Push down negations through the [[Syntax Diagrams|syntax tree]] using [[De Morgan's Laws|De Morgan's laws]] and cancelling double [[Negation|negations]].
> $$\begin{align}
> 	\neg \left( \neg A \land \left( B\lor  C \right) \right) &\iff \neg\neg A \lor \neg \left( B \lor C \right) \\
> 	&\iff A \lor \left( \neg B \land \neg C \right) \\
> \end{align}$$
> 2. Whenever there is a $\land$ inside of a $\lor$, replace the $\lor$ node with a new variable.
> $$\begin{align}
> 	X_{1} &\iff A\lor \left( \neg B \land \neg C \right) \\
> 	&\iff \left( A\lor X_{1} \right) \land \left( X_{2} \leftrightarrow \neg B \land \neg C \right) \\
> \end{align}$$
>    the RHS of this $\leftrightarrow$ can then be put into **conjunctive normal form** itself by doing step (1) on it, and using the [[Distributive Law|distributive law]].
> 3. Expand short clauses
> $$\left( \neg A \lor \neg B \right) = \left( \neg A \lor \neg B \lor Y \right) \land \left( \neg A \lor \neg B \lor \neg Y \right)$$

## 3-SAT
*3-SAT* is the same question as *SAT*, except the given formula is in **conjunctive normal form**, which has a [[Context-Free Grammars|grammar]] of
$$\begin{align}
	\text{CNF} &= \text{Clause}(\land \text{ Clause})^* \\
	\text{Clause} &=  \text{Literal}\lor\text{Literal}\lor\text{Literal} && (\text{Literal}(\lor \text{ Literal})^*) \\
	\text{Literal} &= \text{variable} \;|\; \neg\text{variable} \\
\end{align},$$
with exactly $3$ literals per clause.

> [!definition] **Conjunctive normal form** is a [[Conjunction|conjunction]] of [[Disjunction|disjunction]] of literals.
