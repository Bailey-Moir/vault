---
tags:
  - atom
  - comp
---
The first stage of [[Compilers|compiling]] is *lexical analysis*, performed by the **parser**. It reads the source code character-by-character, producing a sequence of **tokens** to be fed to the [[Syntax Analysis|parser]].

> [!examples]- of Tokens
> - Keywords : `if`, `then`, `else`, `while`, `begin`, `true`, etc...
> - Symbols : `+`, `-`, `<`, `<=` `=`, `+=`, `(`, `)`, `{`, `}`, etc...
> - Identifiers : `n`, `sum`, `current_node_2`, `i`, etc...
> - Number Constants : `24`, `0xa5b3c2`, `2.99e8`, etc...
> - String Constants: `'Name'`, `"Date"`, `%d\n"`, etc...

These tokens are defined using [[Regular Expressions|regular expressions]], which can be [[Finite Automata From Regular Expressions|converted]] to an [[Non-Deterministic Finite Automata with Epsilon-Transitions|NFA]] with $\varepsilon$-transitions, which can then be [[Subset Construction|converted]] to a [[Deterministic Finite Automata|DFA]].
- The input is read until the dump state is reached, and then the last accept state is returned.
- If no accept state is every reached, the **scanner** reports a **lexical error**.