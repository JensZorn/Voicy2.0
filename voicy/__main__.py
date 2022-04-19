#!/usr/bin/env python3 ########################################################
# -*- coding: UTF-8 -*-
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
from sqlite3.dbapi2 import connect
import tkinter as tk
import sqlite3 as sq3
from interaction import show_interaction
from user_management import user_management
from threading import Thread
from queue import Queue

interaction_queue = Queue(maxsize=0)    # type: object
monitoring_queue = Queue(maxsize=0)     # type: object


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

        self.label = tk.Label(self.main_frame, text="Command:")
        self.label.grid(row=2, column=0)
        self.written_input_entry = tk.Entry(self.main_frame, width=70)
        self.written_input_entry.grid(row=2, column=1)
        self.written_input_entry.bind("<Return>", self.send_written_input)
        self.button_send = tk.Button(self.main_frame, text="SEND",
                                     command=lambda: self.send_written_input(True))
        self.button_send.grid(row=2, column=4, pady=2)

        self.button_quit = tk.Button(
            self.main_frame, text="QUIT", command=quit)
        self.button_quit.grid(row=2, column=5)

        self.button_add_user = tk.Button(
            self.main_frame, text="Benutzer anlegen", command=self.user_window)
        self.button_add_user.grid(row=2, column=6)

        self.interaction = Thread(target=show_interaction,
                                  args=(self.main_frame,
                                        interaction_queue, monitoring_queue),
                                  daemon=True)
        self.interaction.start()

    def user_window(self):
        self.user_window = user_management()

    def send_written_input(self, event):

        self.writtencommand = self.written_input_entry.get()
        self.written_input_entry.delete(0, tk.END)
        interaction_queue.put(self.writtencommand)

    def create_new_table(self):
        self.connection = sq3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.crateTable = """ CREATE TABLE IF NOT EXISTS user (
                        id, firstName, lastName);"""
        self.cursor.execute(self.crateTable)
        self.connection.commit()
        self.connection.close()

    def new_table_entry(self):
        self.connection = sq3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(""" INSERT INTO user VALUES (?,?,?)""",
                            ("1", "Dennis", "Stoy"))
        self.connection.commit()
        self.connection.close()

    def show_table(self):
        self.connection = sq3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM user")
        self.content = self.cursor.fetchall()
        self.connection.close()
        print(self.content)


if __name__ == "__main__":
    root = root_window()
    root.geometry("1000x600+50+50")
    root.mainloop()
