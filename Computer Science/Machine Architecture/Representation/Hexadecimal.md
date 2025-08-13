---
tags:
  - atom
  - comp
---
*Hexadecimal* is a base-16 counting system, with digits:
$$0,1,2,3,4,5,6,7,8,9,\text{A},\text{B},\text{C},\text{D},\text{E},\text{F}$$
> [!note-&-example]- Each [[Hexadecimal|hex-digit]] corresponds to four [[Binary|binary]] bits
> $8 = 1000$ and $F = 1111$, so
> - The number $10001111$ in [[Binary|binary]] is then $8F$ in [[Hexadecimal|hexadecimal]].
> - The number $F8$ in [[Hexadecimal|hexadecimal]] is then $11111000$ in [[Binary|binary]].


> [!python]-
> `bytes.fromhex()` converts hex to bytes.
> `.hex()` method converts bytes to hex.