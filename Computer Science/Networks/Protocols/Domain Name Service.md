---
tags:
  - atom
  - comp
---
![500|center](dns-packet.excalidraw)
*Domain name service* (*DNS*) is a load distributed protocol built on [[UDP|UDP]], and it maps
- [[Hosts|host]]names $\to$ [[IPv4|IP]] addresses (`type=A`),
- [[Hosts|host]]names $\to$ [[Hosts|host]]names (host aliasing) (`type=CNAME`), and
- [[Simple Mail Transfer Protocol|mail server]] aliases $\to$ [[Simple Mail Transfer Protocol|mail servers]] (mail server aliasing) (`type=MX`).

> [!note] Each [[Internet Service Provider|ISP]] has a **local _DNS_ server** (which are not strictly part of the hierarchy, but are central to the *DNS* architecture).

> [!fields]-
> - **Identification** is the ID for the query that the response will share,
> - **Flags** include a bit for whether it is a query or reply, whether recursion is desired/available, and if the given reply is authoritative,
> - **Questions** holds `(name, type)` pairs for queries,
> - **Answers** holds `(type, value, ttl)` tuples for replies, and
> - **Authority** holds records for authoritative servers.