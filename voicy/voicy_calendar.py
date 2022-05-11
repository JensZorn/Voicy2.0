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
from tkinter import StringVar
from tkcalendar import Calendar
from datetime import datetime
from pytz import timezone
from datetime import date
from threading import Thread

from time import strftime, sleep



class voicy_calendar():
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Kalender")
        self.parent.geometry("400x300")
        self.parent.resizable(False, False)
        self.parent.attributes('-topmost', 'true')
        self.parent.protocol("WM_DELETE_WINDOW", self.close_window)
        self.frame = ttk.Frame(self.parent)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.quitButton = ttk.Button(self.frame,
                                     text='Quit',
                                     width=25,
                                     command=self.close_window)

        self.quitButton.grid(row=0, column=0)

        self.now = datetime.now()
        self.clock = StringVar()
        self.lbl = ttk.Label(self.frame, font=('calibri', 12, 'bold'),
                    background='grey',
                    foreground='white',
                    textvariable=self.clock
                    )

        self.lbl.grid(row=1, column=0)

        self.cal = Calendar(self.frame, today=date.today())
        self.cal.grid(sticky="nsew")

        self.takeButton = ttk.Button(self.frame,
                                     text='Übernehme das Datum',
                                     width=25,
                                     )
        self.takeButton.grid(row=3, column=0)

        self.thread=Thread(target=self.clock_update,args=(self.frame, ), daemon=True)
        self.thread.start()

    def clock_update(self, parent):
        while True:
            self.clock.set(strftime('%H:%M:%S %p'))
            parent.update_idletasks()
            sleep(1)











    def close_window(self):
            self.parent.withdraw()







