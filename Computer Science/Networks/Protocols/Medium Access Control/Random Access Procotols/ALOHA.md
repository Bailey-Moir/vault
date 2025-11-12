---
tags:
  - atom
  - comp
---
*Pure ALOHA* sends the [[Packets|packet]] with a [[Encoding#Checksums, Hash Totals|checksum]], transmitting immediately, and starting an acknowledgement timer.
- If the receiver successfully receives a [[Packets|packet]] without error, it responds with an immediate acknowledgement.
- If the transmitter receives an immediate acknowledgement before the acknowledgement timer expires, the [[Layered PDU Processing#PDU Names|frame]] is removed.
- If the acknowledgement timer expires, the transmitter enters **backoff mode**: the transmitter chooses a **random** backoff time to wait for without action, and then re-transmitting. 

> [!intuition] Just send it, and if you're left on read, wait a bit (give them space) and send it again in a bit. If they keep ignoring you, give up.

\[[[Service Primitives#Confirmed Delivery Service]]\]