---
tags:
  - atom
  - comp
---
Suppose the *p-segment* of the pattern $P[0:j]$ has matched with the corresponding portion of the text, and the match failed at $P[j]$, i.e. $T[i] \ne P[j]$.
![1000|center](p-segment.excalidraw)

If $B$ is the **widest** border of the matched *p-segment* of the pattern, the minimum shift worth trying is $j - \left| B \right|$.

> [!definition] Border
> A **border** of a [[Strings|string]] $P$ is a [[Strings|string]] that is both a proper prefix and proper suffix of $P$,
> *with proper meaning $P$ is not a proper prefix/suffix of $P$*.

Let $b[j]$ give the length of the widest border of the *p-segment* at position $j$. Thus, initialise it with with $b[0] = -1$ and $b[1] = 0$.
![500|center](p-segment-border-1.excalidraw)
Thus, $b[b[j]]$ give the length of the widest border nested within the previous border of length $b[j]$, and this repeats.
![500|center](p-segment-border-2.excalidraw)
This gives an [[Algorithms|algorithm]] for computing the widest border:
```python
def border_lengths(p):
	b = [0]*(len(p) + 1)
	b[0:2] = [-1, 0]
	j, bj = 1, 0
	while j < len(p):
		 # find widest border that we can be extend
		while bj >= 0 and p[j] != p[bj]:
			bj = b[bj]
		j, bj = j+1, bj+1
		b[j] = bj # increase the matched border length by one
	return b
```
This is $O(m)$, as the outer while loop repeats exactly $m$ ($\left| P \right|$) times, and the inner while loop decreases the value of $bj$ at most as often as it has been increased by the outer while loop.

Thus, the whole *Knuth-Morris-Pratt* [[Algorithms|algorithm]] is
```python
b = border_lengths(pattern)
i, j = 0, 0
while i < len(text):
	while j >= 0 and text[i] != pattern[j]:
		j = b[j]
	i, j = i+1, j+1
	if j == len(pattern):
		# Match found. Print position.
		print (i-j)
		j = b[j]
```
Overall, this is $O(n+m)$, as first it runs `border_lengths`, and similar to the `border_lengths` algorithm, the outer while loop of *KMP* repeats exactly $n$ ($\left| T \right|$) times, and the inner while loop decreases the value of $j$ at most as often as it is increased by the outer while loop.