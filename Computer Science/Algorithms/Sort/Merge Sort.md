*Merge sort* splits the list in the middle and performs *merge sort* ([[Recursion|recursively]]). It then *merges* these two sorted halves in order.  

The merge is normally done by with a pointer in each list, adding the smaller of the two values and incrementing the pointer forward in the list that was taken from. The cases for merging are
- Best case $\frac{n}{2} = \mathcal{O}(n)$ as $n \to \infty$[^1] when the two lists are already sorted.
- Worst case $n - 1 = \mathcal{O}(n)$ as $n \to \infty$.[^1]

These merges are performed $\log_2n$ times, so
- Best case $T(n) = 2T(\frac{n}{2}) + \frac{n}{2} = \mathcal{O}(n\log n)$ as $n \to \infty$.[^1]
- Worst case $T(n) = 2T(\frac{n}{2}) + n-1 = \mathcal{O}(n \log n)$ as $n \to \infty$.[^1]

[^1]: [[Landua's Big Oh Notation]]