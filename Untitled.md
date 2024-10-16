$$y'+y=0$$
$$ \sum_{n=1}^{\infty}nC_{n}t^{n-1} + \sum_{n=0}^{\infty} C_{n}t^n$$
$$ \sum_{n=0}^{\infty}(n+1)C_{n+1}t^{n} + C_{n}t^n$$
$$ \sum_{n=0}^{\infty}\left((n+1)C_{n+1} + C_{n}\right)t^n$$
$$ (n+1)C_{n+1} + C_{n} = 0 \hspace{2em}\forall n\in\N $$
$$ C_{n+1} = -\dfrac{1}{1+n}C_{n}\hspace{2em}\forall n\in\N $$
let $C_{0} = C$
$$y = \sum_{n=0}^{\infty} (-1)^n\dfrac{C}{n!}t^n $$
$$y = C\sum_{n=0}^{\infty} (-1)^n\dfrac{1}{n!}t^n = Ce^{-t} $$