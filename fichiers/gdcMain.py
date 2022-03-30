# -*- coding: utf-8 -*-
#   Generateur de demi classe
#   version Alpha 1.0
#
#   © Copyright, Thomas Le Bonnec, all right reserved
#   24 march 2021
#   --------------------

from gdcObjects import *
from gdcCSV import *
from tkinter import *
from uuid import *
import globals




''' ----- Recuperation des donnees ----- '''

def retrieveAllClasses():
    lines = readFile("classes", "manifeste.csv")
    if lines != False:
        globals.classes.clear()
        for i in range(1, len(lines)):
            if lines[i] != []:
                rc = retrieveClasse(lines[i][0], lines[i][1])
                if type(rc) != type(None):
                    globals.classes.append(rc)
        globals.classes.sort(key = lambda classe: classe.nom)
    #return True



def retrieveClasse(classeID, classeName):
    try:
        lines = readFile("classes/" + classeName, classeName + "_matieres.csv")
        matieres = []
        for i in range(1, len(lines)):
            try:
                lines[i][2] = int(lines[i][2])
            except:
                lines[i][2] = 1
            try:
                lines[i][3] = int(lines[i][3])
            except:
                lines[i][3] = 0
            matieres.append(Matiere(lines[i][0], lines[i][1], int(lines[i][2]), int(lines[i][3])))
        matieres.sort(key = lambda matiere: matiere.nom)
        lines = readFile("classes/" + classeName, classeName + "_eleves.csv")
        eleves = []
        for i in range(1, len(lines)):
            matieresEleve = str(lines[i][2])
            matieresEleve = matieresEleve.replace("[", "")
            matieresEleve = matieresEleve.replace("]", "")
            matieresEleve = matieresEleve.replace("'", "")
            matieresEleve = matieresEleve.replace("UUID(", "")
            matieresEleve = matieresEleve.replace(")", "")
            matieresEleve = matieresEleve.split(", ")
            eleves.append(Eleve(UUID(lines[i][0]), str(lines[i][1]), matieresEleve))
        eleves.sort(key = lambda eleve: eleve.nom)
        return Classe(classeID, classeName, matieres, eleves)
    except:
        print("Erreur. Impossible de charger la classe ayant pour id " + str(classeID))
        return None



def retrieveSettings():
    try:
        lines = readFile("classes", "settings.csv")
        lines.pop(0)
        settings = lines[0]
        if settings[0] == '0':
            globals.blue = "#0a84ff"
            globals.lightblue = "#3a4754"
            globals.lightbluebg = "#222930"
            globals.red = "#ff3b30"
            globals.white = "#FFFFFF"
            globals.lightgray = "#505054"
            globals.gray = "#aeaeb2"
            globals.black = "#FFFFFF"
            #globals.bg1 = "#1c1c1e"
            globals.bg1 = "#1c1c1e"
            globals.bg2 = "#2c2c2e"
            globals.bg3 = "#3a3a3c"
            globals.colorMode = "dark"
        else:
            globals.blue = "#007aff"
            globals.lightblue = "#bdd5ef"
            globals.lightbluebg = "#e8f3ff"
            globals.red = "#ff3b30"
            globals.white = "#FFFFFF"
            globals.lightgray = "#A0A0A7"
            globals.gray = "#636366"
            globals.black = "#000000"
            #globals.bg1 = "#F2F2F7"
            globals.bg1 = "#FFFFFF"
            globals.bg2 = "#e5e5ea"
            globals.bg3 = "#e5e5ea"
            globals.colorMode = "white"
    except:
        print("ERROR : Cannot load settings from the file settings.csv")





retrieveAllClasses()
retrieveSettings()

