"""Tkinter GUI for the simplified Antikythera mechanism."""

from __future__ import annotations

import tkinter as tk
from datetime import date

from antikythera import Antikythera


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Antikythera - Tkinter")
        self.mech = Antikythera()
        self.date_var = tk.StringVar(value=date.today().isoformat())

        tk.Label(self, text="Date (YYYY-MM-DD):").pack(pady=2)
        tk.Entry(self, textvariable=self.date_var).pack(pady=2)
        tk.Button(self, text="Update", command=self.update_info).pack(pady=2)

        self.text = tk.Text(self, width=40, height=6, state="disabled")
        self.text.pack(padx=5, pady=5)

        self.update_info()

    def update_info(self) -> None:
        try:
            d = date.fromisoformat(self.date_var.get())
        except ValueError:
            return
        self.mech.update_for(d)
        info = self.mech.info()
        self.text.configure(state="normal")
        self.text.delete("1.0", "end")
        self.text.insert("1.0", info)
        self.text.configure(state="disabled")


if __name__ == "__main__":
    App().mainloop()
