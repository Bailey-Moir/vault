---
tags:
  - atom
  - comp
---
![600|center](IPv4-packet.excalidraw.md)
Each [[Hosts|host]] is identified by one or more *IP* (*internet protocol*) addresses. The *IP* address helps to identify the [[Hosts|host]], but also helps [[Routers|routers]] to find the path to the [[Hosts|host]] through the [[Networks|network]].

*IP* provides [[Packets|packet]] delivery, which is:
- Connectionless (not [[Circuit-Switching|circuit-switching]])
- Unacknowledged (no success, fail response or anything)
- Unreliable (no retransmissions)
- Unordered

> [!note]- Fields
> - **HdrLen** gives the length of the header as a number of 32-bit [[Words|words]] (the padding on options is used to fill any gaps).
> - **TOS/DSCP** is used for [[Typical QoS Requirements|QoS]], and is often ignored by [[Routers|routers]].
> - **Total Length** (of the fragment) is in bytes.
> - **Identification** gives the sequence number to group fragments (same across fragments).
> - **Flags** contains `DF` (Don't Fragment) and `MF` (More Fragments).
> - **Fragment Offset** gives the offset length of the current fragment within the entire [[Layered PDU Processing#PDU Names|datagram]] as a number of 8 bytes.
> - **Time-to-Live** (**TLL**) gives the maximum amount of [[Routers|routers]] the [[Packets|packet]] can traverse, decremented for each [[Routers|router]]
> - **Protocol Type** indicates the higher-layer [[Protocols|protocol]] that generated the payload, allowing for [[Protocols|protocol]] [[Multiplexing|multiplexing]].
> - **Header Checksum** is calculated over the header only (not the payload).

> [!Note] If `DF` is true and the packet is larger than the [[Maximum Transmission Units|MTU]], the [[Layered PDU Processing#PDU Names|datagram]] is dropped, and an [[Internet Control Message Protocol|ICMP]] message with type 3 and code 4 is sent to the **source address**, giving the [[Maximum Transmission Units|MTU]].
# Fragmentation and Reassembly
When the length is larger than the [[Maximum Transmission Units|maximum transmission unit]], *IP* splits the payload across multiple [[Packets|packet]] fragments, using **fragment offset** and the `MF` **flag**.

Intermediate nodes send fragments along, but the destination node creates a buffer according to the **total length**, and waits for the rest of the fragments to arrive. If they take too long to arrive, the fragments are dropped and an [[Internet Control Message Protocol|ICMP]] message with type 11 and code 1 is sent to the **source address**.
