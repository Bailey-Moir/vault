---
tags:
  - atom
  - comp
---
The *Boyer-Moore [[Algorithms|algorithm]]* is a [[Strings|string]] searching [[Algorithms|algorithm]] that compares the pattern from **right to left** using two types heuristics: 
- "bad character" heuristics, and 
- "good suffix" heuristics.

> [!usage]- Bad Character Heuristic
> If a mismatch occurs and the corresponding character in the text does not appear in the pattern [[Strings|string]] at all, the pattern can be shifted to the end.
> ![350|center](bad-character-heuristic-1.excalidraw.md)
> Further, if the corresponding character in the text does appear in the pattern string at some point, the pattern can be shifted to the rightmost occurrence of that character.
> ![550|center](bad-character-heuristic-2.excalidraw.md)
> However, we never want to shift the pattern backwards, so if the rightmost occurrence of the character appears after `j`, this doesn't help, and we need to slide the pattern forward by one, and restart.
> ![550|center](bad-character-heuristic-3.excalidraw.md)

We can use this heuristic by creating an array `delta1` that contains the distance **from the end of the pattern** to the rightmost occurrence of each character.

> [!example]- `delta1` for "gccgaga"
> | Symbol `s`  | 'a' | 'c' | 'g' | 't' |
> | ----------- | --- | --- | --- | --- |
> | `delta1[s]` | 0   | 4   | 1   | 8   |

Constructing this `delta1` is $O(m +\left| \Sigma \right|)$, as every character in $\Sigma$ needs to be initialised to m, and then every character of the pattern must be checked, only storing the maximum.

This gives
```python
delta1 = bad_char_shifts(pattern)
m = len(pattern)
i = m - 1
while i < len(text):
	j = m - 1
	while j >= 0 and pattern[j] == text[i]:
		i -= 1
		j -= 1
	if j < 0:
		print(i)
		i += m + 1
	else:
		i += Math.max(m - j, delta1[ord(text[i])])
```

However, this simplified version still has a [[Formal Definition of Best and Worst Case|worst case]] of $O(nm)$ with inputs like `T=aaaaaaaaa`, `P=baaa`.
 
> [!definition]- Good Suffix Heuristics
> As established, if a mismatch occurs and the rightmost occurrence of the corresponding character in the text appears on the right of $j$ in the pattern, then `delta1` can not be used, as this would shift the pattern backwards.
>  
> In the simplified version, the pattern is simply shifted by $1$, but instead, if the proper suffix of $P[j:]$ appears earlier in the pattern, **and** $P[k] \ne P[j]$ (where $k$ is the index of the rightmost occurrence of $P[j:]$), then the pattern can be shifted by $j-k$
> ![500|center](good-suffix-heuristic-1.excalidraw.md)
> If only part of the suffix appears at the beginning of the pattern (the pattern has a [[Knuth-Morris-Pratt Algorithm|border]] of length $b$), we can shift the pattern by a distance $m - b$
> ![625|center](good-suffix-heuristic-2.excalidraw.md)
> If the suffix doesn't appear anywhere else in the pattern, and the pattern doesn't have a border, then the pattern can safely be shifted by $m$
> ![625|center](good-suffix-heuristic-3.excalidraw.md)

We can use this heuristic by creating an array `delta2` that contains these shifts.

Finally, this gives the full *Boyer-Moore [[Algorithms|algorithm]]*
```python
delta1 = bad_char_shifts(pattern)
delta2 = good_suffix_shifts(pattern) # Not in course
m = len(pattern)
i = m - 1
while i < len(text):
	j = m - 1
	while j >= 0 and pattern[j] == text[i]:
		i -= 1
		j -= 1
	if j < 0:
		print(i)
		i += m + 1
	else:
		i += Math.max(delta2[j], delta1[ord(text[i])])
```