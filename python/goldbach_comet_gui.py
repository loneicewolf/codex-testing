"""Tkinter visualization of Goldbach's comet.

Select a range of even numbers and plot the number of prime pairs
that sum to each value ("Goldbach's comet").
"""

from __future__ import annotations

import tkinter as tk
from typing import List


# --- math utilities --------------------------------------------------------

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def goldbach_count(n: int) -> int:
    count = 0
    for p in range(2, n // 2 + 1):
        if is_prime(p) and is_prime(n - p):
            count += 1
    return count


# --- GUI ------------------------------------------------------------------

class GoldbachCometGUI(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Goldbach's Comet")

        self.start_var = tk.IntVar(value=4)
        self.end_var = tk.IntVar(value=50)

        tk.Label(self, text="Start (even):").pack()
        tk.Entry(self, textvariable=self.start_var, width=10).pack()
        tk.Label(self, text="End (even):").pack()
        tk.Entry(self, textvariable=self.end_var, width=10).pack()
        tk.Button(self, text="Plot", command=self.plot).pack(pady=4)

        self.canvas = tk.Canvas(self, width=600, height=400, bg="white")
        self.canvas.pack(padx=5, pady=5)

    def plot(self) -> None:
        start = self.start_var.get()
        end = self.end_var.get()
        if start % 2:
            start += 1
        if end % 2:
            end -= 1
        if start < 4:
            start = 4
        if end <= start:
            return

        numbers: List[int] = list(range(start, end + 1, 2))
        counts = [goldbach_count(n) for n in numbers]
        max_count = max(counts)

        w = int(self.canvas["width"])
        h = int(self.canvas["height"])
        margin = 40
        plot_w = w - 2 * margin
        plot_h = h - 2 * margin

        self.canvas.delete("all")
        self.canvas.create_line(margin, h - margin, w - margin, h - margin)
        self.canvas.create_line(margin, margin, margin, h - margin)

        step = plot_w / (len(numbers) - 1 if len(numbers) > 1 else 1)
        for i, c in enumerate(counts):
            x = margin + i * step
            y = h - margin - (c / max_count) * plot_h
            self.canvas.create_line(x, h - margin, x, y, fill="blue")

        self.canvas.create_text(w // 2, margin // 2,
                               text=f"Goldbach counts from {start} to {end}")


if __name__ == "__main__":
    GoldbachCometGUI().mainloop()
