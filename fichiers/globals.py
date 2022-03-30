# -*- coding: utf-8 -*-
#   Generateur de demi classe
#   version Alpha 1.0
#
#   ©  Copyright, Thomas Le Bonnec, all right reserved
#   31 march 2021
#   --------------------

from tkinter import *



def init():
    global classes, selectedClasse, selectedEleveID, colorMode, dataGate, version
    global blue, lightblue, lightbluebg, red, white, lightgray, gray, black, bg1, bg2
    global fCaption, fBody, fButton, fSubtitle, fTitle, fMainTitle
    classes = []
    selectedClasse = None
    selectedEleveID = None
    colorMode = "white"
    dataGate = [None, 0]    # [data, key]
    version = "1.0"

    # Light Colors
    blue = "#007aff"
    lightblue = "#bdd5ef"
    lightbluebg = "#e8f3ff"
    red = "#ff3b30"
    white = "#FFFFFF"
    lightgray = "#A0A0A7"
    gray = "#636366"
    black = "#000000"
    bg1 = "#F2F2F7"
    bg2 = "#e5e5ea"
    bg3 = "#d1d1d6"

    # Fonts
    fCaption = ("Helvetica", 11) #13
    fBody = ("Helvetica", 13) #15
    fButton = ("Helvetica", 13) #15
    fSubtitle = ("Helvetica", 17) #20
    fTitle = ("Helvetica", 22, "bold") #24
    fMainTitle = ("Helvetica", 26, "bold") #30