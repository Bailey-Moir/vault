---
tags:
  - atom
  - comp
---
*Market-basket models* describe data with
- one large [[Sets|set]] of **item**, and
- a large [[Sets|set]] of small [[Subsets|subset]] called **baskets**.

> [!example] **item** = products, **basket** = trolleys

> [!definitions]
> - The **support** for an itemset $I$ is the fraction of baskets containing $I$.
> - A **frequent** itemset is an item above a certain **support** threshold.
^support-and-frequent
# Association Rules
An **association** is a statement about an itemset $I$ and item $j$: "if a **basket** contains $I$, it is likely to contain $j$". This likelihood is given by the **association**'s **confidence**, given by
$$\text{conf}(I \to j) = \dfrac{\text{support}(I \cup j)}{\text{support}(I)}.$$
\[[[Conditional Probability]]\]

How **interesting** an **association** is given by
$$\text{Interest}(I \to j) = \text{conf}(I \to j) - \text{support}(j).$$