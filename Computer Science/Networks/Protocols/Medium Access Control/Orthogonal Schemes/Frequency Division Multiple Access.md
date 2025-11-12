---
tags:
  - atom
  - comp
---
![600|center](fdma.excalidraw.md)
In *FDMA*, the given channel [[Bandwidth|bandwidth]] is subdivided into sub-channels (one per station), with margins around them called **guard bands**.

> [!note] The **guard bands** reduce adjacent-channel interference, and add margin for error in frequency [[Frame Synchronisation|synchronisation]].

> [!pros-vs.-cons]
> Stations can transmit in parallel without time synchronisation, but 
> - receivers need a separate receiver per station or a tunable receiver that can only listen to one station at a time, adding complexity,
> - sub-channels can't be shared (by owner or other transmitters), and
> - coordination of shared state is required to allocate sub-channels.

> [!note] *FDMA* is good for [[Constant Bit Rate|CBR]] but bad for [[Variable Bit Rate|VBR]].

> [!note] Completion Time
> Suppose the total available [[Bandwidth|bandwidth]] is $B\text{ bps}$, and it is subdivided into $N$ sub-channels. Then (ignoring **guard bands**), you are given a [[Bandwidth|bandwidth]] of $\dfrac{B}{N}$, so to send a [[Packets|packet]] of length $M\text{ b}$,
> $$E[\text{Transmission Delay}] = \dfrac{MN}{B}.$$
> Since the access delay is zero, this is then also the completion time.