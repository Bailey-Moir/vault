---
tags:
  - atom
  - comp
---
![400|center](circuit-switching.excalidraw)
The lifetime of a connection has 3 phases:
1. **Connection Setup**
   Identify route and reserve resources (e.g. bandwidth, processing capacity).
2. **Connection Usage**
   Transmit [[Constant Bit Rate|CBR]] data through the established connection.
3. **Connection Teardown**
   Free the reserved resources.

> [!note] Well suited for [[Constant Bit Rate|CBR]] due to the reservation of resources, but not for [[Variable Bit Rate|VBR]], as when the traffic is low, resources are being wasted.

> [!note] Nobody uses this anymore.

\[[[Routers]] (Switches)\]