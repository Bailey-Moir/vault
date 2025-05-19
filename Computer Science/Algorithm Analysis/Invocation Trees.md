---
tags:
  - atom
  - comp
---
The *invocation [[Trees|tree]]* of a procedure/[[Algorithms|algorithm]] shows the calls (*invocations*) that are made by the procedure. It is [[Recursion|recursively]] defined as follows.
1. The [[Root|root]] of the [[Trees|tree]] corresponds to the call to the procedure (with the required arguments)
2. The [[Parent, Children, and Sibling Nodes|children]] of the [[Root|root]] from left to right are *invocation trees* corresponding to calls made by the [[Root|root]].

> [!note] The order in which the calls are **initiated** is given by a [[Tree Traversal#Pre-order|pre-order tree traversal]], and the order in which the calls are **completed** is given by a [[Tree Traversal#Post-order|post-order tree traversal]].

> [!example] [[Merge Sort]]
> ![1000|center](merge-sort-invocation-tree.excalidraw.md)
