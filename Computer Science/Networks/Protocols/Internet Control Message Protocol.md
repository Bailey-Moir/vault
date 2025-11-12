---
tags:
  - atom
  - comp
---
![600|center](ICMP-packet.excalidraw)
*Internet control message protocol* (*ICMP*) is for error messages and operational information about [[IPv4|IPv4]] [[Layered PDU Processing#PDU Names|datagram]] delivery. 
- **Type** and **Code** specify the *ICMP* message type and sub-type respectively.
- **Checksum** covers the *ICMP* header.

> [!example]- Type-Codes
> | Type | Code | Meaning                                         |
> | ---- | ---- | ----------------------------------------------- |
> | 0    | 0    | Echo reply                                      |
> | 3    | 0    | Destination [[Networks\|network]] unreachable   |
> | 3    | 1    | Destination [[Hosts\|host]] unreachable         |
> | 3    | 2    | Destination [[Protocols\|protocol]] unreachable |
> | 3    | 3    | Destination [[Ports\|port]] unreachable         |
> | 3    | 4    | Fragmentation disallowed by `DF`                |
> | 3    | 6    | Destination [[Networks\|network]] unknown       |
> | 3    | 7    | Destination [[Hosts\|host]] unknown.            |

> [!note] *ICMP* [[Packets|packets]] are wrapped in [[IPv4|IPv4]] [[Layered PDU Processing#PDU Names|datagrams]].