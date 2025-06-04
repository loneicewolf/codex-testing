#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "usage: %s shift text\n", argv[0]);
        return 1;
    }
    int shift = atoi(argv[1]);
    for (int i = 2; i < argc; i++) {
        char *p = argv[i];
        if (i > 2) putchar(' ');
        for (; *p; p++) {
            if (isalpha((unsigned char)*p)) {
                char base = isupper((unsigned char)*p) ? 'A' : 'a';
                putchar(((*p - base + shift) % 26) + base);
            } else {
                putchar(*p);
            }
        }
    }
    putchar('\n');
    return 0;
}
