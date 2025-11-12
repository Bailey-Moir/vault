---
tags:
  - atom
  - comp
---
- **Detection Delay**
  Nodes do not detect failed links immediately, meaning packets can be forward into "black holes" (depends on timeout for detecting lost "hellos")
- **Inconsistent Link-State Database**
  Some nodes know about failure before others, meaning the shortest paths are no longer consistent.

> [!note] Nodes periodically send "hello" messages so that other nodes know they are on.