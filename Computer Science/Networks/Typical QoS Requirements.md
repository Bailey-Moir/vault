---
tags:
  - atom
  - comp
---
| Application                           | Data loss     | Bandwidth                                                   | Delay-sensitive    |
| ------------------------------------- | ------------- | ----------------------------------------------------------- | ------------------ |
| File transfer                         | No loss       | Elastic                                                     | No                 |
| Email                                 | No loss       | Elastic                                                     | No                 |
| Web pages                             | No loss       | Mostly elastic, minimum rate desirable                      | No                 |
| Internet telephony, videoconferencing | Loss-tolerant | Audio/Voice: few kbps – 1 Mbps,<br/>Video: 10 kbps – 5 Mbps | $\le$ 200 - 250 ms |
| Streaming audio / video               | Loss-tolerant | Same as above                                               | A few seconds      |
| Interactive games                     | Loss-tolerant | few kbps – 1 Mbps                                           | few hundreds ms    |
| Instant messaging                     | No loss       | Elastic                                                     | Not very, depends  |
where **elastic** means no strict minimum-bandwidth, they just use what they get.

> [!definition] *QoS* refers to the for "quality of service" of a [[Networks|network]].