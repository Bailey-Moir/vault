---
tags:
  - comp
---
The width of the stock `int` type is inconsistent. The *standard integer library* `<stdint.h>` includes the types:
- `int32_t`, a 32-bit integer,
- `int16_t`, a 16-bit integer, and
- `int8_t`, an 8-bit integer.

> [!note] `u` can be added before any of these types (e.g. `uint32_t`) to make them unsigned, [[Two's Complement Signed Integers|doubling the largest number]].