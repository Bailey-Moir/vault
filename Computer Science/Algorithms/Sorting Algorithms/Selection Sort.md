---
tags:
  - atom
  - comp
---
*Minimum selection sort* [[Partitions|partitions]] the list into an empty sorted list, and the unsorted list. The minimum of the unsorted list is then found via a [[Sequential Search|sequential-like search]] and appended to the sorted list until the unsorted list is empty.
- The best, average, and worst case are all $T_{n-1} = \mathcal{O}(n^2)$[^1] as $n \to \infty$[^2].
```c
/* a[0] to a[aLength-1] is the array to sort */
int aLength; // initialise to a's length

int jMin = 0;
for (i = 0; i < aLength-1; i++) {
    for (j = i+1; j < aLength; j++)
        if (a[j] < a[jMin])
            jMin = j;

    if (jMin != i) 
        swap(&a[jMin], &a[i]);
}

return a[jMin]
```

[^1]: [[Triangular Numbers]]
[^2]: [[Landua's Big Oh Notation]]