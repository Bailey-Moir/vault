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
While the medium isn't busy in the given **time slot**, it start transmission on that **time slot** with [[Probabilities|probability]] $p$.

> [!note] If the medium is idle, the number of time slots it waits is distributed with $\text{Geom}(p)$[^1].

## CSMA / CD
[[#P-Persistent CSMA|1-persistent]], but if a collision is detected during transmission (detected as a higher voltage than expected), then:
- abort transmission and send a jamming signal.
- increment the a collision counter,
- if the counter is less than 16, wait a random backoff time ([[#Non-Persistent CSMA|non-persistent]]) and try again, otherwise drop the frame.

> [!note] The backoff time is a random integer from in $\left[ 0,2^{\text{min}\{ 10,\text{coll} \}} \right)$ time slots, meaning the average backoff time doubles after every collision (up to 1023).

> [!note] This is used by [[Ethernet|ethernet]].

[^1]: [[Geometric Random Variable]]
