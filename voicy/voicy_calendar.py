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
from tkcalendar import Calendar
from datetime import datetime
from pytz import timezone
from datetime import date
from datetime import time



class voicy_calendar():
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Kalender")
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

        self.cal = Calendar(self.frame, selectmode='day',
                       year=2022, month=4,
                       day=26)

        self.cal.grid()

        self.takeButton = ttk.Button(self.frame)
        self.takeButton.grid(row = 3, column = 3)




    def close_window(self):
        self.parent.withdraw()