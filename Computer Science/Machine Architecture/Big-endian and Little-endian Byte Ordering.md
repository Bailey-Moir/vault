---
tags:
  - atom
  - comp
---
*Little-endian* means the least significant bye is placed at the start, whereas *big-endian* means the most significant byte is placed at the start.

> [!analogy]
> If you think of bytes as base-256 numbers, the base-10 equivalent is
> - 120 in *big-endian* is stored in memory as 1,2,0
> - 120 in *little-endian* is stored in memory as 0,2,1.

> [!conversion]-
> - `htonl()` takes a long integer in [[Hosts|host]] *byte order* and converts it to [[Networks|network]] *byte order* (*big-endian*).
> - `htons()` takes a short integer in [[Hosts|host]] *byte order* and converts it to [[Networks|network]] *byte order* (*big-endian*).
> - `ntohl()` takes a long integer in [[Networks|network]] *byte order* (*big-endian*) and converts it to [[Hosts|host]] *byte order*.
> - `ntohs()` takes a short integer in [[Networks|network]] *byte order* (*big-endian*) and converts it to [[Hosts|host]] *byte order*.
> 
> where a short is 16-bits and a long is 32-bits.