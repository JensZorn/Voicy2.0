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
        self.root_canvas.rowconfigure(1, weight=1)

        self.main_frame = tk.Frame(self.root_canvas, bg="grey")
        self.main_frame.grid(row=1, column=0, sticky="nsew")
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        # Load modules
        self.modules_list = {
            "chat_section": [0, "Chat", "root_window"],
            "vorlage": [1, "Vorlage", "root_window"],
            "user_management": [2, "User Management", "popup"]
            }
        self.modules_root_window = []
        self.modules_popup = []

        for item in self.modules_list:
            print(item)
            if (self.modules_list[item][2]=="popup"):
                print("popup")
            elif (self.modules_list[item][2]=="root_window"):
                print("root_window")
                imp_module = __import__(item, globals(), locals(), [item], 0)
                mod = getattr(imp_module, item)
                self.modules_root_window.append(mod(self.main_frame))

        self.menu_bar()
        self.tool_bar(self.root_canvas)
        self.module_start(0)
        print("Done...")

    def menu_bar(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar)

        file_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def tool_bar(self, parent):
        self.tool_bar = tk.Frame(parent, bg="red", height=20)
        self.tool_bar.grid(row=0, column=0, sticky="new")
        for item in self.modules_list:
            if (self.modules_list[item][2]=="root_window"):
                a=self.modules_list[item][0]
                self.exit_button = tk.Button(self.tool_bar, text=self.modules_list[item][1],
                                command=lambda j=a: self.module_start(j))
                self.exit_button.grid(row=0, column=self.modules_list[item][0], sticky="w")
            elif (self.modules_list[item][2]=="popup"):
                a=item
                self.exit_button = tk.Button(self.tool_bar, text=self.modules_list[item][1],
                                command=lambda j=a: self.module_start1(j))
                self.exit_button.grid(row=0, column=self.modules_list[item][0], sticky="w")

        self.exit_button = tk.Button(self.tool_bar, text="Exit", command=quit)
        self.exit_button.grid(row=0, column=3, sticky="w")

    def module_start(self, module):
        print(module)
        frame = self.modules_root_window[module]
        frame.tkraise()

    def module_start1(self, module):
        print(module)
        imp_module = __import__(module, globals(), locals(), [module], 0)
        mod = getattr(imp_module, module)
        mod(self.main_frame)
