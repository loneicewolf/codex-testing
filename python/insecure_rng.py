"""Dual EC DRBG style insecure random number generator.

WARNING: This implementation is intentionally insecure and provided
only for demonstration purposes. Do NOT use for real cryptographic
applications or in production systems.
"""

import os

# These constants are taken from the NIST P-256 curve but the output
# generation is intentionally flawed and predictable.
P = 0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF
Q = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
G = 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162cb13b12a14cdbdb1cb4c20ad0c6f1e2

class DualECDRBG:
    """Very simplified and insecure Dual_EC_DRBG-like generator."""

    def __init__(self, seed: int | None = None) -> None:
        if seed is None:
            seed = int.from_bytes(os.urandom(32), "big")
        self.state = seed % P

    def next_bytes(self, nbytes: int = 32) -> bytes:
        # The real algorithm uses elliptic curve point multiplication.
        # Here we use a trivial modular squaring step followed by a
        # predictable linear transformation, which is insecure.
        self.state = pow(self.state, 2, P)
        r = (self.state * Q) % P
        out = (r * G) % P
        return out.to_bytes(64, "big")[:nbytes]


def demo() -> None:
    rng = DualECDRBG()
    for _ in range(5):
        print(rng.next_bytes(16).hex())


if __name__ == "__main__":
    demo()
