# Python Cipher Analysis

This directory provides analysis tools for classic ciphers:

- **Caesar**: brute force decryption of all possible shifts.
- **Vigenere**: estimate key from frequency analysis given a key length.
- **Enigma**: simplified rotor/plugboard simulation.
- **insecure_rng**: demonstrates a Dual EC DRBG style random generator that
  is intentionally insecure. **Do not use in production!**
- **secure_rng**: example wrapper around Python's cryptographically secure
  `secrets` module.
- **antikythera**: simplified astronomical simulation with both Tkinter
  and PySimpleGUI interfaces.

Run `python analyze.py --help` for options.

## AI Examples for Beginners

- **simple_chatbot.py**: rule-based conversation bot illustrating conditional logic.
- **digit_classifier.py**: uses scikit-learn to classify handwritten digits with logistic regression.
- **tic_tac_toe_ai.py**: play Tic-Tac-Toe against an AI employing the minimax algorithm.
- **black_hole_gui.py**: simple Tkinter gravity simulator with sliders and
  color selection for visualizing motion near a black hole.
