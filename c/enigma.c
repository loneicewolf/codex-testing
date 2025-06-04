#include <stdio.h>
#include <ctype.h>
#include <string.h>

/*
 * Toy Enigma cipher demonstration with a single rotor and reflector.
 * Usage: ./enigma text
 * Not intended for real cryptographic use.
 */

static const char *rotor = "EKMFLGDQVZNTOWYHXUSPAIBRCJ";
static const char *reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT";

int main(int argc, char *argv[]) {
    if (argc < 2) {
        fprintf(stderr, "usage: %s text\n", argv[0]);
        return 1;
    }
    int pos = 0;
    for (int i = 1; i < argc; i++) {
        char *p = argv[i];
        if (i > 1) putchar(' ');
        for (; *p; p++) {
            if (isalpha((unsigned char)*p)) {
                int base = 'A';
                int idx = toupper((unsigned char)*p) - base;
                int step1 = (idx + pos) % 26;
                int step2 = rotor[step1] - base;
                int step3 = reflector[step2] - base;
                int step4 = strchr(rotor, step3 + base) - rotor;
                int enc = (step4 - pos + 26) % 26;
                char out = enc + base;
                if (islower((unsigned char)*p)) out = tolower(out);
                putchar(out);
                pos = (pos + 1) % 26;
            } else {
                putchar(*p);
            }
        }
    }
    putchar('\n');
    return 0;
}
