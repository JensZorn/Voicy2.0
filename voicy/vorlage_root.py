###############################################################################
#
#
#
#               Voiceassistant
#
#               by Sarah Köster, Dennis Stoy, Jens Zorn
#
#
#               Vorlage für ein Modul, welches im root_window angezeigt
#               werden soll.
#
#
# <°))))><
###############################################################################
import tkinter as tk
from tkinter import ttk

# initialisiert einen ttk.Frame, dessen parent der self.main_frame des
# root_window ist.
# Startklasse muss so benannt werden, wie die Datei


class vorlage_root(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=0, sticky=tk.NSEW)
