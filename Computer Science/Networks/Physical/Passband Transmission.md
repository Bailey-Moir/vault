---
tags:
  - atom
  - comp
---
*Passband transmission* allows multiple frequencies to be transmitted across a medium by allocating different transmitters specific central frequencies (as opposed to **baseband transmission** which only allocates one central frequency, meaning [[Frequency Division Multiple Access|FDMA]] can't be used).

In **digital passband modulation**, a wave of the form
$$s(t) = A(t)\cos \left[ (f_{c}+f(t))t+\phi(t) \right] $$
where $f_{c}$ is the centre frequency, $f(t)$ is the frequency offset, and $\phi(t)$ is the phase, is transmitted for the **symbol duration**.

- **Amplitude Modulation** (**ASK**) - only $A(t)$ varies.
- **Frequency Modulation** (**FSK**) - only $f(t)$ varies.
- **Phase Modulation** (**PSK**) - only $\phi(t)$ varies.
- **Quadrature Amplitude Modulation** (**QAM**) - combines **ASK** and **PSK** (constant $f(t)$).


> [!example] [[Radio Channel|Radio]]