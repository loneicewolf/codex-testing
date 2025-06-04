"""Secure random number generator wrapper using Python's secrets module."""

import secrets

class SecureRNG:
    """Provides cryptographically strong random bytes."""

    def next_bytes(self, nbytes: int = 32) -> bytes:
        return secrets.token_bytes(nbytes)


def demo() -> None:
    rng = SecureRNG()
    for _ in range(5):
        print(rng.next_bytes(16).hex())


if __name__ == "__main__":
    demo()
