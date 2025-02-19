---
tags:
  - atom
  - math
  - discrete
  - comp
---
*AES* is performed by doing the following process multiple timeswith different keys:
Represent the [[Plaintext|plaintext]] as a square [[Matrices|matrix]] $A$. Let $B$ be given by some [[Substitution Ciphers|substitution]] (similar to the [[Vigenère Cipher|Vigenère cipher]]) and then shift the rows. The output of the iteration is then given by $A\times B$[^1].

[^1]: [[Matrix Multiplication]]
