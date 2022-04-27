###############################################################################
#
#
#
#               Voiceassistant
#
#               by Sarah Köster, Dennis Stoy, Jens Zorn
#
#
#               Vorlage für ein Modul, welches im eigenen window angezeigt
#               werden soll.
#
#
# <°))))><
###############################################################################
import tkinter as tk
from tkinter import ttk

# Die Start-Klasse des Pop-Up Fensters muss so heißen, wie die Datei (ohne .py)


class vorlage_popup():
    def __init__(self, parent):
        # parent bezieht sich auf tk.Toplevel, welches in der root_window
        # initialisiert wurde (Zeile 51-67). In Zeile 59 wird dem Modul das
        # parent-Objekt übergeben
        self.parent = parent
        # .title legt den Namen des Pop-Up Fensters fest
        self.parent.title("Vorlage Popup")
        # .geometry legt die Größe des Fensters fest
        # (Höhe x Breite + Abstand linker Rand + Abstand oberer Rand)
        self.parent.geometry("400x300+50+50")
        # legt fest, ob die Größe des Fensters verändert werden kann True/False
        self.parent.resizable(False, False)
        # -topmost legt fest, dass das Pop-Up immer ganz oben angezeigt werden
        # soll, also immer vor dem root_window ist
        self.parent.attributes('-topmost', 'true')
        # overrideredirect schaltet die Fensterleiste aus (also wo man
        # minimiert, maximiert und das 'x' ist)
        # self.parent.overrideredirect(True)
        # WM_DELETE_WINDOW ist das 'X' in der Fensterleiste. Diese Zeile ist
        # wichtig, da sie verhindert, dass das Fenster "zerstört" wird und als
        # Objekt nicht mehr aufrufbar ist.
        self.parent.protocol("WM_DELETE_WINDOW", self.close_window)
        # Frame, der das gesamte tk.Toplevel ausfüllt. Kann zur Anordnung Der
        # Widgets verwendet werden
        self.frame = ttk.Frame(self.parent)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.quitButton = ttk.Button(self.frame,
                                     text='Quit',
                                     width=25,
                                     command=self.close_window)
        self.quitButton.grid()

    # close_window ist ein Beispiel, wie man das Fenster "schließen" kann, ohne
    # das es "zerstört" wird. .withdraw() versteckt das Fenster, ohne das es in
    # der Taskleiste angezeigt wird.
    def close_window(self):
        self.parent.withdraw()
