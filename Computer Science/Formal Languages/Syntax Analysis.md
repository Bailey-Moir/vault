---
tags:
  - atom
  - comp
---
The second stage of [[Compilers|compiling]] is *syntax analysis*, performed by the **scanner**. It calls the [[Syntax Analysis|scanner]] to deliver tokens when needed, producing a abstract syntax [[Trees|tree]] according

The syntactic structure is described in **Backus-Naur form** (**BNF**), a set of [[Context-Free Grammar|grammar]] rules.

> [!example]-
> $$\begin{align}
> 	\text{Expression} &\to \text{Expression}\;\text{Arithmetic}\;\text{Expression}|\text{Expression}|\text{number}|\text{identifier} \\
> 	\text{Arithmetic} &\to +|-|*|\;/ \\
> 	\\
> 	\text{Comparison} &\to \text{Expression} \; \text{Relation} \; \text{Expression} \\
> 	\text{Relation} &\to \;=|!=|<|<= | > | >= \\
> 	\\
> 	\text{Statements} &\to \text{Statement}|\text{Statement}; \; \text{Statments} \\
> 	\text{Relation} &\to \text{If}|\text{While}|\text{Assignment} \\
> 	\text{Assignment} &\to \text{identifier} = \text{Expression} \\
> 	\text{While} &\to \text{while Comparison do Statements end} \\
> 	\text{While} &\to \text{if Comparison then Statements else Statements end} \\
> \end{align}$$