---
tags:
  - atom
  - comp
---
In *broadcast topologies*, [[Stations|stations]] perform [[Passband Transmission|passband transmission]] in **half-duplex mode**, meaning [[Medium Access Control|MAC]] is needed, using [[Carrier Sense Multiple Access#CSMA / CD|CSMA/CD]].

> [!note] This is only used in $10 \text{ Mbps}$ PHYs (the bottom end of [[Ethernet|Ethernet]]), as the [[End-to-End Delay|propagation delay]] must smaller than the [[End-to-End Delay|transmission delay]] to be able to reliably [[Carrier Sense Multiple Access|detect collisions]], and a slow bit rate means a much larger [[End-to-End Delay|transmission delay]], meaning this condition is much easier to satisfy. 

> [!definition] A [[Stations|station]] in **half-duplex mode** switches between transmitting and receiving (but never both at the same time).