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


class vorlage_popup():
    def __init__(self, parent):
        self.parent = parent
        self.parent.geometry("400x300")
        self.parent.resizable(False, False)
        self.frame = tk.Frame(self.parent)
        self.quitButton = tk.Button(self.frame, text='Quit', width=25, command=self.close_windows)
        self.quitButton.pack()
        self.frame.grid(row=0, column=0)

    def close_windows(self):
        self.parent.withdraw()
