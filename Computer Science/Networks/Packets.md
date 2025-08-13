---
tags:
  - atom
  - comp
---
Information is transmitted in *packets*: pieces of data that is passed through a [[Networks|network]] ($\approx 1000$ bytes).

They consist of:
- a **packet header** containing meta-information such as address fields,
- the **packet payload**, and
- possible a **packet trailer** for error detection/correction (e.g. checksums).

> [!definition] The **packet header** and **trailer** together are referred to as the **packet overhead**.