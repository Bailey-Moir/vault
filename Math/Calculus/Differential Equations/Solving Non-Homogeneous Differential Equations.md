---
tags:
  - atom
  - math
---
The [[General vs Particular Solution|general solution]] to a [[Homogeneous Differential Equations|non-homogeneous]] [[Linear Differential Equations|linear]] [[Ordinary Differential Equations|ODE]] problem always has a special structure that can be written as
$$y(x) = y_p(x) + y_h(x)$$
- The **particular solution**, $y_p$, is a [[General vs Particular Solution|particular solution]] (not [[General vs Particular Solution|general]] – no arbitrary constants) 
- The **[[Homogeneous Differential Equations|homogeneous]] solution**/complementary solution, $y_h$, contains all the constants of integration and is the [[General vs Particular Solution|general solution]] to the [[Homogeneous Differential Equations|homogeneous]] version of the DE.

The **particular solution** is found with [[Method of Undetermined Coefficients|the method of undetermined coefficients]], and the **homogeneous solution** is found using the corresponding [[Auxiliary Equations|auxiliary equation]] or [[Reduction of Order|reduction of order]].

> [!proof]- (ish)
> $$\begin{align}
> 	y(t) &= y_{p}(t) + y_{h}(t) \\
> \end{align}$$
> $$\begin{align}
> 	r(x)&=a_{2}(t)y'' + a_{1}(t)y' + a_{0}(t)y \\
> 	&=a_{2}(t)(y_{p}'' + cy_{h}'') + a_{1}(t)(y_{p}'+cy_{h}') + a_{0}(t)(y_{p}+cy_{h}) \\
> 	&= \left[ a_{2}(t)y_{p}''+a_{1}(t)y_{p}'+a_{0}(t)y_{p} \right]  + c\left[ a_{2}(t)y_{h}''+a_{1}(t)y_{h}'+y \right]  \\
> 	&= a_{2}(t)y_{p}''+a_{1}(t)y_{p}'+a_{0}(t)y_{p} 
> \end{align}$$
> The particular solution is not unique