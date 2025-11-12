---
tags:
  - atom
  - comp
---
*Congestion control* attempts to avoid buffer overflow (or general queuing) in the [[Routers|routers]] of a [[Networks|network]], or deal with it optimally. There are two types:
- **Network-assisted _Congestion Control_**
  [[Routers|Routers]] provide feedback to the [[Hosts|end hosts]], such as a single bit indicating *congestion* at a link, or the explicit transmission rate supported on an outgoing link.
- **End-to-end _Congestion Control_**
  No explicit support from the [[OSI Seven Layer Model#Network Layer|network layer]], and *congestion* is inferred by the [[Hosts|end hosts]] based on observed [[Packets|packet]] loss and [[End-to-End Delay|delay]].

> [!definition] In [[Packet-Switching|packet-switching]], **congestion** is when a [[Routers|router]]'s memory is full or close to full, meaning [[Packets|packets]] must be dropped or packets queue for a long time.