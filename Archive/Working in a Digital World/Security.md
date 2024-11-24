---
tags:
  - atom
  - comp
---
# Triangle of CIA
Prioritizing two often sacrifices another.

Confidentiality - right person can access
Integrity - accurate
Availability - when needed, it is available

# Symmetric Key Encryption
Same key used for both processes.
# Asymmetric Key Encryption
One public key to do the encryption, and one that is private key to do the decryption.
# Diffy Helman Method
In reality, usually [[#Symmetric Key Encryption]] and [[#Asymmetric Key Encryption]] are mixed together.

Alice has a secret key $a$ and Bob has a secret key $B$.
1. Alice and Bob agree on public parameters $p$ and $g$. It is fine for anyone else to know these values.
2. They combine their secret keys and the parameters and sends the resulting public key
$$\begin{array}{ll}
	\bf{Alice} & \bf{Bob} \\
	A = g^a \mod p & B = g^b \mod p \\
	S = B^a \mod p & S = B^a \mod p \\
\end{array}$$
$$ S = \left( g^b \mod p \right)^a \mod p $$

# Attack Examples
- Ransomware
- Fraud
- Botnets (DDoS)
- Password attacks, hashed passwords
	- Brute-force
	- Dictionary
- Social engineering
- Spam

# Privacy Principles
- You know about every database with information about you.
- You can see everything about you that is in a database.
- You are able to challenge data about yourself (with onus of proof on the holder of the data).
- All cross-references are public knowledge.
- Information cannot be used for purposes other than those for which it was collected.
- There are strict controls on who has access to data.
- Severe penalties for misuse.

# Quantum Computing
Quantum Theory - 1920s
Digital Computing - 1930s
Quantum Computing - 1980
## Quantum Computing vs. Classical Computing

| Classical Computing                                                                      | Quantum Computing                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| - One-Dimensional<br>- Bit: Zero or One (Low Voltage or High Voltage)<br>- Deterministic | - Multidimensional<br>- Quantum Bit - "Qubit"<br> - Superposition<br>$\hspace{1em}$- Combine two or more valid states into a new valid state.<br>$\hspace{1em}$- Any state represented as sum of two or more states.<br>- Entanglement<br>$\hspace{1em}$- Two Systems link so closely, one gives immediate knowledge of the other.<br>- Not deterministic |
## Quantum Achievements
- 1994 - Shor's Algorithm
	- Reduce prime factorization from $O(e^n)$ to $O(\log N)$ on quantum computers.
- 1996 - Grover's Algorithm
	- Reduce search space from brute force $O(N)$ to $O(\sqrt{N})$.
	