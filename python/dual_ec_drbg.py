P = (3, 65)
Q = (83, 97)
p = 233
A = 1

# Elliptic curve utilities over F_p

def inv_mod(a, p):
    """Return modular inverse of a mod p."""
    return pow(a, -1, p)

def add(Pt, Qt):
    if Pt is None:
        return Qt
    if Qt is None:
        return Pt
    x1, y1 = Pt
    x2, y2 = Qt
    if x1 == x2 and (y1 + y2) % p == 0:
        return None
    if Pt != Qt:
        m = ((y2 - y1) * inv_mod((x2 - x1) % p, p)) % p
    else:
        m = ((3 * x1 * x1 + A) * inv_mod((2 * y1) % p, p)) % p
    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return x3, y3

def mul(k, Pt):
    result = None
    addend = Pt
    while k:
        if k & 1:
            result = add(result, addend)
        addend = add(addend, addend)
        k >>= 1
    return result

def dual_ec_drbg(seed, blocks=5):
    s = seed
    out = []
    for _ in range(blocks):
        s = mul(s, P)[0]
        r = mul(s, Q)[0]
        out.append(r)
    return out

if __name__ == "__main__":
    from sys import argv
    seed = int(argv[1]) if len(argv) > 1 else 7
    blocks = int(argv[2]) if len(argv) > 2 else 5
    print(dual_ec_drbg(seed, blocks))
