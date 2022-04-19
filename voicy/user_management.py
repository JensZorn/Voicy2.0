import tkinter as tk




class user_management(tk.Tk):
        
    def __init__(self):
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
        
        
