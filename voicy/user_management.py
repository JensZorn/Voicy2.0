import tkinter as tk
from tkinter import ttk
import sqlite3 as sq3


class user_management():

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.parent.title("User Management")
        self.parent.geometry("400x300+50+50")
        self.parent.resizable(False, False)
        self.parent.attributes('-topmost', 'true')
        self.parent.protocol("WM_DELETE_WINDOW", self.close_window)
        self.container = tk.Frame(self.parent)
        self.container.pack(side="top", fill="both", expand=True)
        #self.container.columnconfigure(1, weight=1)
        #self.container.rowconfigure(0, weight=0)
        self.container.grid_rowconfigure(0, weight=0)
        self.container.grid_columnconfigure(0, weight=1)

        
        
        self.frames = {}
        for F in (user_login, new_user):
            page_name = F.__name__
            frame =F(parent_frame= self.container, controller = self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame("user_login")
        
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def close_window(self):
        self.parent.withdraw()
        


class user_login(tk.Frame):
    def __init__(self, parent_frame, controller):
        tk.Frame.__init__(self, parent_frame)
        self.controller = controller
        
        self.username_login = tk.Label(self, text="Username: ")
        self.username_login.pack()
    
        
        self.username_login_entry = tk.Entry(self)
        self.username_login_entry.pack()
        

        self.passwd_login = tk.Label(self, text="Passwort: ")
        self.passwd_login.pack()
        
        self.passwd_login_entry = tk.Entry(self)
        self.passwd_login_entry.pack()
        
        self.button_login = tk.Button(self, text="Login")
        self.button_login.pack()

        self.button_sign_in = tk.Button(self, text="Benutzer anlegen",
                                         command=lambda: controller.show_frame("new_user"))
        self.button_sign_in.pack()      


    def close_window(self):
        self.parent.withdraw()

class new_user(tk.Frame):
    def __init__(self, parent_frame, controller):
        tk.Frame.__init__(self, parent_frame)
        self.controller = controller
        
        self.e_mail = tk.Label(self, text="Email Adresse")
        self.e_mail.pack()
        self.Entry_e_mail = tk.Entry(self)
        self.Entry_e_mail.pack()
        
        self.user_name = tk.Label(self, text="Benutzername")
        self.user_name.pack()
        self.Entry_user_name = tk.Entry(self)
        self.Entry_user_name.pack()
        
        self.password_first = tk.Label(self, text="Passwort")
        self.password_first.pack()
        self.Entry_password_first = tk.Entry(self)
        self.Entry_password_first.pack()
        
        self.password_second = tk.Label(self, text="Passwort wiederholen")
        self.password_second.pack()
        self.Entry_password_second = tk.Entry(self)
        self.Entry_password_second.pack()
        
        self.Buttonsenden = tk.Button(self, text="Ok", command=self.new_table_entry)
        self.Buttonsenden.pack()
        self.Buttonanzeigen = tk.Button(self, text="Anzeigen", command=self.show_table)
        self.Buttonanzeigen.pack()



    def close_window(self):
        self.parent.withdraw()

    def create_new_table(self):
        self.connection = sq3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.crateTable = """ CREATE TABLE IF NOT EXISTS user (
                        id INT  AUTO_INCREMENT,
                        firstName VARCHAR(255), lastName VARCHAR(255));"""
                        
                        
        self.cursor.execute(self.crateTable)
        self.connection.commit()
        self.connection.close()
        
        print("Table createt")

    def new_table_entry(self):
        self.create_new_table()
        
        self.input_e_mail = self.Entry_e_mail.get()
        self.input_user_name = self.Entry_user_name.get()
        self.input_password_first = self.Entry_password_first.get()
        self.input_password_second = self.Entry_password_second.get()
        
        self.connection = sq3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.input_e_mail = self.input_e_mail
        self. input_user_name = self.input_user_name
        self.input_password_first = self.input_password_first
        self. input_password_second = self.input_password_second
        
        self.cursor.execute(""" INSERT INTO user VALUES (?,?,?,?)""",
                            ("id", self.input_e_mail, self.input_user_name,
                             self.input_password_first, self.input_password_second))

        
        self.connection.commit()
        self.connection.close()

        print("Entry added")
        

    def show_table(self):
        self.connection = sq3.connect("database.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM user")
        for dsatz in self.cursor:
            print(dsatz[0], dsatz[1], dsatz[2], dsatz[3])
        
        self.connection.close()
        
        print("Show New Entry")
        

        
        
        
        
        
        
        
        
        
        
        
        
 