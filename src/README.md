# Sample Programs

This directory contains examples in C, Python, and x86-64 Assembly.

## Building and Running

### C

Compile the C program with:

```bash
gcc hello.c -o hello_c
./hello_c
```

### Python

Run the Python script:

```bash
python hello.py
```

### Assembly

The assembly example uses [NASM](https://www.nasm.us) for assembly and `ld` for linking:

```bash
nasm -f elf64 hello.asm -o hello.o
ld hello.o -o hello_asm
./hello_asm
```
