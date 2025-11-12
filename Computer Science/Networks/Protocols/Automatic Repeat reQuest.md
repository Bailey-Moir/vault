---
tags:
  - atom
  - comp
---
[[Reliable Data Transmission|Reliable data transmission]] protocols based on retransmission are known as *ARQ* (*Automatic Repeat reQuest*). There are three key types: [[#Stop-and-Wait|stop-and-wait]] *ARQ*, [[#Go-back-N|go-back-n]] *ARQ*, and [[#Selective Repeat/Reject (SR)|selective repeat/reject]] *ARQ*.
## Stop-and-Wait
*Stop-and-wait ARQ* is a [[Reliable Data Transmission|rdt 2.0]] protocol.

> **Sender**
> 1. When the [[Packets|packet]] is ready to be sent, send it and wait for a **ACK**/**NAK**.
> 2. If **NAK** is received, go to step 1 (retransmission).
> 3. If **ACK** is received, wait for the next [[Packets|packet]] to be ready to send.

> **Receiver**
> If the [[Packets|packet]] is received without errors, send **ACK**, otherwise, send **NAK**.

> [!note] Sequence Numbers
> The **ACK**/**NAK** sent by the receiver can be corrupted, and then the receiver won't know if the subsequent [[Packets|packet]] sent by the sender is a retransmission, or if it's new.
> [[Reliable Data Transmission|rdt 2.1]]: To account for this, a 1-bit sequence number is added to the senders' [[Packets|packets]].
> [[Reliable Data Transmission|rdt 2.2]]: In fact, **NAK** can then be removed, as we can add the last succesfully received sequence number to the receivers' **ACK**s.

## Go-back-N
*Go-back-N ARQ* is a [[Reliable Data Transmission|pipeline protocol]].

The sender can send multiple [[Packets|packets]] without waiting for **ACK**, but can send no more than **N** unacknowledged [[Packets|packets]], determined by the number of bits in the sequence number.

An **ACK** with sequence number $n$ means all [[Packets|packets]] up to (and including) sequence number $n$ have been successfully received.

The receiver will discard any [[Packets|packets]] with incorrect sequence numbers (but still **ACK**).

If a timeout occurs on the sender, it will go back to the oldest unacknowledged [[Packets|packet]], and start sending from there.

If the **ACK** gets corrupted, fully restart from the start (how?).
## Selective Repeat/Reject (SR)
*Selective Repeat/Reject ARQ* is a [[Reliable Data Transmission|pipeline protocol]].

The receiver **ACK**s each individual correctly received [[Packets|packet]], buffering [[Packets|packets]] as needed to attempt in-order delivery to [[TCP-IP Reference Model|upper layer]].

Sender only resends un**ACK**ed [[Packets|packets]] packets based on a timer (one timer for each [[Packets|packet]]).

Similarly to [[#Go-back-N|go-back-n]], still maintains a sequence number and corresponding maximum number of un**ACK**ed [[Packets|packets]].

> [!note] Window size $\le \dfrac{1}{2}$ # of sequence numbers