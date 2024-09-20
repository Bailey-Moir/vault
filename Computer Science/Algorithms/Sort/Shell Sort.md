---
tags:
  - atom
  - comp
---
*Shell sort* 'splits' a list of length $n$ list into [[Equivalence Classes|equivalence classes]] (shells) [[Congruence|modulo]] $1/2^i$, performing [[Insertion sort|insertion sort]] on each of the shells separately. The shells are determined by the [[Equivalence Classes|equivalence class]] of the index of each item [[Congruence|modulo]] $n/2$.
#TOD kms