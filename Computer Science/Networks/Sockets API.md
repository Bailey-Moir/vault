---
tags:
  - atom
  - comp
---
```python
from socket import socket

s = socket(family=AF_INET, type=SOCK_STREAM)
s.connect(address)
```

where
- `family` defines the protocol (`AF_INET` for [[IPv4|IPv4]], `AF_INET6` for [[IPv6|IPv6]]),
- `type` defines the [[Sockets|socket type]] (e.g. `SOCK_STREAM` for [[Sockets#Stream Sockets|stream sockets]], `SOCK_DGRAM` for [[Sockets#Datagram Sockets|datagram sockets]], and `SOCK_RAW` for [[Sockets#Raw Sockets|raw sockets]]), and
- `address` takes a [[Basic Python#Tuples|tuple]] `(ip, port)`.

> [!example]- Sending
> ```python
> amount = s.send(bytes)
> amount = s.sendto(bytes, address)
> ``` 
> where `amount` gives the amount of bytes sent.

> [!example]- Receiving
> ```python
> data = s.recv(bufsize)
> data, address = s.recvfrom(bufsize)
> ```

> [!example]- Accepting
> `conn, client_addr = s.accept()`
> where `conn` is a new [[Sockets|socket]].

- `listen()` takes an optional parameter `backlog`, which specifies the length of the [[Queues|queue]].
- `accept()` is the non-blocking equivalent of `accept()` from multiple [[Sockets|sockets]].
- `getaddrinfo(host, port)` gives a [[Basic Python#Tuples|5-tuple]] of information about what services a [[Hosts|host]] supports, and to get the [[IPv4]] from the [[Domain Name Service|domain name]].

\[[[Sockets]]\]

[^1]: [[Sockets]]
