# Beginner Level

These introductory examples demonstrate how to compile and run a basic program in C and assembly.

## Compiling the C example

```
cc hello.c -o hello_c
./hello_c
```

## Assembling the assembly example

```
nasm -felf64 hello.asm
ld hello.o -o hello_asm
./hello_asm
```
