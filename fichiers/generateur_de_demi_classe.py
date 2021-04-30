# -*- coding: utf-8 -*-
#   Generateur de demi classe
#   version Alpha 1.0
#
#   ©  Copyright, Thomas Le Bonnec, all right reserved
#   31 march 2021
#   --------------------
try:
    from tkinter import * # Python 3
except ImportError:
    from Tkinter import * # Python 2

from gdcInterface import *

window = GenerateurDemiClassApp()
window.title("Générateur de Demi-Classe")
window.geometry("1080x920")
window.minsize(1080,920)
window.iconbitmap("gdcIcon.ico")
window.mainloop()