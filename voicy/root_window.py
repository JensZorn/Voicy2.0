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
import importlib


class root_window(tk.Tk):
    def __init__(self):
        print("Loading, please wait!")
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
        print("Done...")

    def menu_bar(self, main_frame):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar)
        file_menu.add_command(label="Exit")
        menu_bar.add_cascade(label="File", menu=file_menu)

        menu_bar.add_command(label="Chat anzeigen",
                             command=self.module_start(self.main_frame, "chat_section"))
        menu_bar.add_command(label="Benutzer anlegen", command=lambda: self.module_start(self, "user_management"))
        menu_bar.add_command(label="Exit", command=quit)

    def module_start(self, parent, module):
        imp_module = __import__(module, globals(), locals(), [module], 0)
        mod = getattr(imp_module, module)
        mod(parent)
