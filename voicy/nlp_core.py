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
import spacy
from queues import to_nlp, from_nlp
from threading import enumerate
nlp = spacy.load("de_core_news_lg")


class nlp_core():
    def __init__(self):
        usernlp = "Hallo, ich bin Voicy! Wie kann ich dir helfen?"
        from_nlp.put(usernlp)
        while True:
            # try:
            userinput = to_nlp.get()
            print("Got input")
            self.active_threads = enumerate()
            print(self.active_threads)
            usernlp = self.parse_request(userinput)
            from_nlp.put(usernlp)

    def parse_request(self, userinput):
        usernlp = "Habe ich das richtig verstanden?\n"
        doc = nlp(userinput)
        for token in doc:
            usernlp += token.lemma_ + " "
        usernlp += "\n"
        for token in doc:
            usernlp += token.dep_ + " "

        return usernlp
