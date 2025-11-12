---
tags:
  - atom
  - comp
---
*Border gateway protocol* (*BGP*) is an [[Exterior and Interior Routing Protocols|exterior]] [[TCP|TCP]] based [[Distance-Vector Routing|distance-vector]] [[Routing Protocols|routing protocol]]. It provides each [[Autonomous Systems|AS]] a way to

1. obtain the [[Subnets|subnet]] reachability information from neighbouring [[Autonomous Systems|AS]]s,
2. propagate this reachability information to all [[Routers|routers]] in the [[Exterior and Interior Routing Protocols|interior]] [[Autonomous Systems|AS]], and
3. determine "good" routes to [[Subnets|subnets]].

> [!note] 
> To initiate a connection between two neighbouring [[Routers|routers]] of different [[Autonomous Systems|AS]]s, one sends an **open message** to request to create a connection, and the other acknowledges this with a **keepalive message.**
> This **keepalive message** is sent periodically by each [[Routers|router]] to maintain the connection.

> [!note] *BGP* is the de facto [[Exterior and Interior Routing Protocols|exterior routing protocol]] for the [[Internet|internet]].
## Advertising Prefixes
In a *BGP* connection, one [[Routers|router]] can advertise a ([[Classless Inter-Domain Routing|CIDR]]) prefix to the other using *eBGP*, which also contains a
- **[[Autonomous Systems|AS]] Path** - the [[Autonomous Systems|AS]]s required to go through to get to the ([[Classless Inter-Domain Routing|CIDR]]) prefix
  (if the other [[Routers|router]] is in one of these [[Autonomous Systems|AS]]s, it rejects the advertisement), and a
- **[[Forwarding Tables|Next Hop]]** - the gateway [[Routers|router]] sending the advertisement.
## Choosing Prefix Route
The following criteria are used from most important to least important:
- highest local preference value,
- shortest [[Autonomous Systems|AS]] path,
- closest [[Forwarding Tables|next hop]] [[Routers|router]], and
- additional criteria we don't talk about.
## Capitalism Rule of Thumb
Any traffic flowing across an [[Internet Service Provider|ISP]]'s backbone [[Networks|network]] must have either a source or destination in a [[Networks|network]] that is a customer of that [[Internet Service Provider|ISP]].