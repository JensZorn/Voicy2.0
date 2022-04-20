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
from queues import interaction_queue

if __name__ == "__main__":
    root = root_window()
    root.geometry("800x600+80+80")
    root.resizable(False, False)
    root.mainloop()
