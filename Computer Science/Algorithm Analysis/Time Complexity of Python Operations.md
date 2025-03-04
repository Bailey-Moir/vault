---
tags:
  - atom
  - comp
---

| **Operation**                            | **Complexity**            |
| ---------------------------------------- | ------------------------- |
| `=`                                      | $\Theta(1)$               |
| `+`,`-`,`*`,`/`,`//`,`abs`               | $\Theta(1)$               |
| List indexing                            | $\Theta(1)$               |
| List length                              | $\Theta(1)$               |
| List slice of length $k$                 | $\Theta(k)$               |
| List copy                                | $\Theta(n)$               |
| List `pop` and `append`                  | $\Theta(1)$               |
| List `pop`                               | $\Theta(1)$               |
| List `pop` and `insert` at $k \in [0,n)$ | $\Theta(n-k)$             |
| List membership `in`                     | $O(n)$                    |
| Set membership (`in`)                    | $\Theta(1)$               |
| `min`, `max`, `sum`                      | $\Theta(n)$               |
| `sort`, `sorted`                         | $\Omega(n)$, $O(n\log n)$ |
