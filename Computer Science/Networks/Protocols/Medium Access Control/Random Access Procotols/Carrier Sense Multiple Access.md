---
tags:
  - atom
  - comp
---
With *carrier sense multiple access* (*CSMA*), it is assumed that all mediums can determine (almost instantaneously) the state of the medium. The operation of checking this state is called **carrier-sensing** (**CS**).

> [!intuition] Wait till the chat isn't being spammed.

> [!note] *CSMA* is most useful when [[End-to-End Delay|propagation delay]] is small (e.g. [[LAN|LAN]]). It is especially bad if it is greater than [[End-to-End Delay|transmission delay]].

## Non-Persistent CSMA
If the medium is busy (or a collision occurs), wait the entirety of a random backoff time (similar to [[ALOHA|ALOHA]]).

## P-Persistent CSMA
While the medium isn't busy in the given **mini slot**, it start transmission on that **mini slot** with [[Probabilities|probability]] $p$.

> [!note] If the medium is idle, the number of time slots it waits is distributed with $\text{Geom}(p)$[^1].

> [!important-note] $\mathbf{p \in \left( 0,1 \right)}$
## 1-Persistent CSMA
Sends as soon as medium is idle (no **mini slots**). On collision, 
- abort transmission and [[Broadcasting|broadcast]] a jamming signal (to inform all [[Stations|stations]] about the collision),
- and undergo a collision resolution procedure (e.g. [[Ethernet|Ethernet]] backoff schemes).
## CSMA / CD
[[#P-Persistent CSMA|1-persistent]], but if a collision is detected during transmission (detected as a higher voltage than expected), then:
- abort transmission and [[Broadcasting|broadcast]] a jamming signal,
- increment the a collision counter,
- if the counter is less than 16, wait a random backoff time ([[#Non-Persistent CSMA|non-persistent]]) and try again, otherwise drop the frame.

> [!note] The backoff time is a random integer from in $\left[ 0,2^{\text{min}\{ 10,\text{coll} \}} \right)$ **slot times**, meaning the average backoff time doubles after every collision.

> [!note] This is used by [[Ethernet|ethernet]].

[^1]: [[Geometric Random Variable]]
