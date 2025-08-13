---
tags:
  - atom
  - comp
---
![1000|center](osi-model.excalidraw)
## Physical Layer
Concerned with transmission over physical media.
- Cable types (wired) or frequencies / bandwidth (wireless)
- Connectors
- Electrical specifications
- Modulation / demodulation and signal specification
- Carrier- or bit synchronization methods

## Link Layer
Transfer of messages over one physical link, which are referred to as **frames** during the linking stage.
- Framing:
	- delineation of frame start and end
	- choice of frame size
	- frame format
- Error control (e.g. coding- or retransmission-based)
	- Error-correction coding is also often regarded as a PHY functionality
- Medium access control
	- distributes right to send on shared channel to several participants
	- often considered as a separate “sub-layer” of link layer
- Flow control (hop-to-hop scope)
	- Avoid overwhelming a slow receiver with too much data

## Network Layer
Providing a [[#Link Layer|link]] technology-independent abstraction of entire network to higher layers, performing addressing and [[Routers|routing]].
- Addressing formats
- Exchange of routing information and route computation
- Depending on technology: establishment, maintenance and teardown of connections
## Transport Layer
- Error-control procedures
- Flow control procedures (end-to-end scope)
- Congestion control procedures.
## Session Layer
Establish/maintain communication sessions between applications, which can involve multiple [[#Transport Layer|transport layer]] connections.
## Representation Layer
Translates between data type representations (e.g. [[Big-endian and Little-endian Byte Ordering|endianness]]).
## Application Layer
Support functions useful for many applications (e.g. [[FTP|FTP]], directory services).
