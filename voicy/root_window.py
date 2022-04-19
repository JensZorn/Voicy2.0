###############################################################################
#
#
#
#               Voiceassistant
#
#               by Sarah Köster, Dennis Stoy, Jens Zorn
#
#
#               ...
#
#
#
# <°))))><
###############################################################################
import tkinter as tk
from threading import Thread
from queues import interaction_queue
import importlib


class root_window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Voiceassistant")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.root_canvas = tk.Canvas(self, bg="black")
        self.root_canvas.grid(row=1, column=0, sticky=tk.NSEW)
        self.root_canvas.columnconfigure(0, weight=1)
        self.root_canvas.rowconfigure(0, weight=1)

        self.main_frame = tk.Frame(self.root_canvas, bg="grey")
        self.main_frame.grid(row=1, column=0, sticky=tk.NSEW)

        self.menu_bar(self.main_frame)


    def menu_bar(self, main_frame):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar)
        file_menu.add_command(label="Exit")
        menu_bar.add_cascade(label="File", menu=file_menu)

        menu_bar.add_command(label="Chat anzeigen",
                             command=lambda: self.chat_section(self.main_frame))
        menu_bar.add_command(label="Benutzer anlegen", command=self.user_window)
        menu_bar.add_command(label="Exit", command=quit)



    def chat_section(self, parent):
        from chat_section import chat_section
        self.chat_section = Thread(target=chat_section,
                                          args=(parent, ), daemon=True)
        self.chat_section.start()

    def user_window(self):
        from user_management import user_management
        self.user_window = user_management()
