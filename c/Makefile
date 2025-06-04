CC=gcc
CFLAGS=-Wall -O2

all: cipher_tool

cipher_tool: main.o ciphers.o
	$(CC) $(CFLAGS) -o cipher_tool main.o ciphers.o

main.o: main.c ciphers.h
	$(CC) $(CFLAGS) -c main.c

ciphers.o: ciphers.c ciphers.h
	$(CC) $(CFLAGS) -c ciphers.c

clean:
	rm -f *.o cipher_tool
