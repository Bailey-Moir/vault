---
tags:
  - atom
  - comp
---
Given a [[Sets|set]] of points in some [[Metric Spaces|metric space]] $X$, we will try to [[Partitions|partiton]] them into $k$ clusters of points. This is done by doing the following:
1. Initalize $k$ *clusters* by assigning each one point (ideally as far away from one another as possible).
2. Place each point in the *cluster* whose centroid is nearest.
3. Update the centroids of each *cluster*.
4. Reassign each point to the *cluster* whose centroid is nearest.
5. Repeat 3 and 4 untill convergence.