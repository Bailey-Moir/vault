---
tags:
  - atom
  - comp
---

| Code   | Meaning                                              |
| ------ | ---------------------------------------------------- |
| `%d`   | Decimal Integer                                      |
| `%x`   | [[Hexadecimal\|Hexadecimal]] Integer                 |
| `%u`   | Unsigned Decimal (Integer)                           |
| `%06u` | Zero Padded Unsigned Decimal (Integer)               |
| `%ld`  | Long Decimal Integer - for 64-bit integers           |
| `%lu`  | Long Unsigned Decimal - for 64-bit unsigned          |
| `%c`   | for characters (in a symbol form)                    |
| `%f`   | for floating-point in conventional display form      |
| `%.nf` | for floating-point up to $n$ decimal places          |
| `%e`   | for floating-point in (engineering) exponential form |
| `%p`   | Addresses as [[Hexadecimal\|hexadecimal]]            |
| `%x`   | Hexadecimal                                          |

Length sub-specifiers come before the ones above (but after the `%`)

| Code | Type with Length                             |
| ---- | -------------------------------------------- |
| hh   | signed char                                  |
| l    | long int                                     |
| ll   | long long int                                |
| j    | [intmax_t](https://cplusplus.com/intmax_t)   |
| z    | [size_t](https://cplusplus.com/size_t)       |
| t    | [ptrdiff_t](https://cplusplus.com/ptrdiff_t) |