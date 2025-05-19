---
tags:
  - atom
  - comp
---
A [[Syntax Analysis|parser]] can be implemented as a [[Sets|set]] of mutually [[Recursion|recursive]] functions. A *recursive-descent parser* is a [[Syntax Analysis|parser]] that built from a [[Sets|set]] of mutually [[Recursion|recursive]] functions, representing the non-terminals of the [[Syntax Analysis|(E)BNF]].

> [!example]- $$\begin{align} Expression &= Term \,((+\,|\,-)\,Term)^* \\ Term &= Factor \,((*\,|\,/)\,Factor)^* \\ Factor &= (Expression) \,|\, \text{number} \,|\, \text{identifier} \\ \end{align}$$
> ```py
> def expression():
> 	term()
> 	while lookahead() in [ADD, SUB]:
> 		consume(ADD, SUB)
> 		term()
> 	
> def term():
> 	factor()
> 	while lookahead() in [MUL, DIV]:
> 		consume(MUL, DIV)
> 		factor()
> 	
> def factor():
> 	if lookahead() == LPAR:
> 		consume(LPAR)
> 		expression()
> 		consume(RPAR)
> 	elif lookahead() == NUM:
> 		consume(NUM)
> 	elif lookahead() == ID:
> 		consume(ID)
> 	else:
> 		raise Exception
> ```
