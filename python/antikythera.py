"""Simplified Antikythera mechanism simulation."""

from __future__ import annotations

import datetime
from dataclasses import dataclass


@dataclass
class Gear:
    """Represents a simple gear with a rotation period in days."""

    period: float  # days for a full rotation
    angle: float = 0.0  # current angle in degrees

    def update(self, days: float) -> None:
        self.angle = (days % self.period) / self.period * 360.0


class Antikythera:
    """Minimal model of the Antikythera mechanism."""

    def __init__(self, start_date: datetime.date | None = None) -> None:
        if start_date is None:
            start_date = datetime.date.today()
        self.start_date = start_date
        self.sun = Gear(365.25)
        self.moon = Gear(29.53)  # synodic month
        self.metonic = Gear(365.25 * 19)  # 19-year cycle

    def update_for(self, date: datetime.date) -> None:
        days = (date - self.start_date).days
        self.sun.update(days)
        self.moon.update(days)
        self.metonic.update(days)

    def moon_phase(self) -> str:
        phase_angle = self.moon.angle % 360
        phase = (phase_angle / 360) * 8
        idx = int(phase + 0.5) % 8
        names = [
            "New Moon",
            "Waxing Crescent",
            "First Quarter",
            "Waxing Gibbous",
            "Full Moon",
            "Waning Gibbous",
            "Last Quarter",
            "Waning Crescent",
        ]
        return names[idx]

    def info(self) -> str:
        return (
            f"Sun angle: {self.sun.angle:.1f}\n"
            f"Moon angle: {self.moon.angle:.1f}\n"
            f"Metonic angle: {self.metonic.angle:.1f}\n"
            f"Moon phase: {self.moon_phase()}"
        )


if __name__ == "__main__":
    mech = Antikythera()
    today = datetime.date.today()
    mech.update_for(today)
    print(mech.info())
