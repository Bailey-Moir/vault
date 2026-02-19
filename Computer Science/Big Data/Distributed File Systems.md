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

