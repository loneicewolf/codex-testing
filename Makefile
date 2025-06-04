CFLAGS=-Wall -Wextra -O2
ASMFLAGS=-f elf64

ASMOBJS=asm/caesar.o asm/vigenere.o asm/enigma.o

all: c/caesar c/vigenere c/enigma asm/caesar asm/vigenere asm/enigma

c/caesar: c/caesar.c
	$(CC) $(CFLAGS) $< -o $@

c/vigenere: c/vigenere.c
	$(CC) $(CFLAGS) $< -o $@

c/enigma: c/enigma.c
	$(CC) $(CFLAGS) $< -o $@

asm/%.o: asm/%.asm
	nasm $(ASMFLAGS) $< -o $@

asm/caesar: asm/caesar.o
	$(CC) $< -no-pie -lc -o $@

asm/vigenere: asm/vigenere.o
	$(CC) $< -no-pie -lc -o $@

asm/enigma: asm/enigma.o
	$(CC) $< -no-pie -lc -o $@

clean:
	rm -f c/caesar c/vigenere c/enigma $(ASMOBJS) asm/caesar asm/vigenere asm/enigma
