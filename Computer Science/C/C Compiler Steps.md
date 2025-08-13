---
tags:
  - atom
  - comp
---
![[c-compiling-steps.png | center]]

With `gcc`,
- `-Wall` outputs all its warning messages.
- `-Werror` means warnings are treated as errors, halting on warnings.
- `-c` just does the compilation step, not a full compile-and-build (not linking). This adds an intermediate "relocatable object code" `.o` file that needs `gcc` (without `-c`) to be run on it again to give the executable.
- `-o {name}` names the executable `{name}` instead of `a.out`.

 