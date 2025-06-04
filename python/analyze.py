import argparse
from collections import Counter

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def caesar_break(ciphertext):
    ciphertext = ciphertext.upper()
    possibilities = {}
    for shift in range(26):
        decrypted = ''.join(
            ALPHABET[(ALPHABET.index(c) - shift) % 26] if c in ALPHABET else c
            for c in ciphertext
        )
        possibilities[shift] = decrypted
    return possibilities


def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    result = []
    key_index = 0
    for c in ciphertext.upper():
        if c in ALPHABET:
            shift = ALPHABET.index(key[key_index % len(key)])
            index = (ALPHABET.index(c) - shift) % 26
            result.append(ALPHABET[index])
            key_index += 1
        else:
            result.append(c)
    return ''.join(result)


def vigenere_break(ciphertext, key_length):
    ciphertext = ''.join(c for c in ciphertext.upper() if c in ALPHABET)
    columns = ['' for _ in range(key_length)]
    for i, c in enumerate(ciphertext):
        columns[i % key_length] += c
    key = ''
    for col in columns:
        freqs = Counter(col)
        most_common = freqs.most_common(1)[0][0]
        shift = (ALPHABET.index(most_common) - ALPHABET.index('E')) % 26
        key += ALPHABET[shift]
    plaintext = vigenere_decrypt(ciphertext, key)
    return key, plaintext


# Simple Enigma simulation with 3 rotors and plugboard
def enigma_encrypt(text, rotors, reflector, plugboard):
    def apply_plugboard(c):
        return plugboard.get(c, c)

    result = []
    r_positions = [0, 0, 0]
    for ch in text.upper():
        if ch not in ALPHABET:
            result.append(ch)
            continue
        c = apply_plugboard(ch)
        for i in range(3):
            offset = (ALPHABET.index(c) + r_positions[i]) % 26
            c = rotors[i][offset]
        c = reflector[ALPHABET.index(c)]
        for i in reversed(range(3)):
            offset = rotors[i].index(c)
            c = ALPHABET[(offset - r_positions[i]) % 26]
        c = apply_plugboard(c)
        result.append(c)
        r_positions[0] = (r_positions[0] + 1) % 26
        if r_positions[0] == 0:
            r_positions[1] = (r_positions[1] + 1) % 26
            if r_positions[1] == 0:
                r_positions[2] = (r_positions[2] + 1) % 26
    return ''.join(result)


def main():
    parser = argparse.ArgumentParser(description="Cipher analysis tools")
    subparsers = parser.add_subparsers(dest="command")

    caesar_p = subparsers.add_parser("caesar_break")
    caesar_p.add_argument("ciphertext")

    vig_p = subparsers.add_parser("vigenere_break")
    vig_p.add_argument("ciphertext")
    vig_p.add_argument("key_length", type=int)

    enigma_p = subparsers.add_parser("enigma_sim")
    enigma_p.add_argument("text")

    args = parser.parse_args()

    if args.command == "caesar_break":
        possibilities = caesar_break(args.ciphertext)
        for shift, text in possibilities.items():
            print(f"Shift {shift}: {text}")
    elif args.command == "vigenere_break":
        key, text = vigenere_break(args.ciphertext, args.key_length)
        print("Estimated key:", key)
        print("Plaintext:", text)
    elif args.command == "enigma_sim":
        rotors = [
            'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
            'AJDKSIRUXBLHWTMCQGZNPYFVOE',
            'BDFHJLCPRTXVZNYEIWGAKMUSQO'
        ]
        reflector = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
        plugboard = {}
        text = enigma_encrypt(args.text, rotors, reflector, plugboard)
        print(text)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
