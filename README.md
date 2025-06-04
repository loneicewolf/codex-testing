# Cipher Simulators

This repository contains simple implementations of Caesar, Vigenere and toy Enigma ciphers in three languages:

- **Python**: located in `py/`
- **C**: located in `c/`
- **NASM assembly**: located in `asm/`

## Building and Running

### Python
Run the scripts directly with Python 3:
```bash
python3 py/caesar.py 3 "HELLO"
python3 py/vigenere.py KEY "HELLO WORLD"
python3 py/enigma.py HELLO
```

### C
Compile each program with a C compiler such as GCC:
```bash
gcc c/caesar.c -o c/caesar
gcc c/vigenere.c -o c/vigenere
gcc c/enigma.c -o c/enigma
```
Then run them:
```bash
./c/caesar 3 HELLO
./c/vigenere KEY "HELLO WORLD"
./c/enigma HELLO
```

### Assembly
Assemble with NASM and link with GCC:
```bash
nasm -f elf64 asm/caesar.asm -o asm/caesar.o
gcc asm/caesar.o -no-pie -lc -o asm/caesar

nasm -f elf64 asm/vigenere.asm -o asm/vigenere.o
gcc asm/vigenere.o -no-pie -lc -o asm/vigenere

nasm -f elf64 asm/enigma.asm -o asm/enigma.o
gcc asm/enigma.o -no-pie -lc -o asm/enigma
```
Run the executables:
```bash
./asm/caesar
./asm/vigenere
./asm/enigma
```

