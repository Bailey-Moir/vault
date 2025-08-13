---
tags:
  - atom
  - comp
---
> [!example] Vector
> ```c
> // vector.h
> #ifndef VECTOR_H
> #define VECTOR_H
> 
> #include <stdint.h>
> 
> typedef struct {
>     int32_t x;
>     int32_t y;
> } Vector;
> 
> float vector_length(Vector vec);
> 
> #endif // VECTOR_H
> ```
> 
> ```c
> // vector.c
> #include <stdint.h>
> #include <math.h>
> #include "vector.h"
> 
> float vector_length(Vector vec)
> {
>     return sqrt(vec.x*vec.x + vec.y*vec.y);
> }
> ```
> To compile,  run `gcc -Werror -Wall main.c vector.c -lm`.