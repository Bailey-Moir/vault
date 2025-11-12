---
tags:
  - atom
  - comp
---
*Network address translation* (*NAT*) converts between private and public [[IPv4|IP]] addresses.

> [!motivation]
> - [[Internet Service Provider|ISP]]s only needs to allocate one [[IPv4|IP]] address per end [[Networks|network]].
> - addresses of local [[Networks|network]] devices can change without notifying other [[Networks|networks]].
> - local [[Networks|network]] device addresses are independent of the [[Internet Service Provider|ISP]] ([[Internet Service Provider|ISP]] can change).
> - local [[Networks|network]] devices can not be explicitly addressed. 

> [!violations]
> - It spans both the [[TCP-IP Reference Model|internet and transport layers]].
> - It breaks end-to-end connectivity model, as a middle man does a thing, and
> - [[TCP|TCP]] and [[UDP|UDP]] are required, as [[Ports|ports]] are used to address local [[Networks|network]] devices.