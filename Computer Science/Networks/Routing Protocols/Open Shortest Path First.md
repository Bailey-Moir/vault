---
tags:
  - atom
  - comp
---
![500|center](ospf.excalidraw)
*Open shortest path first* (*OSPF*) is an [[Exterior and Interior Routing Protocols|interior]] [[Link-State Routing|link-state]] [[Routing Protocols|routing protocol]]. Notably, *OSPF*:
- is authenticated,
- stores all shortest paths and splits between them to balance load,
- uses a user-configurable cost metrc, and
- allows an [[Autonomous Systems|AS]] to be divided into numbered areas.

> [!note] These areas are like sub-[[Autonomous Systems|AS]]s, each running their own version of *OSPF*.