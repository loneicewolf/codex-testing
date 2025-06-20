"""Tkinter visualization of Goldbach's conjecture."""

from __future__ import annotations

import tkinter as tk
from typing import List, Tuple


def primes_up_to(n: int) -> List[int]:
    """Return a list of all primes <= n."""
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i : n + 1 : i] = [False] * len(range(i * i, n + 1, i))
    return [i for i, prime in enumerate(sieve) if prime]


def goldbach_pairs(n: int) -> List[Tuple[int, int]]:
    """Return prime pairs (p, q) with p <= q and p + q == n."""
    primes = primes_up_to(n)
    pset = set(primes)
    pairs = []
    for p in primes:
        if p > n // 2:
            break
        if n - p in pset:
            pairs.append((p, n - p))
    return pairs

class GoldbachApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Goldbach Conjecture")
        self.number = tk.IntVar(value=20)

        top = tk.Frame(self)
        top.pack(pady=5)
        tk.Label(top, text="Even number ≥ 4:").pack(side=tk.LEFT)
        tk.Entry(top, textvariable=self.number, width=6).pack(side=tk.LEFT, padx=2)
        tk.Button(top, text="Show", command=self.update_view).pack(side=tk.LEFT, padx=2)

        self.canvas = tk.Canvas(self, width=600, height=300, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.update_view()

    def update_view(self) -> None:
        n = self.number.get()
        if n < 4 or n % 2:
            return
        pairs = goldbach_pairs(n)
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        margin = 20
        scale = (width - 2 * margin) / n
        for idx, (p, q) in enumerate(pairs):
            y = margin + idx * 20
            x1 = margin + p * scale
            x2 = margin + q * scale
            self.canvas.create_line(x1, y, x2, y, fill="blue", width=2)
            self.canvas.create_text(x1, y - 5, text=str(p), anchor="s")
            self.canvas.create_text(x2, y - 5, text=str(q), anchor="s")
        info = f"{n} has {len(pairs)} prime pair(s)."
        self.canvas.create_text(width / 2, self.canvas.winfo_height() - margin,
                                text=info)


def main() -> None:
    GoldbachApp().mainloop()


if __name__ == "__main__":
    main()
