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


class vorlage_root(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="green")
        self.grid(row=0, column=0, sticky=tk.NSEW)
