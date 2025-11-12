---
tags:
  - atom
  - comp
---
The *forwarding table* maps [[IPv4|IPv4]] destination addresses to output [[Ports|ports]], with each entry containing
- **Destination [[IPv4|IPv4]] Address** (a full [[Hosts|host]] address or a [[Networks|network]] address with [[Classless Inter-Domain Routing|netmask]]).
- **Next Hop [[IPv4|IPv4]] Address** (on its own [[Networks|network]] or otherwise)
- **Flags**
	- whether the destination is a [[Hosts|host]] or [[Networks|network]].
	- whether next-hop is a [[Routers|router]] or directly attached [[Networks|network]].
- **Specification of Outgoing Interface**

> [!usage]
> 1. Search for a matching [[Hosts|host]] address, and if one is not found
> 2. search for matching [[Networks|network]] address, and if one is not found
> 3. send to the **default** entry if it exists, otherwise
> 4. drop the [[Layered PDU Processing|datagram]].

> [!note] The *forwarding table* results from the [[Routing Protocols|routing protocol]].