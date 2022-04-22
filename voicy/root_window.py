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


class root_window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)
        self.title("Voicy-Voiceassistant")
        self.geometry("800x600+80+80")
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.main_frame = tk.Frame(self, bg="grey")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        # Load modules
        self.modules_list = {
            # "modulename":[Unique-Key, Displayname, Popup/RootWindow, toolbar]
            "chat_section": [0, "Chat", "root_window", "toolbar"],
            "vorlage_root": [1, "Vorlage", "root_window", "toolbar"],
            "vorlage_popup": [2, "User Management", "popup", "toolbar"]
            }
        self.modules_root_window = []
        self.modules_popup = []

        # Initialize Modules
        for item in self.modules_list:
            print(item)
            if (self.modules_list[item][2] == "popup"):
                print("popup")
                imp_module = __import__(item, globals(), locals(), [item], 0)
                mod = getattr(imp_module, item)
                self.popup_window = tk.Toplevel(self)
                self.app = mod(self.popup_window)
                self.popup_window.withdraw()
                self.popup_window.deiconify()
            elif (self.modules_list[item][2] == "root_window"):
                print("root_window")
                imp_module = __import__(item, globals(), locals(), [item], 0)
                mod = getattr(imp_module, item)
                self.modules_root_window.append(mod(self.main_frame))

        self.menu_bar()
        self.tool_bar(self)
        self.change_main_frame(0)
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
            if (self.modules_list[item][2] == "root_window"):
                a = self.modules_list[item][0]
                self.toolbbutton = tk.Button(self.tool_bar, text=self.modules_list[item][1],
                                             command=lambda j=a: self.change_main_frame(j))
                self.toolbbutton.grid(row=0, column=self.modules_list[item][0],
                                      sticky="w")
            elif (self.modules_list[item][2] == "popup"):
                a = item
                self.toolbbutton = tk.Button(self.tool_bar, text=self.modules_list[item][1],
                                             command=lambda j=a: self.load_popup_window(j))
                self.toolbbutton.grid(row=0, column=self.modules_list[item][0],
                                      sticky="w")

        self.exit_button = tk.Button(self.tool_bar, text="Exit", command=quit)
        self.exit_button.grid(row=0, column=3, sticky="w")

    def change_main_frame(self, module):
        frame = self.modules_root_window[module]
        frame.tkraise()

    def load_popup_window(self, module):
        imp_module = __import__(module, globals(), locals(), [module], 0)
        mod = getattr(imp_module, module)
        self.popup_window = tk.Toplevel(self)
        self.app = mod(self.popup_window)
