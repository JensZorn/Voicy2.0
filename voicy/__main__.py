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


class App(Thread):

    def __init__(self):
        Thread.__init__(self, daemon=True)
        self.start()

    def run(self):
        self.root = tk.Tk()
        self.root.title("Voicy Splash Screen")
        self.root.geometry("400x300+50+50")
        self.root.resizable(False, False)
        self.root.attributes('-topmost', 'true')
        self.root.overrideredirect(True)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.style, self.colors, self.menu_theme = standard_theme(self.root)

        self.canvas = tk.Canvas(self.root)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        label = ttk.Label(self.canvas, text="Hello World")
        label.pack()
        self.root.after(500, lambda: test())
        self.root.after(8000, lambda: self.root.destroy())
        self.root.mainloop()


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
    app = App()
    root = root_window()
    root.mainloop()
