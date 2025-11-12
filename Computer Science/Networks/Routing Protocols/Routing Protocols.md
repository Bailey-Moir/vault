---
tags:
  - atom
  - comp
---
*Routing* is the [[Networks|network]]-wide process that determines the **end-to-end** paths [[Packets|packets]] takes from source to destination.
## Routing Strategies
- **Fixed/Static Routing**
  A single permanent route is established for each source-destination pair, only changing when the topology changes.
- **Flooding**
  Every node acts as a [[Hubs|hub]], excluding the incoming link.
- **Adaptive/Dynamic Routing**
  Same as **fixed/static**, except it changes when it needs to (e.g. on congestion or failure).
- **Random Routing**
  Every node picks a random outgoing link, excluding the incoming link.

