#ifndef CIPHERS_H
#define CIPHERS_H

void caesar_break(const char *ciphertext);
void vigenere_break(const char *ciphertext, int key_length);

#endif // CIPHERS_H
