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
from root_window import root_window
import tkinter as tk
from tkinter import ttk
from threading import Thread
from standard_theme import standard_theme


class App(tk.Toplevel):

    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.geometry("400x300+50+50")
        self.resizable(False, False)
        self.attributes('-topmost', 'true')
        self.overrideredirect(True)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        # self.style, self.colors, self.menu_theme = standard_theme(self)

        self.canvas = tk.Canvas(self)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        label = ttk.Label(self.canvas, text="Hello World")
        label.grid()
        # self.root.after(500, lambda: test())
        self.after(8000, lambda: self.destroy())
        # self.root.mainloop()


class test(Thread):
    def __init__(self):
        Thread.__init__(self, daemon=True)
        self.start()

    def run(self):
        imp_module = __import__("nlp_core", globals(),
                                locals(), ["nlp_core"], 0)
        module = getattr(imp_module, "nlp_core")
        module()


if __name__ == "__main__":
    print("Loading, please wait!")

    root = root_window()
    app = App(root)
    root.mainloop()
