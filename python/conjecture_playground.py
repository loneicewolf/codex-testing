"""Tkinter-based Mathematical Conjecture Playground.

Select a predefined conjecture or enter a custom Python expression in terms of
`n` (or `x`) and visualize the resulting sequence.
"""

from __future__ import annotations

import math
import tkinter as tk
from tkinter import ttk

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    r = int(math.isqrt(n)) + 1
    for i in range(3, r, 2):
        if n % i == 0:
            return False
    return True


def goldbach_count(n: int) -> int:
    count = 0
    for p in range(2, n // 2 + 1):
        if is_prime(p) and is_prime(n - p):
            count += 1
    return count


def collatz_steps(n: int) -> int:
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps


class ConjecturePlayground(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Conjecture Playground")
        self.geometry("700x500")

        self.example_var = tk.StringVar(value="Goldbach")
        self.expr_var = tk.StringVar(value="n**2")
        self.max_n_var = tk.IntVar(value=20)

        top = tk.Frame(self)
        top.pack(fill=tk.X, pady=5)

        tk.Label(top, text="Example:").pack(side=tk.LEFT, padx=5)
        examples = ["Goldbach", "Collatz", "Custom expression"]
        self.example_menu = ttk.OptionMenu(top, self.example_var, examples[0], *examples, command=lambda _: self.toggle_entry())
        self.example_menu.pack(side=tk.LEFT, padx=5)

        tk.Label(top, text="Expression:").pack(side=tk.LEFT, padx=5)
        self.expr_entry = tk.Entry(top, textvariable=self.expr_var, width=20)
        self.expr_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(top, text="Max n:").pack(side=tk.LEFT, padx=5)
        tk.Entry(top, textvariable=self.max_n_var, width=6).pack(side=tk.LEFT, padx=5)

        tk.Button(top, text="Plot", command=self.update_plot).pack(side=tk.LEFT, padx=5)

        self.text_box = tk.Text(self, height=8, width=40, state="disabled")
        self.text_box.pack(pady=5)

        fig = Figure(figsize=(6, 3), dpi=100)
        self.ax = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.toggle_entry()
        self.update_plot()

    def toggle_entry(self) -> None:
        if self.example_var.get() == "Custom expression":
            self.expr_entry.configure(state="normal")
        else:
            self.expr_entry.configure(state="disabled")

    def update_plot(self) -> None:
        example = self.example_var.get()
        max_n = self.max_n_var.get()
        if max_n < 1:
            max_n = 1
        if example == "Goldbach":
            xs = list(range(4, max_n + 1, 2))
            ys = [goldbach_count(n) for n in xs]
            title = "Goldbach pair counts"
            text_lines = [f"{n}: {c}" for n, c in zip(xs, ys)]
        elif example == "Collatz":
            xs = list(range(2, max_n + 1))
            ys = [collatz_steps(n) for n in xs]
            title = "Collatz steps"
            text_lines = [f"{n}: {s}" for n, s in zip(xs, ys)]
        else:
            expr = self.expr_var.get()
            xs = list(range(1, max_n + 1))
            ys = []
            for n in xs:
                try:
                    y = eval(expr, {"n": n, "x": n, "math": math})
                except Exception:
                    y = float("nan")
                ys.append(y)
            title = expr
            text_lines = []

        self.text_box.configure(state="normal")
        self.text_box.delete("1.0", "end")
        self.text_box.insert("end", "\n".join(text_lines))
        self.text_box.configure(state="disabled")

        self.ax.clear()
        self.ax.bar(xs, ys, width=0.8, color="skyblue")
        self.ax.set_title(title)
        self.ax.set_xlabel("n")
        self.ax.set_ylabel("Value")
        self.canvas.draw()


if __name__ == "__main__":
    ConjecturePlayground().mainloop()
