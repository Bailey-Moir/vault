---
tags:
  - atom
  - comp
---
In *peer-to-peer* (*P2P*) [[Networks|networks]], there is
- (almost) no dedicated [[Client-Server Paradigm|server]] to provide services,
- no strict separation of roles, each [[Hosts|host]] send and receives, and
- no requirement for [[Hosts|hosts]] to always be on.

> [!rough-idea]-
> Suppose there are already $n$ [[Hosts|hosts]] with a certain piece of data
> The $n-1$-th [[Hosts|host]] requests different chunks of the data from some or all of the $n$ [[Hosts|hosts]].
> In return, the $n+1$-th host agrees to provide data to the $n+2$-th.

> [!example] Blockchain (eww), BitTorrent