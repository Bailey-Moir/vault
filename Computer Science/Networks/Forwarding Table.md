---
tags:
  - atom
  - comp
---
The *forwarding table* maps [[IP|IP]] destination addresses to output ports, with each entry containing
- **Destination [[IP|IP]] Address** (a full [[Hosts|host]] address or a [[Networks|network]] address with [[Classless Inter-Domain Routing|netmask]]).
- **Next Hop [[IP|IP]] Address** (on its own [[Networks|network]] or otherwise)
- **Flags**
	- whether the destination is a [[Hosts|host]] or [[Networks|network]].
	- whether next-hop is a [[Routers|router]] or directly attached [[Networks|network]].
- **Specification of Outgoing Interface**

> [!usage]
> 1. Search for a matching [[Hosts|host]] address, and if one is not found
> 2. search for matching [[Networks|network]] address, and if one is not found
> 3. send to the **default** entry if it exists, otherwise
> 4. drop the [[Layered PDU Processing|datagram]].