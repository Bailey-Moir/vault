---
tags:
  - atom
  - comp
---
The second stage of [[Compiler Steps|compiling]] is *syntax analysis*, performed by the **parser**. It calls the [[Lexical Analysis|scanner]] to deliver tokens when needed, producing a abstract syntax [[Trees|tree]] according

The syntactic structure is described in **Backus-Naur form** (**BNF**), a set of [[Context-Free Grammars|grammar]] rules.

> [!example]-
> $$\begin{align}
> 	\text{Expression} &= \text{Expression}\;\text{Arithmetic}\;\text{Expression}|\text{Expression}|\text{number}|\text{identifier} \\
> 	\text{Arithmetic} &= +|-|*|\;/ \\
> 	\\
> 	\text{Comparison} &= \text{Expression} \; \text{Relation} \; \text{Expression} \\
> 	\text{Relation} &= \;=|!=|<|<= | > | >= \\
> 	\\
> 	\text{Statements} &= \text{Statement}|\text{Statement}; \; \text{Statments} \\
> 	\text{Relation} &= \text{If}|\text{While}|\text{Assignment} \\
> 	\text{Assignment} &= \text{identifier} = \text{Expression} \\
> 	\text{While} &= \text{while Comparison do Statements end} \\
> 	\text{While} &= \text{if Comparison then Statements else Statements end} \\
> \end{align}$$

> [!definition] An *extended BNF* (*EBNF*) has [[Regular Expressions|regular expressions]] on the right-hand side.