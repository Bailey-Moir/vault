---
tags:
  - atom
  - phys
---
A *capacitor* consists of two conductors separated by an insulator (e.g. parallel plates), able to form an [[Electric Fields|electric field]].
- *Capacitors* can hold [[Charge|charge]]
- *Capacitors* have a maximum [[Voltage|voltage]] equal to that of the supply [[Voltage|voltage]].
- The rate at which *capacitors* [[#Charging and Discharging Capacitors|charge/discharge]] decreases over time as electron-electron-repulsion increases/decreases.

$$ E = \frac{1}{2}QV $$
> [!variables]-
> - $E$ is the [[Energy|energy]] ($J$) stored in the *capacitor*.
> - $Q$ is the [[Charge|charge]] ($C$) stored in the *capacitor*.
> - $V$ is the [[Voltage|voltage]] ($V$) across the *capacitor*.

$$C = \varepsilon_{0}\varepsilon_{r} \dfrac{A}{d}$$
> [!variables]-
> - $C$ is the [[Capacitance|capacitance]] ($F$) of the *capacitor*.
> - $\varepsilon_{0}$ is permittivity of free space ($Fm^{-1}$).
>   (The universal constant measuring the ability for a vacuum [[Electric Fields|electric field]]).
> - $A$ is the area of overlap ($m^{2}$) between the two conductors.
> - $d$ is the distance ($m$) between the two conductors.
# Charging and Discharging Capacitors
![1000|center](charging-and-discharging-capacitors.excalidraw.md)
$$ \tau = RC $$
> [!variables]-
> - $\tau$ is the time constant ($s$) seen in the diagrams.
> - $C$ is the circuit [[Capacitance|capacitance]] ($F$).
> - $R$ is the circuit [[Physics/Electricity/Resistance|resistance]] ($\ohm$).

Note similarity to [[Inductors#Charging and Discharging Inductors]].

```sheet
| Phase         |-| [[Current\|Current]] | [[Voltage\|Voltage]]    | Electrons                                     |
| ------------- |-| ------- | ---------- | ------------------------------------------------- |
| Start         |-| $I \gg 0$  | $V \ll V_s$ | $\overline e$ deposit onto plate                  |
| Charging      |-| $I>0$   | $V < V_s$  | more $\overline e$ accumlate ($V$ apposes $V_s$) |
| Fully Charged |-| $I=0$   | $V=V_s$    | repulsive force matches and opposoes $V_s$        | 
```
