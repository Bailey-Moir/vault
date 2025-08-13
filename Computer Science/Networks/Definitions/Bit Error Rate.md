---
tags:
  - atom
  - comp
---
The *bit error rate* (or *bit error [[Probabilities|probability]]*) is the rate at which the receiver interprets bits incorrectly (due to noise in the communication channel).

> [!note]- For a [[Packets|packet]] with $I$ bits, the [[Probabilities|probability]] of at least one error being interpreted incorrectly is $1 - (1-p)^I$ where $p$ is the *bit error rate*.
> Bit loss can be modelled with a [[Binomial Random Variable|binomial random variable]] $X$ with $I$ trials and [[Probabilities|probability]] of success (*bit error probability*) being $p$, so the [[Probabilities|probability]] at least one bit is lost is given by
> $$\begin{align}
> 	P(X>0) &= 1 - P(X = 0) \\
> 	&= 1 - \left(\begin{pmatrix} n \\ 0 \end{pmatrix} p^0 (1-p)^{I-0}\right) \\
> 	&= 1 - (1-p)^{I} \\
> \end{align}$$