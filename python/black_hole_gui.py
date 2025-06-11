import tkinter as tk
from tkinter import colorchooser
import math

class BlackHoleSimulator(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Black Hole Gravity Simulator")
        self.geometry("800x600")

        # Simulation parameters
        self.mass = tk.DoubleVar(value=10.0)
        self.show_trace = tk.BooleanVar(value=True)
        self.auto = tk.BooleanVar(value=False)
        self.arrow_color = "red"

        # Set up UI controls
        control_frame = tk.Frame(self)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        tk.Label(control_frame, text="Mass M").pack()
        tk.Scale(control_frame, from_=1, to=50, orient=tk.HORIZONTAL,
                 variable=self.mass, resolution=1).pack(fill=tk.X)

        tk.Checkbutton(control_frame, text="Show Trace",
                       variable=self.show_trace).pack(anchor="w")
        tk.Checkbutton(control_frame, text="Auto Mode",
                       variable=self.auto).pack(anchor="w")

        tk.Button(control_frame, text="Pick Color",
                  command=self.pick_color).pack(fill=tk.X, pady=2)
        tk.Button(control_frame, text="Reset",
                  command=self.reset).pack(fill=tk.X, pady=2)

        self.info = tk.Label(control_frame, text="")
        self.info.pack(pady=4)

        # Canvas for drawing
        self.canvas = tk.Canvas(self, width=600, height=600, bg="black")
        self.canvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.center = (300, 300)
        self.horizon = 20  # radius of event horizon
        self.reset()

        # Bind keyboard
        self.bind("<KeyPress>", self.on_key)

        self.after(20, self.update_sim)

    def pick_color(self) -> None:
        color = colorchooser.askcolor(color=self.arrow_color)
        if color[1]:
            self.arrow_color = color[1]

    def reset(self) -> None:
        self.canvas.delete("all")
        x0, y0 = self.center
        self.canvas.create_oval(x0 - self.horizon, y0 - self.horizon,
                                x0 + self.horizon, y0 + self.horizon,
                                fill="grey20", outline="")
        # particle starting position and velocity
        self.pos = [x0 + 150, y0]
        self.vel = [0.0, -1.5]
        self.trace_points = []

    def on_key(self, event: tk.Event) -> None:
        if event.keysym == 'Up':
            self.vel[1] -= 0.5
        elif event.keysym == 'Down':
            self.vel[1] += 0.5
        elif event.keysym == 'Left':
            self.vel[0] -= 0.5
        elif event.keysym == 'Right':
            self.vel[0] += 0.5

    def update_sim(self) -> None:
        x0, y0 = self.center
        px, py = self.pos
        dx = px - x0
        dy = py - y0
        r = math.hypot(dx, dy)
        if r == 0:
            r = 0.1
        # gravitational acceleration
        acc_mag = self.mass.get() / r**2
        acc = [-acc_mag * dx / r, -acc_mag * dy / r]
        self.vel[0] += acc[0]
        self.vel[1] += acc[1]
        if self.auto.get():
            self.vel[0] *= 0.99
            self.vel[1] *= 0.99
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        # Draw
        self.canvas.delete("particle")
        self.canvas.delete("arrow")
        self.canvas.create_oval(px - 5, py - 5, px + 5, py + 5,
                                fill="white", tags="particle")
        # arrow for acceleration
        ax = px + acc[0]*100
        ay = py + acc[1]*100
        self.canvas.create_line(px, py, ax, ay, arrow=tk.LAST,
                                fill=self.arrow_color, tags="arrow")
        if self.show_trace.get():
            self.trace_points.append((px, py))
            for p1, p2 in zip(self.trace_points, self.trace_points[1:]):
                self.canvas.create_line(p1[0], p1[1], p2[0], p2[1],
                                        fill="yellow", tags="trace")
        info_text = f"r = {r:.1f}  |  speed = {math.hypot(*self.vel):.1f}"
        self.info.configure(text=info_text)

        if r < self.horizon:
            self.info.configure(text=info_text + "  |  Inside horizon!")

        self.after(20, self.update_sim)


if __name__ == "__main__":
    BlackHoleSimulator().mainloop()
