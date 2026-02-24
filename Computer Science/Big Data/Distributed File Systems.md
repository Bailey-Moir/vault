---
tags:
  - atom
  - comp
---
![1000|center](chunk-servers.excalidraw)
In a *distributed file system*,
- files are split into contiguous chunks of about 16-64MB,
- chunks are stored in 2-3 different **chunk servers**, and
- metadata about where each file/chunk is stored is stored in the **master node**.

> [!-] **Chunk servers** also serve as compute servers.

> [!note] **Chunk servers** are organised into racks, typically intra-connected by gigabit [[Ethernet|ethernet]], and these racks are typically connected to each other by higher [[Bandwidth|bandwidth]] [[Ethernet|ethernet]].
