#include <stdio.h>
#include <string.h>
#include "ciphers.h"

int main(int argc, char **argv) {
    if (argc < 3) {
        printf("Usage: %s <cipher> <text> [key_length]\n", argv[0]);
        return 1;
    }
    const char *mode = argv[1];
    const char *text = argv[2];
    if (strcmp(mode, "caesar") == 0) {
        caesar_break(text);
    } else if (strcmp(mode, "vigenere") == 0 && argc >= 4) {
        int key_length = atoi(argv[3]);
        vigenere_break(text, key_length);
    } else {
        printf("Unsupported mode or missing arguments\n");
    }
    return 0;
}
