---
tags:
  - atom
  - comp
---
![700|center](http-packets.excalidraw.md)
*HTTP* (*Hypertext Transfer Protocol*) is
- built on [[TCP|TCP]] (excluding *HTTP-3*),
- structured in [[Plaintext|plaintext]], and
- stateless (no need to retain information from past requests).

> [!note]- **Non-persistent HTTP**
> In *HTTP-1.0*, at most one object can be sent per [[TCP|TCP]] connection.
> (this is stupid, and dumb. luckily 1.0 is obsolete).

> [!note] *HTTP* requests' `Accept-langauge` field can have multiple languages with multiple 'quality' values, specifying how preferred each language is. The default is $1$.

> [!note]- **Methods**
> | Method  | Description                |
> | ------- | -------------------------- |
> | GET     | Read a Web page.           |
> | HEAD    | Read a Web page's header.  |
> | POST    | Append to a Web page.      |
> | PUT     | Store a Web page.          |
> | DELETE  | Remove a Web page.         |
> | TRACE   | Echo the incoming request. |
> | CONNECT | Connect through a proxy.   |
> | OPTIONS | query options for a page.  |

> [!note]- **Cookies**
> Each [[Client-Server Paradigm|client]] stores a mapping from [[Client-Server Paradigm|servers]] to cookie IDs. These are allocated by the [[Client-Server Paradigm|server]], and sent by the [[Client-Server Paradigm|client]] in each request. The [[Client-Server Paradigm|server]] stores information for each of these cookies in some back-end database.