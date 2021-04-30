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
import globals
globals.init()
from gdcMain import *
from gdcCSV import *
from uuid import *

from gdcHomeView import *
from gdcGroupeView import *
from gdcNewClasseView import *
from gdcClasseDetailView import *
from gdcMatiereSelectorView import *

import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)






class GenerateurDemiClassApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        menu = Menu(self)
        self.config(menu = menu)
        affichageMenu = Menu(menu)
        menu.add_cascade(label = "Affichage", menu = affichageMenu)
        affichageMenu.add_command(label = "Mode Clair", command = self.lightMode)
        affichageMenu.add_command(label = "Mode Sombre", command = self.darkMode)


        container = Frame(self)
        container.pack(side = "top", fill = "both", expand = YES)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for f in (HomeView, NewClasseView, ClasseDetailView, MatiereSelectorView, GroupeView):
            frameName = f.__name__
            self.frames[frameName] = f(parent = container, controller = self)
            frame = self.frames[frameName]
            frame.grid(row=0, column=0, sticky="nsew")

        self.showFrame("HomeView")

    def showFrame(self, name):
        frame = self.frames[name]
        frame.refresh()
        frame.tkraise()

    def lightMode(self):
        lines = readFile("classes", "settings.csv")
        headers = lines.pop(0)
        lines[0][0] = 1
        rightInBlankFile("classes", "settings.csv", headers, lines)
        retrieveSettings()

    def darkMode(self):
        lines = readFile("classes", "settings.csv")
        headers = lines.pop(0)
        lines[0][0] = 0
        rightInBlankFile("classes", "settings.csv", headers, lines)
        retrieveSettings()
