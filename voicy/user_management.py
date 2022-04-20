import tkinter as tk


class user_management(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)
        self.title("Create a new User")
        self.geometry("500x300")
        self.LabelVorname = tk.Label(self, text="Vorname")
        self.LabelVorname.pack()
        self.EntryVorname = tk.Entry(self)
        self.EntryVorname.pack()
        self.LabelNachname = tk.Label(self, text="Nachname")
        self.LabelNachname.pack()
        self.EntryNachname = tk.Entry(self)
        self.EntryNachname.pack()
        self.Buttonsenden = tk.Button(self, text="Ok")
        self.Buttonsenden.pack()

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
