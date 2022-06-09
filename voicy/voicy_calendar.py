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
from tkinter import OptionMenu

from time import strftime, sleep



class voicy_calendar():
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Kalender")
        self.parent.geometry("600x300")
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
        self.cal.grid(row=1, column=1)

        self.takeButton = ttk.Button(self.frame,
                                     text='Übernehme das Datum',
                                     width=25,
                                     )
        self.takeButton.grid(row=3, column=0)

        self.HoursList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16",
                          "17", "18", "19", "20", "21", "22", "23", "24"]
        self.MinuteList = ["00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]

        self.clicked = StringVar()

        self.drophours = ttk.OptionMenu(self.frame, self.clicked, *self.HoursList)
        self.drophours.config(width=5)
        self.drophours.grid(row=1, column=2)

        self.clicked1 = StringVar()

        self.dropminute = ttk.OptionMenu(self.frame, self.clicked1, *self.MinuteList)
        self.dropminute.config(width=5)
        self.dropminute.grid(row=1, column=3)



        #self.button = ttk.Button(self.frame, text="click here", width=25)
        #self.button.grid(row=3, column=3)


        self.thread=Thread(target=self.clock_update,args=(self.frame, ), daemon=True)
        self.thread.start()

    def clock_update(self, parent):
        while True:
            self.clock.set(strftime('%H:%M:%S %p'))
            parent.update_idletasks()
            sleep(1)










    #def callback(self):

        #self.label.Uhrzeit.configure(text="Die ausgewählte Uhrzeit ist {}".format.self.takeTime.set())
        #self.takeTime.trace(self.frame, self.callback)








    def close_window(self):
            self.parent.withdraw()







