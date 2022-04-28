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
from tkinter import ttk
from standard_theme import standard_theme


class root_window(tk.Tk):

    # The dictionary of existent modules
    modules_list = {
        # "modulename":[Unique-Key, gepeicherte Instanz, Displayname,
        #               Popup/RootWindow, toolbar]
        #"chat_section": [0, "chat_section", "", "Chat", "root_window", True],
        "user_management": [1, "user_management", "", "User Management",
                            "popup", True],
        "voicy_calendar": [2, "voicy_calendar", "", "Kalender", "popup", True],
        "vorlage_root": [8, "vorlage_root", "", "Vorlage", "root_window",
                         True],
        "vorlage_popup": [9, "vorlage_popup", "", "User Management", "popup",
                          True]
        }

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)
        self.title("Voicy-Voiceassistant")
        self.geometry("800x600+80+80")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.style, self.colors, self.menu_theme = standard_theme()

        self.main_frame = ttk.Frame(self)
        self.main_frame.grid(row=1, column=0, sticky="nsew")
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        # Initialize Modules
        for item in self.modules_list:
            imp_module = __import__(item, globals(), locals(), [item], 0)
            module = getattr(imp_module, item)
            if (self.modules_list[item][4] == "popup"):
                self.popup_window = tk.Toplevel(self)
                self.popup_window.columnconfigure(0, weight=1)
                self.popup_window.rowconfigure(0, weight=1)
                module(self.popup_window)
                self.modules_list[item][2] = self.popup_window
                self.popup_window.withdraw()
                # self.popup_window.deiconify()
            elif (self.modules_list[item][4] == "root_window"):
                self.modules_list[item][2] = module(self.main_frame)
                # self.modules_root_window.append(mod(self.main_frame))
            else:
                print("Error initializing modules")

        self.menu_bar()
        self.tool_bar(self)
        self.change_main_frame(self.modules_list["vorlage_root"][2])
        print("Done...")

    def menu_bar(self):
        menu_bar = tk.Menu(self)
        menu_bar.config(**self.menu_theme)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.config(**self.menu_theme)
        file_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.config(**self.menu_theme)
        edit_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)
        view_menu = tk.Menu(menu_bar, tearoff=0)
        view_menu.config(**self.menu_theme)
        view_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="View", menu=view_menu)
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.config(**self.menu_theme)
        help_menu.add_command(label="Exit", command=quit)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def tool_bar(self, parent):
        self.tool_bar = ttk.Frame(parent)
        self.tool_bar.grid(row=0, column=0, sticky="new")
        for item in self.modules_list:
            if(self.modules_list[item][4] == "root_window"
               and self.modules_list[item][5]):
                mod_inst = self.modules_list[item][2]
                self.tbbutton = ttk.Button(self.tool_bar,
                                           text=self.modules_list[item][3],
                                           command=(lambda j=mod_inst:
                                                    self.change_main_frame(j)))
                self.tbbutton.grid(row=0,
                                   column=self.modules_list[item][0],
                                   sticky="w")
            elif(self.modules_list[item][4] == "popup"
                 and self.modules_list[item][5]):
                mod_inst = self.modules_list[item]
                self.tbbutton = ttk.Button(self.tool_bar,
                                           text=self.modules_list[item][3],
                                           command=(lambda j=mod_inst:
                                                    self.show_popup_window(j)))
                self.tbbutton.grid(row=0,
                                   column=self.modules_list[item][0],
                                   sticky="w")
        # Der Exit Button soll bestimmt irgendwann weg
        self.exit_tbbutton = ttk.Button(self.tool_bar,
                                        text="Exit",
                                        command=quit)
        self.exit_tbbutton.grid(row=0, column=10, sticky="w")

    def change_main_frame(self, module):
        module.tkraise()

    def show_popup_window(self, module):
        try:
            module[2].deiconify()
        except Exception:
            print("Mist, Popup Fenster Problem!")
            # imp_module = __import__(module[1], globals(), locals(),
            # [module[1]], 0)
            # modul = getattr(imp_module, module[1])
            # self.popup_window = tk.Toplevel(self)
            # self.popup_window.columnconfigure(0, weight=1)
            # self.popup_window.rowconfigure(0, weight=1)
            # modul(self.popup_window)
            # print(type(module))
            # print(self.modules_list[module[1]])
            # del self.modules_list[module[1]][2]
            # self.modules_list[module[1]].insert(2, self.popup_window)
            # self.popup_window.withdraw()
