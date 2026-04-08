---
tags:
  - atom
  - comp
---
![500|center](lsh-minhash-sig-target.excalidraw)
Given a [[Minhash Signatures|signature matrix]] $M$: 
- Choose a [[Jaccard Distance|similarity]] threshold $0 < s < 1$.
- Split $M$ into $b$ bands of $r$ rows.
- For each band, create $k$ buckets.
- [[Hash|Hash]] each column [[Vectors|vector]] of each band into one of the band's buckets such that [[Jaccard Distance|similar]] columns are more likely to [[Hash|hashed]] to the same bucket.
  The pairs that end up in the same bucket in at least one band are called **candidate pairs**.

Let $t = \text{SIM}(C_{1},C_{2})$. For these columns, the [[Probabilities|probability]] that all the rows in a given band are equal can be approximated (due to replacement) by $t^r$. Thus, the [[Probabilities|probability]] some row in  given band is different is $1 - t^r$.  Further, the [[Probabilities|probability]] that no band is identical can be approximated (due to replacement) by $(1 - t^r)^b$. Finally, the [[Probabilities|probability]] that at least $1$ band is identical, and thus of $\left( C_{1},C_{2} \right)$ being a **candidate pair** is $1 - \left( 1 - t^r \right)^b$. The point where this graph "transitions" from $0$ to $1$ can be approximated with $s \sim \left( 1/b \right)^{1/r}$.