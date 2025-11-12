---
tags:
  - atom
  - comp
---
- `malloc(n)` - allocate `n` bytes and return pointer. 
- `calloc(n,s)` - allocate `n` array of `s` bytes initialised to `0` and return pointer.
- `realloc(p,n)` - attempts to change the size of a [[Memory in C|heap]] pointer, giving the (potentially) new pointer.
- `memcpy(d,s,n)` - copy `n` bytes from `s` to `d`.
- `free(p)` - deallocate [[Memory in C|heap]] pointer.

\[[[Memory in C]]\]