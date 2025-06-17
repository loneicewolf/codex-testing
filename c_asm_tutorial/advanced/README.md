# Advanced Level

Here we show basic file I/O in both C and assembly.

## C File Reader
```
cc filecat.c -o filecat_c
./filecat_c example.txt
```

## Assembly File Reader
```
nasm -felf64 filecat.asm
ld filecat.o -o filecat_asm
./filecat_asm example.txt
```
