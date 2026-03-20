---
tags:
  - atom
  - comp
---
Given a [[Minhash Signatures|signature matrix]] $M$: 
- Choose a [[Jaccard Distance|similarity]] threshold $0 < s < 1$.
- Split $M$ into $b$ bands of $r$ rows.
- For each band, create $k$ buckets.
- [[Hash|Hash]] each column [[Vectors|vector]] of each band into one of the band's buckets such that [[Jaccard Distance|similar]] columns are more likely to [[Hash|hashed]] to the same bucket. The pairs that end up in the same bucket are called **candidate pairs**.

The [[Probabilities|probability]] that all rows in a given band are equal can be approximated (due to replacement) by $t^r$. Thus, the [[Probabilities|probability]] some row in  given band is different 

Desired:
![400|center](lsh-minhash-sig-target.excalidraw)

$b=1$, $r=1$:
![400|center](lsh-minhash-sig-11.excalidraw)
