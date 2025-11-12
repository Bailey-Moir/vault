---
tags:
  - atom
  - comp
---
![500|center](tcp-segment.excalidraw)
*TCP* (*transmission control protocol*) extends upon the [[IPv4]] protocol, adding [[Ports|port numbers]] and making it
- Connection-oriented,
- Byte-stream oriented,
- [[Switched Topologies|Full-duplex]],
- Reliable (acknowledgement and retransmissions),
- Ordered (in-sequence), and
- [[Reliable Data Transmission|Pipelined]].
*TCP* does not respect data boundaries.

> [!note]- **Fields**
> - **Sequence #** & **Acknowledgement #** count bytes of data, not [[Layered PDU Processing#PDU Names|segments]].
> - **Header Length** gives the length of the header as a number of 32-bit [[Words|words]] (the padding on options is used to fill any gaps).
> - _**U** is for urgent data (generally ignored)_,
> - **A** is for ACKs,
> - _**P** is for pass data now (generally ignored)_,
> - **R**, **S**, & **F** are for **RST**, **SYN**, and **FIN** respectively, used for connection management,
> - **Receive Window** gives the number of bytes the receiver is willing to accept,
> - **Checksum** is an internet checksum, the same used in [[UDP|UDP]]. #TODO
> - _**Urg data pnter** is used for the **U** thing, which again, is generally ignored._

> [!note]- **3-way Handshake & Normal Closing**
> ![600|center](tcp-handshake-and-normal-closing.excalidraw.md)

> [!note]- **[[Reliable Data Transmission|Reliable Data Transmission]]**
> *TCP* uses [[Automatic Repeat reQuest#Selective Repeat/Reject (SR)|SR]], except
> - it uses cumulative ACKs (similar to [[Automatic Repeat reQuest#Go-back-N|GBN]]).
> - the ACK gives the next byte expected,
> - [[Layered PDU Processing#PDU Names|segments]] are retransmitted after receiving **three** (as opposed to one) of the same ACKs,
> - on timeout, only the [[Layered PDU Processing#PDU Names|segment]] with the smallest seq # is sent, and the timer is restarted **with double the wait time** (to prevent congestion),
> - the payload received is sent with the ACK, and the ACK is ACKed (this time without a payload).

> [!note]- **Calculating Timeout Value**
> The timeout value is given as a [[Functions|function]] of the round-trip time (RTT). This round-trip time is calculated by maintaining a [[Point Estimate|point estimate]] for the RTT $\text{EstimatedRTT}$ and the [[Standard Deviation|deviation]] $\text{DevRTT}$ by linearly interpolating to a new $\text{SampleRTT}$ when a (non-re) transmission is performed.
> $$\text{EstimatedRTT} = (1-\alpha) \times \text{EstimatedRTT} + \alpha \times \text{SampleRTT}$$
> $$\text{DevRTT} = (1-\alpha) \times \text{DevRTT} + \beta \times \left| \text{SampleRTT}-\text{EstimatedRTT} \right| $$
> This is an **exponential weighted moving average**, where usually $\alpha = 1.25$ and $\beta=2.5$.

> [!-]- **Flow Control v. [[Congestion Control|Congestion Control]]**
> Both of these are achieved by the sender by ensuring,
> $$ \text{LastByteSent} - \text{LastByteAcked} \le \min\{ \text{CongWin}, \text{RcvWin} \} $$ 
> where the $\text{RcvWin}$ gives the *flow control*, and the $\text{CongWin}$ gives the *[[Congestion Control|congestion control]]*.
> 
> *Flow control* is a speed-matching service, meaning the sender tries to match the sending rate to the receiver's reading rate. The receiver calculates the $\text{RcvWin}$ using
> ![400|center](tcp-flow-control.excalidraw)
> $$ \text{RcvWindow} = \text{RcvBuffer} - \left[ \text{LastByteReceived} - \text{LastByteRead} \right], $$ 
> where $\text{LastByteRead}$ is the last byte sent up to the [[OSI Seven Layer Model#Application Layer|application layer]].
> 
> ---
> 
> In contrast, *[[Congestion Control|congestion control]]* attempts to avoid buffer overflow (or general queuing) in the [[Routers|routers]] of a [[Networks|network]]. [[TCP|TCP]] achieves this with [[Congestion Control|end-to-end congestion control]] by adjusting $\text{CongWin}$.
> $$\text{Sending rate} = \dfrac{\text{CongWin}}{\text{RTT}} \text{ bytes/sec}.$$
> [[Congestion Control|Congestion]] is detected through **loss events**, which are when timeouts occur and when 3 duplicate ACKs are received.
> - Initially, $\text{CongWin} = 1 \text{ MSS}$ (maximum [[Layered PDU Processing#PDU Names|segment]] size). Then
> - **slow start** doubles $\text{CongWin}$ until the first **loss event** occurs, and then
> - **AIMD** (Additive-Increase, Multiplicative-Decrease) increases $\text{CongWin}$ by one $\text{MSS}$ on successful ACKs, and halves it on **loss events**.
> 
> This can be refined, by having a **slow start** threshold $\text{ssthresh}$, where if $\text{CongWin} < \text{ssthresh}$, **slow start** is used (otherwise **AIMD** is used). Then
> - on 3 duplicate ACKs, 
>   $\text{ssthresh} \leftarrow \text{CongWin}/2$ and
>   $\text{CongWin} \leftarrow \text{CongWin}/2 + 3 \text{ MSS}$, and
> - on a timeout event,
>   $\text{ssthresh} \leftarrow \text{CongWin}/2$ and
>   $\text{CongWin} \leftarrow 1 \text{ MSS}$.
  
\[[[Sockets#Stream Sockets]]\]