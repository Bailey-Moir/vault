---
tags:
  - atom
  - stats
---
Regression uses one or more [[Explanatory and Response Variables|explanatory]] [[Variable Types|quantitative variables]] ($x$) to predict one [[Explanatory and Response Variables|response]] [[Variable Types|quantitative variable]] ($y$).
- The **simple** part of simple linear regression means there will only be **one [[Explanatory and Response Variables|explanatory]]**.
- The **linear** part of simple linear regression means the prediction will be from a **linear approximation**.
$$ Y = \beta_0 + \beta_1X + \varepsilon $$
$$ Y \sim N(\beta_0 + \beta_1X, \sigma_\varepsilon) $$
$\beta_0 :=$ Population Intercept
$\beta_1 :=$ Population Slope
$\varepsilon :=$ Random Error / [[Residuals|Residual]]

$\beta_0$ and $\beta_1$ are found with the [[Least Square Lines|least square estimates]].

Watch out for:
- Departures from linearity.
- Consistently changing variability.
- Outliers and influential points.