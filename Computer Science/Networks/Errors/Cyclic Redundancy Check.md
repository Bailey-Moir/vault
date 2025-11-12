---
tags:
  - atom
  - comp
---
*Cyclic redundancy check* (*CRC*), typically used in the [[OSI Seven Layer Model#Link Layer|link layer]], given a $k$-bit message, the
- **Transmitter**
  Generate an $\left( n-k \right)$-bit **frame check sequence** (**FCS**) such that the resulting [[Layered PDU Processing#PDU Names|frame]] is exactly [[Divisibility|divisible]] by some predetermined divisor.
- **Receiver**
  Assume there is no error if the incoming [[Layered PDU Processing#PDU Names|frame]] is [[Divisibility|divisible]] by the predetermined divisor.

> [!note] The divisor is chosen to be one bit longer than the **FCS**, where the highest-order bit must be `1`, and the lowest-order bit is normally `1`.

If $D$ is the $k$-bit message,
$$\mathbf{FCS} = D 2^{n-k} \mod P,$$
with the $2^{n-k}$ shifting $D$ to the left to make space for the **FCS**.

> [!note] We do this with long division (without carries).