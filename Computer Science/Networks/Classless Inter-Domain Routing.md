---
tags:
  - atom
  - comp
---
*Classless inter-domain routing* (*CIDR*) allows you to vary how many of 32 bits are allocated to the [[Networks|network]] address and the [[Hosts|host]] address respectively using a **netmask**.

> [!note]- Special [[Hosts|host]] addresses
> In the [[Networks|network]] $a.b.c.d/k$, there are two special [[Hosts|host]] addresses:
> - All $0$s gives to the [[Networks|network]] address as a whole.
> - All $1$s gives the [[Broadcasting|broadcast]] address for the [[Networks|network]].

> [!note]- Special [[Networks|network]] addresses
> | Address Block    | Usage                                            |
> | ---------------- | ------------------------------------------------ |
> | $127.0.0.0/8$    | [[Hosts\|Host]] loopback [[Networks\|network]]   |
> | $169.254.0.0/16$ | Link local address                               |
> | $10.0.0.0/7$     | Private-use [[IPv4\|IP]] [[Networks\|network]]     |
> | $172.16.0.0/12$  | Private-use [[IPv4\|IP]] [[Networks\|network]]     |
> | $192.168.0.0/16$ | Private-use [[IPv4\|IP]] [[Networks\|network]]<br> |
> where private use [[IPv4|IPv4]] addresses are often used for broadband clients or NAT boxes.
