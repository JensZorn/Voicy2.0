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
        self.parent.title("Vorlage Popup")
        self.parent.geometry("400x300")
        self.parent.resizable(False, False)
        self.parent.attributes('-topmost', 'true')
        self.frame = ttk.Frame(self.parent)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.quitButton = ttk.Button(self.frame,
                                     text='Quit',
                                     width=25,
                                     command=self.close_window)
        self.quitButton.grid()

    def close_window(self):
        self.parent.withdraw()
