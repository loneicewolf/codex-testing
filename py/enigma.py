"""Toy Enigma cipher demonstration with a single rotor."""

import sys

rotor = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'

def enigma(text):
    pos = 0
    res = []
    for ch in text:
        if ch.isalpha():
            base = ord('A')
            idx = ord(ch.upper()) - base
            step1 = (idx + pos) % 26
            step2 = ord(rotor[step1]) - base
            step3 = ord(reflector[step2]) - base
            step4 = rotor.index(chr(step3 + base))
            out = (step4 - pos) % 26
            char = chr(out + base)
            if ch.islower():
                char = char.lower()
            res.append(char)
            pos = (pos + 1) % 26
        else:
            res.append(ch)
    return ''.join(res)

if __name__ == '__main__':
    text = ' '.join(sys.argv[1:])
    print(enigma(text))
