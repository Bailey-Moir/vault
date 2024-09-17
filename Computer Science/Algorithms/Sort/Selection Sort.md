*Minimum selection sort* works by finding the smallest element in the list via a [[Sequential Search|sequential-like search]], putting it at the start, and then doing the same for the rest of the list. *Maximum selection sort* does the same thing except it finds the largest elements, putting them at the end.
- The best, average, and worst case are all $T_{n-1} = \mathcal{O}(n^2)$^[[[Triangular Numbers]]] as $n \to \infty$.^[[[Landua's Big O Notation]]]
```c
/* a[0] to a[aLength-1] is the array to sort */
int i,j;
int aLength; // initialise to a's length

for (i = 0; i < aLength-1; i++) {
    int jMin = i;
    for (j = i+1; j < aLength; j++)
        if (a[jMin] > a[j])
            jMin = j;

    if (jMin != i) 
        swap(&a[jMin], &a[i]);
}
```