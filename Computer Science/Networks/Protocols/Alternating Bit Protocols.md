---
tags:
  - atom
  - comp
---
[[Reliable Data Transmission|rdt 3.0]]: If the sender does not receive an **ACK**/**NAK** within a set timeout, it retransmits. Sequence numbers are still used, but the sender doesn't respond when it receives an incorrect sequence number.

> [!note] This is essentially a [[Automatic Repeat reQuest#Stop-and-Wait|stop-and-wait ARQ]] protocol.