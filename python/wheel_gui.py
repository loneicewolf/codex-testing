"""Simple wheel GUI with commands.

This demonstration uses Tkinter to create a wheel-like GUI that performs
basic text manipulation commands when started. It's inspired by
"EPIGRAPH"-style interface with spinning gears.
"""

import math
import tkinter as tk
from tkinter import ttk


class GearCanvas(tk.Canvas):
    """Canvas widget that draws a simple gear and rotates it."""

    def __init__(self, master=None, radius=60, teeth=8, **kwargs):
        super().__init__(master, width=2 * radius + 20, height=2 * radius + 20, **kwargs)
        self.radius = radius
        self.teeth = teeth
        self.angle = 0
        self._gear_id = None
        self.draw_gear()

    def draw_gear(self):
        """Draw the gear at the current angle."""
        self.delete("all")
        cx = cy = self.radius + 10
        # outer circle
        self.create_oval(cx - self.radius, cy - self.radius, cx + self.radius, cy + self.radius, outline="black")
        # teeth as lines
        for i in range(self.teeth):
            a = self.angle + i * 2 * math.pi / self.teeth
            x = cx + self.radius * math.cos(a)
            y = cy + self.radius * math.sin(a)
            self.create_line(cx, cy, x, y)

    def rotate(self, delta):
        """Rotate the gear by delta radians."""
        self.angle += delta
        self.draw_gear()


class WheelApp(tk.Tk):
    """Main application window."""

    def __init__(self):
        super().__init__()
        self.title("Wheel GUI")
        self.geometry("400x400")

        self.gear = GearCanvas(self)
        self.gear.pack(pady=10)

        self.input_text = tk.Text(self, height=4)
        self.input_text.pack(fill="x", padx=10)

        self.command_var = tk.StringVar(value="reverse")
        ttk.Label(self, text="Command:").pack()
        ttk.OptionMenu(
            self,
            self.command_var,
            "reverse",
            "reverse",
            "uppercase",
            "lowercase",
            "custom",
        ).pack()

        self.custom_cmd = tk.Entry(self)
        self.custom_cmd.insert(0, "text[::-1]")
        self.custom_cmd.pack(fill="x", padx=10, pady=5)

        ttk.Button(self, text="Start", command=self.start).pack(side="left", padx=10)
        ttk.Button(self, text="Stop", command=self.stop).pack(side="right", padx=10)

        self.result_var = tk.StringVar()
        ttk.Label(self, textvariable=self.result_var).pack(pady=10)

        self.running = False

    def apply_command(self, text):
        cmd = self.command_var.get()
        if cmd == "reverse":
            return text[::-1]
        if cmd == "uppercase":
            return text.upper()
        if cmd == "lowercase":
            return text.lower()
        if cmd == "custom":
            try:
                return str(eval(self.custom_cmd.get(), {"text": text}))
            except Exception as exc:
                return f"Error: {exc}"
        return text

    def animate(self):
        if not self.running:
            return
        self.gear.rotate(math.pi / 16)
        self.after(100, self.animate)

    def start(self):
        text = self.input_text.get("1.0", tk.END).strip()
        result = self.apply_command(text)
        self.result_var.set(result)
        if not self.running:
            self.running = True
            self.animate()

    def stop(self):
        self.running = False


def main():
    WheelApp().mainloop()


if __name__ == "__main__":
    main()
