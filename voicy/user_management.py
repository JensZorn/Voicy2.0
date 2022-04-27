import tkinter as tk
from tkinter import ttk


class user_management():

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.parent.title("User Management")
        self.parent.geometry("400x300+50+50")
        self.parent.resizable(False, False)
        self.parent.attributes('-topmost', 'true')
        self.parent.protocol("WM_DELETE_WINDOW", self.close_window)
        self.frame = ttk.Frame(self.parent)
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.LabelVorname = tk.Label(self.frame, text="Vorname")
        self.LabelVorname.pack()
        self.EntryVorname = tk.Entry(self.frame)
        self.EntryVorname.pack()
        self.LabelNachname = tk.Label(self.frame, text="Nachname")
        self.LabelNachname.pack()
        self.EntryNachname = tk.Entry(self.frame)
        self.EntryNachname.pack()
        self.Buttonsenden = tk.Button(self.frame, text="Ok")
        self.Buttonsenden.pack()

    def close_window(self):
        self.parent.withdraw()

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
