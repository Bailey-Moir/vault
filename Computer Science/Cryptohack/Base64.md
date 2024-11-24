---
tags:
  - atom
  - comp
---
Allows us to represent binary data as an [[ASCII|ASCII string]] using an alphabet of 64 characters. One character of a Base64 string encodes 6 bits.
`import base64`
`base64.b64encode()` encodes a given readable buffer into base 64.
`base64.b64encode()` decodes base 64 into bytes.