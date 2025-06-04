# Python Cipher Analysis

This directory provides analysis tools for classic ciphers:

- **Caesar**: brute force decryption of all possible shifts.
- **Vigenere**: estimate key from frequency analysis given a key length.
- **Enigma**: simplified rotor/plugboard simulation.
- **insecure_rng**: demonstrates a Dual EC DRBG style random generator that
  is intentionally insecure. **Do not use in production!**
- **secure_rng**: example wrapper around Python's cryptographically secure
  `secrets` module.

Run `python analyze.py --help` for options.

## Node-based GUI Example

The file `node_gui.py` demonstrates a minimal node editor built with
PyQt5. Nodes can be moved around and connected by dragging from an
output socket to an input socket. The example provides color and
hairstyle option nodes that feed into a result node.
