---
tags:
  - comp
---
[[#Compression]] (Source Coding)
[[#Error Control Methods|Error Control]] (Channel Coding)
Encryption (Cryptographic Coding)

# Shannon-Weaver Communication Model
![1000|center](shannnon-communiocation-model.excalidraw.md)

# Simple (Uncoded Representations)
```sheet
| Text    |-| Unicode (ASCII) - 1 byte |
| Numbers |-| 1/2/4 bytes |
| Sound   |-| Sound pressure / wave. 16 bits per sample, 44kHz |
| Images  |-| RGB - byte per channel - 3 bytes |
```

# Compression
## Why Compress?
If transmitting, then the smaller the file, the [[Network#Speed|throughput]] increases. Takes up less space in storage.
# Lossless v. Lossy
Lossless compression represents the original data exactly (e.g. PNG, ZIP), whereas lossy compression approximately represents the original data (e.g. JPG), sacrificing quality for size. 
## Compression Algorithms
### LZSS
Attempts to replace symbols in a string with a reference to a dictionary of the same string. 
### Run Length Encoding
Works by finding series of identical information and grouping it together. For example, in an image, it would find all the pixels in a row, and group them together, saying that there is $x$ colour for $n$ pixels.
### Huffman Codes
![Tom Scott Video](https://youtu.be/JsTptu56GM8?si=746XGbB3Pj0czNmR)

> [!example]
> `"A_DEAD_DAD"`
>
> | Letter | Frequency |
> |-|-|
> | A | 3 |
> | D | 4 |
> | E | 1 |
> | _ | 2 |
> This is 10 characters in total, so uncompressed, this would be 80 bits, as each uncompressed character is a byte.
> Combine our lowest frequencies (note this is created bottom to top):
> ![200|center](huffman-coding-example.excalidraw.md)
> This tree results in no codes being the prefix of others.
>
> | Code | Letter | Total Bits |
> | ---- | ------ | ---------- |
> | 1    | D      | 4 x 1 |
> | 01   | A      | 3 x 2 |
> | 000  | E      | 1 x 3 |
> | 001  | _      | 3 x 2 |
> Now instead of 80 bits, the messages is 19 bits.

# Audio
Audio is split into different predictable frequency groups. This is [[#Lossless v. Lossy|lossy]], as the frequency groups are often rounded off to be more predictable. $>40\,\text{kHz}$ is approximately above what humans can hear.
# JPEG
JPEG files employ [[#Lossless v. Lossy|lossy]] file [[#Compression|compression]]. It focuses on 8x8 blocks of pixels. JPEG approximates each block using 64 basis functions, which are based on cosine waves. In particular, these waves are based on a Discrete Cosine Transform, which means they are digital and not continuous, so there is a limited number of values for each block.
When approximating each block, each of the basis functions is given a coefficient (weighting) which determines how dark each one will be.
JPEG uses a process called quantisation, which works by trying to approximate each 8x8 block with as few of the basis functions as possible, zeroing out those not used and those not significant.
An advantage of this is that those basis functions with low frequency changes and high frequency changes can be separated. Those not used often are down the bottom-right of the quantisation table, so by representing each of the coefficients in a zig-zag, it is possible to get a long run of zeros for many images.
![[Pasted image 20240507120339.png]]
Therefore, [[#Huffman Codes|Huffman encoding]] and [[#Run Length Encoding|run length encoding]] can be used to further compress the file.

# Error Control Methods
## Parity
2D parity lets you correct 1 bit (detect more than 1 bit).
## Reed-Solomon Code
Used for QR codes, disks, etc.
## Checksums, Hash Totals
See \[[[Spreadsheets]]\]
