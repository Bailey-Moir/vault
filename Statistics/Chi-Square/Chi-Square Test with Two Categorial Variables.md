---
tags:
  - atom
  - stats
---
This is the expected count if there is no difference between groups.
$$ \text{expected count} = \dfrac{\text{row total} \times \text{column total}}{\text{sample size}} $$
$$ \text{expected count for other group} = \text{column total}\left(1 - \dfrac{\text{row total}}{\text{sample size}} \right) $$
Now that the expected is found, the standard $\chi^2$-statistic[^1] formula can be used:
$$ \chi^2 = \sum\dfrac{(\text{observed} - \text{expected})^2}{\text{expected}} $$
The degrees of freedom of the resulting $\chi^2$-distribution[^2] is $df = (r-1)(c-1)$ where $r$ and $c$ are the number of rows and columns respectively (the number of categories in each of the two categorical variables).

[^1]: [[Chi-Square Statistic]]
[^2]: [[Chi-Square Distribution]]
