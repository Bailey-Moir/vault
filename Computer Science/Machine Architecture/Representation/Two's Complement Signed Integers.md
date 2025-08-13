---
tags:
  - atom
  - comp
---
To invert the sign of an integer $x = 37$ of width $n$ with the *two's complement* method,
1. **Invert all the bits** ($2^n - 1 - x$)
   e.g. $00100101 \to 11011010$
2. **Add one** $(2^n  - x)$
   e.g. $11011010 \to 11011011$

To maintain a [[Bijective Functions|bijection]] between a representation its number, a *two's complement signed integer* of width $n$ has values from $-2^{n-1}$ to $2^{n-1}-1$ instead of from $0$ to $2^n-1$ as with unsigned integers (e.g. -128 to 127 instead of 0 to 255).

> [!definition] The leftmost bit is called the **sign bit** for 2 reasons:
> 1. Due to the restriction in range above, the **sign bit** is on iff the number is negative.
> 2. The value of a *two's complement signed integer* can be worked out the same way as with unsigned integers, but subtracting the value associated with the **sign bit** instead of adding it.
> > [!example]-
> > $$\begin{align}
> > 	1101 &= \mathbf{-(1\times 2^3)} + (1\times 2^2)  + (0\times 2^1)+ (1\times 2^0) \\
> > 	&= \mathbf{-(1\times 2^3)} + (1\times 2^2)  + (0\times 2^1)+ (1\times 2^0) \\
> > 	&= -8 + 4 + 0 + 1 \\
> > 	&= -3 \\
> > \end{align}$$

> [!note] These *signed integers* work with unsigned integer addition, subtraction, multiplication, and division.

> [!note] This is essentially working [[Modular Arithmetic|modulo]] $2^n$, except the numbers are restricted to $-2^{n-1}$ to $2^{n-1}-1$ to maintain uniqueness.

\[[[Binary]]\]