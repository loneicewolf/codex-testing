import sys

def caesar(text, shift):
    res = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            res.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            res.append(ch)
    return ''.join(res)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: python caesar.py shift text')
        sys.exit(1)
    shift = int(sys.argv[1])
    text = ' '.join(sys.argv[2:])
    print(caesar(text, shift))
