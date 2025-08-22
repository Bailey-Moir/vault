---
tags:
  - atom
  - comp
---
![600|center](arp-packet.excalidraw)
*Address resolution protocol* (*ARP*) determines the [[Medium Access Control|MAC]] address for a given [[IP|IP]] address.

Each [[Stations|station]] maintains an **ARP cache**, mapping [[IP|IP]] addresses to [[Medium Access Control|MAC]] addresses, and entries are normally removed ~20 minutes after creation. 

> [!note] *ARP* [[Packets|packets]] are normally wrapped in [[Ethernet|Ethernet]] [[Packets|packets]] (not [[IP|IP]]). It is not restricted to [[Ethernet|Ethernet]], but in general is geared towards [[LAN|LANs]] with [[Broadcasting|broadcast]] capabilities.

> [!note]- Packet Fields
> - **Hardware Type** (**HardType**) determines the type of [[Medium Access Control|MAC]] address used (e.g. $\text{0x0001}$ is for [[Ethernet|Ethernet]] 48-bit addresses).
> - **Protocol Type** (**ProtType**) determines the higher-layer [[Protocols|protocol]] that *address resolution* needs to be done (e.g. $\text{0x0800}$ for [[IP|IP]]) for [[Protocols|protocol]] [[Multiplexing|multiplexing]].
> - **Hardware Size** (**HardSize**) and **Protocol Size** (**ProtSize**) give the size of the respective address types.
> - **Op** determines between *ARP*-request, *ARP*-reply, *RARP*-request, etc.

### Address Resolution Process
1. [[Stations|Station]] $A$ [[Broadcasting|broadcasts]] an *ARP* request indicating $A$'s [[IP|IP]] and [[Medium Access Control|MAC]] addresses, and $B$'s [[IP|IP]] address.
2. Some [[Stations|station]] $C$ may either discard this request or update $A$ in **cache**.
3. [[Stations|Station]] $B$ stores $A$ in its **cache**, and [[Unicasting|unicasts]] to $A$ with $A$ and $B$'s [[IP|IP]] and [[Medium Access Control|MAC]] addresses.