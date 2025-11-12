---
tags:
  - atom
  - comp
---
![600|center](IPv6-packet.excalidraw.md)
> [!note] *IPv6* Addresses
> ![600|center](IPv6-address.excalidraw.md)

> [!note]- Fields
> - **Version** $= 6$ (`0110`)
> - **Traffic Class** is for [[Typical QoS Requirements|QoS]].
> - **Flow Label** marks groups of packets?
> - **Payload Length** gives the length of the payload **in bytes**.
> - **Next Header** gives the *IPv6* equivalent of Protocol Type from [[IPv4|IPv4]] ([[Protocols|protocol]] [[Multiplexing|multiplexing]]), **or the extension header**.
> - **Hop Limit** gives the *IPv6* equivalent of TTL from [[IPv4|IPv4]].
> - **Source Address** & **Destination Address** are 128 bit *IPv6* addresses.

> [!note] Unlike [[IPv4|IPv4]], in *IPv6*, [[IPv4#Fragmentation and Reassembly|fragmentation and reassembly]] happen only at end [[Hosts|hosts]], meaning there is no need for the Flags field from [[IPv4|IPv4]].
## Dual-Stack Approach
When an *IPv6* [[Packets|packet]] needs to be sent through an [[IPv4|IPv4]] [[Routers|router]], it is converted to an [[IPv4|IPv4]] [[Packets|packet]], and it is converted back when being sent through an *IPv6* [[Routers|router]], which **will loose information**.
## Tunnelling
When an *IPv6* [[Packets|packet]] needs to be sent through an [[IPv4|IPv4]] [[Routers|router]], it is wrapped in an [[IPv4|IPv4]] [[Packets|packet]], specifying that a *IPv6* [[Packets|packet]] is contained using the Protocol Type [[IPv4|IPv4]] field.