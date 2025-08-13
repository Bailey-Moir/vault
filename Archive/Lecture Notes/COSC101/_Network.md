---
tags:
  - comp
---
URL - Uniform Resource Locator
Servers - Web: host data

A lot of people think that most WiFi comes from satellites. In reality, most comes through cables running under the ocean.
# Definitions
```sheet
| Packet      |-| A piece of data that is passed through a network ($\approx 1000$ bytes)      |
| Node        |-| Anything that is connected to a network                                      |
| Connection  |-| How the nodes are connected                                                  |
| Services    |-| Anything that runs on a network                                              |
```

## Speed
```sheet
| Bandwidth   |-| Speed (bits per second)                                                      |
| Latency     |-| Delay for the first packet (round trip time).                                |
| Throughput  |-| How much we can get through out network (latency + bandwidth + lost packets) |
| Bottlenecks |-| Slow downs along the way                                                     |
```

# Services
Anything that runs on a network:
- http(s)
- mailto
- ftp
- voip (voice over internet protocol)
- remote login

# Physical Media
```sheet
| Ethernet |-| Copper $\sim 800m$ |
| Fibre |-| Glass/plasitc (optic/light). Has a very high bandwidth as has many different possible frequencies that can be used at once. |
| Wireless |-| Wi-Fi, Mobile (broadband cellular network), Satelite, Wireless Personal area Network (PAN, Bluetooth) |
```

# Types of Networks
- PAN (Personal Area Network)
	- Bluetooth
- LAN (Local Area Network)
	- Ethernet
- WLAN (Wireless LAN)
- WAN (Wide Area Network)
	- Different towns/cities/countries (this would be fibre optic)

# Protocols
- TCP/IP (Transport Control Protocol, Internet Protocol)
	- IPv4 4 bytes
	- IPv6 16 bytes
- HTTP
- DNS (Domain Name Server, URL $\to$ IP)