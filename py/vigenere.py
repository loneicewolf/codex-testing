import sys

def vigenere(text, key):
    res = []
    j = 0
    klen = len(key)
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = ord(key[j % klen].lower()) - ord('a')
            res.append(chr((ord(ch) - base + shift) % 26 + base))
            j += 1
        else:
            res.append(ch)
    return ''.join(res)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: python vigenere.py key text')
        sys.exit(1)
    key = sys.argv[1]
    text = ' '.join(sys.argv[2:])
    print(vigenere(text, key))
