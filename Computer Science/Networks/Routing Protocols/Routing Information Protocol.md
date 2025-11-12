---
tags:
  - atom
  - comp
---
*RIP* (*Routing Information Protocol*) is an [[Exterior and Interior Routing Protocols|interior]] [[UDP|UDP]] based [[Distance-Vector Routing|distance-vector]] [[Routing Protocols|routing protocol]] that uses the **[[Forwarding Tables|hop]] count** as its distance metric. There are two types of messages:
- a **request message** asking for all or part of a [[Routers|router]]'s *RIP* table, and a
- a **response message** (***RIP* advertisement**) can be a:
	- response to a **request message**,
	- regular update (unsolicited), or
	- update triggered by a [[Routing Protocols|route]] change.

> [!definition] For *RIP*, the **[[Forwarding Tables|hop]] count** is the number of [[Subnets|subnets]] traversed, including the destination.

> [!note] *RIP* solves the [[Distance-Vector Routing|count-to-infinity]] problem by 
> - setting a maximum **[[Forwarding Tables|hop]] count** of 15, using 16 to denote infinity,
> - not sending a neighbour the information learned from that neighbour, or
> - [[Distance-Vector Routing|poison reverse]].