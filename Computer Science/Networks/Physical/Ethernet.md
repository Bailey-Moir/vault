---
tags:
  - atom
  - comp
---
![1000|center](ethernet-packet.excalidraw)

The [[Layered PDU Processing#PDU Names|frame]] format for *Ethernet* contains a:
- **Preamble**
  Allows the receiver to [[Frame Synchronisation|synchronise]].
- **SOF** (Start of Frame)
- **SrcAddr** and **DstAddr**
  The address fields are each 6 bytes long. They are represented as six colon-separated hexadecimal bytes, e.g.
  $$\text{00:0c:29:10:fb:f3}$$ 
  If all bits are $1$s, then it is the [[Broadcasting|broadcasting]] address. 
  If the first bit is $1$ (and it's not the all $1$s), then it is a [[Multicast|multicast]] address.
  If the first bit is $0$, then it is a [[Unicasting|unicast]] address.
- **Length/Type**
  When the **L/T** field is $\ge \text{0x0600}$, it is interpreted as a type, indicating the higher-[[Layered PDU Processing|layer]] protocol that the payload is from. Otherwise, it just indicates the length of the payload, and the payload type is assumed to be in the first 2 bytes of the payload.

| Type Field      | [[Protocols\|Protocol]]              |
| --------------- | ------------------------------------ |
| $\text{0x0800}$ | [[IPv4\|IPv4]]                       |
| $\text{0x0806}$ | [[Address Resolution Protocol\|ARP]] |
| $\text{0x809B}$ | Apple Talk                           |
| $\text{0x86DD}$ | [[IPv6\|IPv6]]                       |
| $\text{0x8863}$ | PPPoE Discovery                      |
| $\text{0x8864}$ | PPPoE Session                        |
- **[[Packets|Payload]]**
- **FCS** (Frame Check Sequence)
  CRC [[Encoding#Checksums, Hash Totals|checksum]] (idk what that means).

> [!note] A minimum [[Layered PDU Processing#PDU Names|frame]] size is chosen to ensure transmitters can [[Carrier Sense Multiple Access|detect collisions]] while still transmitting (longer than the [[End-to-End Delay|round-trip]] delay + [[End-to-End Delay|processing delay]]). **See [[Broadcast Topologies]]**