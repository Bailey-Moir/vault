---
tags:
  - atom
  - comp
---

![600|center](tdma.excalidraw.md)
In *TDMA*, the whole frequency spectrum (except [[Frequency Division Multiple Access|guard bands]] at either end) is used, but only at certain times. Time is divided into **superframes** that is subdivided into time-slots for each station to use, with **guard times** between them.

> [!note] The **guard times** reduce adjacent-channel interference, and add margin for error in time [[Frame Synchronisation|synchronisation]].

> [!pros-vs.-cons] 
> - Asymmetric [[Bandwidth|bandwidth]] assignment is easier than with [[Frequency Division Multiple Access|FDMA]], as it is easier to transmit at multiple times than on multiple frequencies at the same time.
> - **Faster completion time than [[Frequency Division Multiple Access|FDMA]]**\*. 
> - No complex hardware such as tunable receivers required.
> ---
> - Tight time-synchronisation between stations required.
> - High access delay in otherwise idle systems.
> - Not possible to reuse unused time slots.
> - Coordination of shared state is required to allocate time-slots.

> [!note] *TDMA* is good for [[Constant Bit Rate|CBR]] but bad for [[Variable Bit Rate|VBR]].

> [!note] Completion Time
> Suppose the total available [[Bandwidth|bandwidth]] is $B\text{ bps}$, and it is subdivided into $N$ time slots with superframe length of $T_{SF}$. Then (ignoring **guard times**), you are given a [[Bandwidth|bandwidth]] of $\dfrac{B}{N}$, so to send a [[Packets|packet]] of length $M$,
> $$\begin{align}
> 	E[\text{Access Delay}] &= \dfrac{T_{SF}}{2} \\
> 	E[\text{Transmission Delay}] &= \dfrac{M}{B} + T_{SF}\left( \left\lceil \dfrac{MN}{B} \right\rceil - 1 \right) \\
> 	\to E[\text{Completion TIme}] &= \dfrac{M}{B} + T_{SF}\left( \left\lceil \dfrac{MN}{B} \right\rceil - \dfrac{1}{2} \right) \\
> \end{align}$$