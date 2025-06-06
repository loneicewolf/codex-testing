import tkinter as tk
from tkinter import ttk
import math


class WheelGUI:
    """Simple GUI with animated wheels that execute text commands."""

    def __init__(self, root):
        self.root = root
        self.root.title("Wheel Command Runner")

        self.text_var = tk.StringVar()

        input_frame = tk.Frame(root)
        tk.Label(input_frame, text="Input text:").pack(side="left")
        tk.Entry(input_frame, textvariable=self.text_var, width=30).pack(side="left", padx=5)
        input_frame.pack(pady=5)

        tk.Label(root, text="Command:").pack()
        self.command_var = tk.StringVar(value="Reverse")
        commands = ["Reverse", "Uppercase", "Lowercase"]
        ttk.Combobox(root, textvariable=self.command_var, values=commands, state="readonly").pack()

        custom_frame = tk.Frame(root)
        tk.Label(custom_frame, text="Custom Python expression (use 'text'):").pack(side="left")
        self.custom_var = tk.StringVar()
        tk.Entry(custom_frame, textvariable=self.custom_var, width=40).pack(side="left", padx=5)
        custom_frame.pack(pady=5)

        tk.Label(root, text="Speed:").pack()
        self.speed_var = tk.DoubleVar(value=5)
        tk.Scale(root, from_=1, to=10, orient="horizontal", variable=self.speed_var).pack()

        self.canvas = tk.Canvas(root, width=200, height=200)
        self.canvas.pack(pady=10)

        tk.Label(root, text="Output:").pack()
        self.output = tk.Text(root, width=40, height=4)
        self.output.pack()

        control = tk.Frame(root)
        tk.Button(control, text="Start", command=self.start).pack(side="left", padx=5)
        tk.Button(control, text="Stop", command=self.stop).pack(side="left", padx=5)
        control.pack(pady=5)

        self.angle = 0
        self.running = False

    def draw_wheels(self):
        self.canvas.delete("all")
        x1, y1, r1 = 50, 100, 40
        for i in range(8):
            ang = self.angle + i * 45
            x = x1 + r1 * math.cos(math.radians(ang))
            y = y1 + r1 * math.sin(math.radians(ang))
            self.canvas.create_line(x1, y1, x, y)
        self.canvas.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1)

        x2, y2, r2 = 150, 100, 40
        for i in range(6):
            ang = -self.angle + i * 60
            x = x2 + r2 * math.cos(math.radians(ang))
            y = y2 + r2 * math.sin(math.radians(ang))
            self.canvas.create_line(x2, y2, x, y, fill="blue")
        self.canvas.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, outline="blue")

        self.angle = (self.angle + self.speed_var.get()) % 360

    def execute_command(self):
        text = self.text_var.get()
        cmd = self.command_var.get()
        if cmd == "Reverse":
            result = text[::-1]
        elif cmd == "Uppercase":
            result = text.upper()
        elif cmd == "Lowercase":
            result = text.lower()
        else:
            result = text
        expr = self.custom_var.get().strip()
        if expr:
            try:
                result = str(eval(expr, {"text": result}, {}))
            except Exception as exc:
                result = f"Error: {exc}"
        self.output.delete("1.0", "end")
        self.output.insert("1.0", result)

    def step(self):
        if self.running:
            self.draw_wheels()
            self.execute_command()
            self.root.after(100, self.step)

    def start(self):
        if not self.running:
            self.running = True
            self.step()

    def stop(self):
        self.running = False


if __name__ == "__main__":
    root = tk.Tk()
    gui = WheelGUI(root)
    root.mainloop()
