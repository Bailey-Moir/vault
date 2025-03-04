---
tags:
  - atom
  - math
  - discrete
---
To compute $a^m \mod n$[^1],
1. Write $m$ in binary
   $m = m_{k}2^k + \cdots + m_{0}2^0 = (m_{k}\cdots m_{0})_{2}$[^2]
2. Compute $a^{2^1},a^{2^2}, a^{2^3},\dots,a^{2^k}$ by successive squaring modulo $n$.
3. Then $a^m = a^{m_{k}2^k + \cdots + m_{0}2^0} = {a^{(2^k)}}^{m_{k}} \times \cdots \times {a^{(2^0)}}^{m_{0}}$

[^1]: [[Congruence]]
[^2]: [[Changing Base]]