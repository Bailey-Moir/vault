---
tags:
  - atom
  - comp
---

![500|center](delay-components.excalidraw)
*End-to-end* delay is the time between generation of a [[Packets|packet]] at a source [[Hosts|host]] and its **reception at the destination**. Its components are:
- **Propagation Delay**
  Information is imparted on carrier signals. It is given by $\frac{d}{v}$.
  e.g. $v=c$, and $d = 5\,\text{km}$.
- **Transmission Delay**
  The number of bits divided by the bit rate of the modulation.
- **Processing Delay**
  The sum of the processing times each [[Stations|station]] a [[Packets|packet]] traverses takes.
- **Queuing Delay**
  The time the [[Packets|packet]] spends in the [[Routers|router]] [[Queues|queue]], waiting for other [[Packets|packets]] to be sent.

[[Circuit-Switching]]