---
tags:
  - atom
  - comp
---
![500|center](udp-segment.excalidraw)
*UDP* (*user datagram protocol*) offers largely the same service as [[IPv4]] (still has the 4 properties listed), (almost) only adding [[Ports|port numbers]].

> [!note] **Fields**
> - **Length** gives the length of the entire [[Layered PDU Processing#PDU Names|segment]], and
> - the optional **checksum** covers the whole [[Layered PDU Processing#PDU Names|segment]] as well as a conceptual IP pseudo-header (what the skib bro).


\[[[Sockets#Datagram Sockets]]\]