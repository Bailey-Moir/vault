---
tags:
  - atom
  - comp
---
![500|center](services-&-interfaces.excalidraw)
A layer $N$ offers an $\it{N}$*-service* *interface*, and the next layer $N + 1$ is only allowed to use the $\it{N}$*-interface*, but not any of the lower *interfaces* (e.g. the $\it{N − 1}$*-interface*).

> [!note] This "Exchange $N$-[[Layered PDU Processing|PDU]]" thing is actually fake. It creates the PDU and passes it to layer $N-1$, continuing all the way down to the [[TCP-IP Reference Model|physical layer]].