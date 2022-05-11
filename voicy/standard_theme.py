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
from tkinter import ttk


def standard_theme(parent):
    colors = {
        'fg': '#5c616c',
        'bg': '#f5f6f7',
        'disabledbg': '#fbfcfc',
        'disabledfg': '#a9acb2',
        'selectbg': '#5294e2',
        'selectfg': '#ffffff',
        'window': '#ffffff',
        'focuscolor': '#5c616c',
        'checklight': '#fbfcfc'
    }

    style = ttk.Style(parent)
    style.theme_create('standard-voicy', 'default')
    style.theme_use('standard-voicy')

    # Styles for the Widgets
    style.map('.', background=[('disabled', colors['disabledfg'])])

    style.configure('.',
                    background=colors['bg'],
                    foreground=colors['fg'],
                    troughcolor=colors['bg'],
                    selectbg=colors['selectbg'],
                    selectfg=colors['selectfg'],
                    fieldbg=colors['window'],
                    font=('TkDefaultFont',),
                    borderwidth=1,
                    focuscolor=colors['focuscolor']
                    )

    style.configure('TButton', padding=(8, 4, 8, 4), anchor='center')

    style.configure('TMenubutton', padding=(8, 4, 4, 4))

    style.configure('Toolbutton', anchor='center')

    style.map('TCheckbutton', background=[('active', colors['checklight'])])
    style.configure('TCheckbutton', padding=3)

    style.map('TRadiobutton', background=[('active', colors['checklight'])])
    style.configure('TRadiobutton', padding=3)

    style.configure('TNotebook', tabmargins=(0, 2, 0, 0))
    style.configure('TNotebook.Tab', padding=(6, 2, 6, 2), expand=(0, 0, 2))
    style.map('TNotebook.Tab', expand=[('selected', (1, 2, 4, 2))])

    style.configure('TSeparator', background=colors['bg'])

    style.configure('Treeview', background=colors['window'])
    style.configure('Treeview.Item', padding=(2, 0, 0, 0))
    style.map('Treeview',
              background=[('selected', colors['selectbg'])],
              foreground=[('selected', colors['selectfg'])])
    menu_theme = {"bg": colors['bg'],
                  "fg": colors['fg'],
                  "activebackground": colors['selectbg'],
                  "activeforeground": colors['selectfg'],
                  "activeborderwidth": 1,
                  "font": ('TkDefaultFont', )}
    print("läuft...")

    return style, colors, menu_theme
