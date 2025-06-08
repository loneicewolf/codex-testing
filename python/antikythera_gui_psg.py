"""PySimpleGUI version of the Antikythera mechanism interface."""

from __future__ import annotations

from datetime import date

import PySimpleGUI as sg

from antikythera import Antikythera


def main() -> None:
    mech = Antikythera()
    layout = [
        [sg.Text("Date (YYYY-MM-DD):"), sg.Input(date.today().isoformat(), key="-DATE-")],
        [sg.Button("Update")],
        [sg.Multiline(size=(40, 6), key="-OUT-")],
    ]
    window = sg.Window("Antikythera - PySimpleGUI", layout)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Exit"):
            break
        if event == "Update":
            try:
                d = date.fromisoformat(values["-DATE-"])
            except ValueError:
                continue
            mech.update_for(d)
            window["-OUT-"].update(mech.info())
    window.close()


if __name__ == "__main__":
    main()
