*Quick sort* splits the list such that everything in the left list is smaller than everything in the right. It then performs *quick sort* ([[Recursion|recursively]]) on these lists, and then simply adds them back together after.

It splits by first picking a **pivot**. It then iterates through the list, adding it to a new left list if it is smaller than the pivot, and adding it to a new right list if it is greater than the pivot. This is $\mathcal{O}(n)$.

- **Worst-case**
  If the **pivot** picked is always the smallest value, this results in a total $\mathcal{O}(n^2)$.
- **Average & Best-case** $\mathcal{O}(n\log n)$
- **Extra Space** $\mathcal{O}(1)$ (for in-place *quicksort*)

*Quick sort* has a costly split and an inexpensive join, while [[Merge Sort|merge sort]] has an inexpensive split and a costly merge/join.

# Median of Three
An estimate of the [[Median|median]] a list can be estimated as the [[Median|median]] of three of the values. When implementing this, we chose this as the first, middle, and last element.