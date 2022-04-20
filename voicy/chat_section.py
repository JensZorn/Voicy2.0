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
import spacy
from threading import Thread, enumerate
from queues import interaction_queue
nlp = spacy.load("de_core_news_lg")

"""
randomanswer = ["Oh, wie schön!", "Sehr interessant!", "Wenn Sie meinen,...", "Ach, das hätte ich nicht gedacht.",
                "Manchmal fällt ein Sack Reis um und das interessiert auch niemanden"]

reactions = {"hallo": "oh, willkommen!",
             "hunger": "Das Einzige was ich essen kann ist in deiner Steckdose!",
             "zeit": "Ja, die Zeit rennt extrem schnell.",
             "danke": "Sehr gerne, ich bin immer für dich da!",
             "trinken": "Kein Bier vor vier!",
             "sitzen": "Sitzen ist was für dicke, faule Säcke",
             "langeweile": "Man könnte bei langeweile etwas essen gehen.",
             "stop": "Ok, ich glaube ich bin zu weit gegangen",
             "glaube": "Das kann ich mir nicht vorstellen",
             "laufen": "Zum Glück musst du mich immer transportieren, darauf hätte ich keine Lust.",
             "freude": "Freude ist schön, vor allem wenn man sich die Freude teilen darf.",
             "weihnachten":"Weihnachten ist das Fest der Liebe!",
             "einkaufsliste": "Ich habe es auf die Einkaufsliste hinzugefügt"}
"""


class learning():
    def __init__(self):
        pass


class chat_section():
    def __init__(self, parent):
        super().__init__()
        self.modu = Thread(target=self.main, name="chat_section", args=(parent, ), daemon=True)
        active_threads = enumerate()
        print (active_threads)
        chat_section_alive=False
        for item in active_threads:
            print(item)
            if(item.getName()=="chat_section"):
                chat_section_alive=True
        if not chat_section_alive:
            self.modu.start()

    def main(self, parent):
        self.label = tk.Label(parent, text="Command:")
        self.label.grid(row=2, column=0)
        self.written_input_entry = tk.Entry(parent, width=70)
        self.written_input_entry.grid(row=2, column=1)
        self.written_input_entry.bind("<Return>", self.send_written_input)
        self.button_send = tk.Button(parent, text="SEND",
                                             command=lambda: self.send_written_input(True))
        self.button_send.grid(row=2, column=4, pady=2)

        self.chat_history = tk.Canvas(parent, bg="blue")
        self.chat_history.grid(row=0, column=0, columnspan=6, sticky=tk.NSEW)
        self.chat_history_scroll = tk.Scrollbar(parent, orient="vertical",
                                                command=self.chat_history.yview)
        self.chat_history_scroll.grid(row=0, column=6, sticky="ns")
        self.chat_history_frame = tk.Frame(self.chat_history, bg="red")
        self.chat_history_frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.chat_history.configure(
            scrollregion=self.chat_history_frame.bbox("all"))
        self.chat_history_frame_window = self.chat_history.create_window((0, 0),
                                                                         window=self.chat_history_frame, anchor="nw")
        self.chat_history.configure(
            yscrollcommand=self.chat_history_scroll.set)

        # Start the chat greeting the user

        self.chat_bubble("bot", "Hallo, ich bin Voicy! Wie ist dein Name?")

        while True:
            # try:
            self.userinput = interaction_queue.get()
            self.chat_bubble("user", self.userinput)
            self.usernlp = self.parse_request(self.userinput)

            self.chat_bubble("bot", self.usernlp)

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
        interaction_queue.put(self.writtencommand)

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

    def parse_request(self, userinput):
        usernlp = "Habe ich das richtig verstanden?\n"
        doc = nlp(userinput)
        for token in doc:
            usernlp += token.lemma_ + " "
        usernlp += "\n"
        for token in doc:
            usernlp += token.dep_ + " "
        for token in doc:
            match(token.dep_):
                case "ROOT":
                    match(token.lemma_):
                        case "test":
                            usernlp += "Dies war ein Test."
                        case "können":
                            usernlp += "Du kannst mich mal!"
                        case "kalender":
                            usernlp += "Kalender starten"
        return usernlp
