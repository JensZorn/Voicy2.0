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
# import random
import tkinter as tk
from tkinter import ttk
from threading import Thread, enumerate
from queues import to_nlp, from_nlp


class chat_section(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(row=0, column=0, sticky=tk.NSEW)
        self.modu = Thread(target=self.main, name="chat_section",
                           args=(self, ), daemon=True)
        self.active_threads = enumerate()
        print(self.active_threads)
        chat_section_alive = False
        for item in self.active_threads:
            # print(item)
            if(item.getName() == "chat_section"):
                chat_section_alive = True
        if not chat_section_alive:
            self.modu.start()

    def main(self, parent):
        self.label = ttk.Label(parent, text="Command:")
        self.label.grid(row=2, column=0)
        self.written_input_entry = ttk.Entry(parent, width=70)
        self.written_input_entry.grid(row=2, column=1)
        self.written_input_entry.bind("<Return>", self.send_written_input)
        self.button_send = ttk.Button(parent, text="SEND",
                                      command=lambda:
                                      self.send_written_input(True))

        self.button_send.grid(row=2, column=4, pady=2)

        self.chat_history = tk.Canvas(parent, bg="blue")
        self.chat_history.grid(row=0, column=0, columnspan=6, sticky=tk.NSEW)
        self.chat_history_scroll = ttk.Scrollbar(parent, orient="vertical",
                                                 command=self.chat_history.yview)
        self.chat_history_scroll.grid(row=0, column=6, sticky="ns")
        self.chat_history_frame = ttk.Frame(self.chat_history)
        self.chat_history_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.chat_history.configure(
            scrollregion=self.chat_history_frame.bbox("all"))
        self.chat_history_frame_window = self.chat_history.create_window((0, 0),
                                                                         window=self.chat_history_frame, anchor="nw")
        self.chat_history.configure(
            yscrollcommand=self.chat_history_scroll.set)

        # Start the chat greeting the user

        # self.chat_bubble("bot", "Hallo, ich bin Voicy! Wie ist dein Name?")

        while True:
            # try:
            self.userinput = from_nlp.get()
            self.chat_bubble("bot", self.userinput)

            parent.update_idletasks()
            self.chat_history.configure(
                    scrollregion=self.chat_history.bbox("all"))
            self.chat_history.configure(
                    yscrollcommand=self.chat_history_scroll.set)
            self.chat_history.yview_moveto(1)

            # except Exception:
            # print("There has been an error!")

    def send_written_input(self, event):

        self.writtencommand = self.written_input_entry.get()
        self.written_input_entry.delete(0, tk.END)
        self.chat_bubble("user", self.writtencommand)
        to_nlp.put(self.writtencommand)

    def chat_bubble(self, owner, text):
        self.column, self.row = list(self.chat_history_frame.grid_size())
        chatrow = owner + str(self.row)
        if owner == "user":
            self.column = 1
        elif owner == "bot":
            self.column = 0
        chatrow = tk.Text(self.chat_history_frame, height=3, width=50)
        chatrow.grid(row=self.row, column=self.column)
        chatrow.insert(1.0, text)
