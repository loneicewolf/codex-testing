#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

/*
 * Simple Vigenere cipher demonstration.
 * Usage: ./vigenere KEY text
 * Not intended for real cryptographic use.
 */

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "usage: %s key text\n", argv[0]);
        return 1;
    }
    char *key = argv[1];
    int key_len = strlen(key);
    int j = 0;
    for (int i = 2; i < argc; i++) {
        char *p = argv[i];
        if (i > 2) putchar(' ');
        for (; *p; p++) {
            if (isalpha((unsigned char)*p)) {
                char base = isupper((unsigned char)*p) ? 'A' : 'a';
                int shift = tolower(key[j % key_len]) - 'a';
                putchar(((*p - base + shift) % 26) + base);
                j++;
            } else {
                putchar(*p);
            }
        }
    }
    putchar('\n');
    return 0;
}
