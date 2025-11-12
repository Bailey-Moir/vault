---
tags:
  - atom
  - comp
---
![300|center](sockets.excalidraw)
A *socket* is bound to a [[Ports|port]]. The main types of *socket* are [[#Stream Sockets|stream sockets]], [[#Datagram Sockets|datagram sockets]], and [[#Raw Sockets|raw sockets]].
- `socket()`: create a socket, allocating resources (e.g. buffer) and assigning a random unused port.
- `bind()`: bind socket to a particular port.
- `listen()`: Declare willingness to accept incoming connections, and allocate resources (queue).
- `accept()`: Accept an incoming connection from the queue, and create a new *socket* for it, bound to the same [[Ports|port]] `listen()` was called on.
- `connect()`: establish connection with [[Client-Server Paradigm|server]] (similar to [[Circuit-Switching|circuit-switching]]), or for [[#Datagram Sockets|datagram sockets]], specifies a default receiver.
- `recv()`/`send()`: reading/writing to/from the socket buffers.
- `close()`: close connection.

 \[[[TCP]], [[UDP]]\]
## Stream Sockets
![500|center](tcp-sockets.excalidraw)
Built on [[TCP|TCP]] (sender notified of errors).

## Datagram Sockets
![500|center](udp-sockets.excalidraw)
Built on [[UDP|UDP]] (sender not notified of errors).
## Raw Sockets
Built on [[IPv4|IPv4]].
