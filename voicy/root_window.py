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

        self.menu_bar()
        self.tool_bar(self.root_canvas)
        print("Done...")

    def menu_bar(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar)
        file_menu.add_command(label="Chat anzeigen",
                                command=self.module_start(self.main_frame, "chat_section"))
        file_menu.add_command(label="Benutzer anlegen", command=lambda: self.module_start(self, "user_management"))
        file_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def tool_bar(self, parent):
        self.tool_bar = tk.Frame(parent, bg="red", height=20)
        self.tool_bar.grid(row=0, column=0, sticky="new")
        self.chat_button = tk.Button(self.tool_bar, text="Chat anzeigen",
                                command=self.module_start(self.main_frame, "chat_section"))
        self.chat_button.grid(row=0, column=0, sticky="w")
        self.user_button = tk.Button(self.tool_bar, text="User Management",
                                command=lambda: self.module_start(self, "user_management"))
        self.user_button.grid(row=0, column=1, sticky="w")
        self.exit_button = tk.Button(self.tool_bar, text="Exit", command=quit)
        self.exit_button.grid(row=0, column=2, sticky="w")

    def module_start(self, parent, module):
        imp_module = __import__(module, globals(), locals(), [module], 0)
        mod = getattr(imp_module, module)
        mod(parent)
