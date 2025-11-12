---
tags:
  - atom
  - comp
---
*SMTP* (*Simple mail transfer protocol*) communicates in 7-bit ASCII text, using a mail server. To access emails, you can either use [[#POP3|POP3]] or [[#IMAP|IMAP]].

> [!-]- **[[Hypertext Transfer Protocol|HTTP]] vs. *SMTP***
> | [[Hypertext Transfer Protocol \| HTTP]] | *SMTP*                         |
> | --------------------------------------- | ------------------------------ |
> | Pull protocol                           | Push protocol                  |
> | Synchronous communication               | Asynchronous communication     |
> | Direct request-response model           | Store-and-forward architecture |
> |                                         | Based on 7-bits ASCII          |
# POP3
In *POP3* (Post Office Protocol v3), there are four states:
1. **Connection Establishment**
   A [[TCP|TCP]] connection to the mail server is established on port `110`.
2. **Authentication State**
   User agent sends username & password ([[Plaintext|plaintext]]) to authenticate the user.
3. **Transaction State**
   User agent retrieves retrieves messages, can mark (or remove marks) for deletion, and can obtain mail statistics.
4. **Update State**
   Mail server deletes marked messages and closes [[TCP|TCP]] connection.

> [!-]- **Notable Issues**
> - *POP3* does not synchronise emails across multiple devices.
> - *POP3* does not support [[Client-Server Paradigm|server-side]] folder management.
# IMAP
With IMAP (Internet Mail Access Protocol),
- messages are kept on the [[Client-Server Paradigm|server]] and copies are replicated on the [[Client-Server Paradigm|client]],
- users can organise messages in folders,
- user state information is maintained across sessions, and specifically
- *IMAP4* allows a user agent to obtain components of messages.