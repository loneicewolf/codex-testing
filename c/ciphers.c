#include <stdio.h>
#include <string.h>
#include "ciphers.h"

void caesar_break(const char *ciphertext) {
    for (int shift = 0; shift < 26; ++shift) {
        for (const char *p = ciphertext; *p; ++p) {
            if (*p >= 'A' && *p <= 'Z')
                putchar('A' + (*p - 'A' - shift + 26) % 26);
            else if (*p >= 'a' && *p <= 'z')
                putchar('a' + (*p - 'a' - shift + 26) % 26);
            else
                putchar(*p);
        }
        printf("\n");
    }
}

void vigenere_break(const char *ciphertext, int key_length) {
    size_t len = strlen(ciphertext);
    char key[key_length + 1];
    for (int i = 0; i < key_length; ++i) {
        int counts[26] = {0};
        for (size_t j = i; j < len; j += key_length) {
            char c = ciphertext[j];
            if (c >= 'A' && c <= 'Z')
                counts[c - 'A']++;
        }
        int max = 0, idx = 0;
        for (int k = 0; k < 26; ++k) {
            if (counts[k] > max) {
                max = counts[k];
                idx = k;
            }
        }
        key[i] = 'A' + (idx - ('E' - 'A') + 26) % 26;
    }
    key[key_length] = '\0';
    printf("Estimated key: %s\n", key);
}
