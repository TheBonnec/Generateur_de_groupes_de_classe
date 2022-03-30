# -*- coding: utf-8 -*-
#   Generateur de demi classe
#   version Alpha 1.0
#
#   ©  Copyright, Thomas Le Bonnec, all right reserved
#   31 march 2021
#   --------------------

from tkinter import *
from tkinter import messagebox
from gdcMain import *
from gdcCSV import *
from uuid import *
import globals





class NewClasseView(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg = globals.lightblue)
        self.controller = controller
        self.initView()


    def initView(self):
        mainFrame = Frame(self, bg = globals.lightblue)
        buttonsFrame = Frame(mainFrame, bg = globals.lightblue)

        # Titre
        title = Label(mainFrame, text = "Nouvelle Classe", font = globals.fMainTitle, bg = globals.lightblue, fg = globals.blue)
        title.pack()

        # Textfield
        self.textField = Entry(mainFrame, bd = 0, bg = globals.bg1, fg = globals.black, insertbackground = globals.black, font = globals.fBody)
        self.textField.pack(pady = 16, fill = X)

        # Buttons
        exitButton = Button(buttonsFrame, text = "Retour", font = globals.fButton, bg = globals.bg1, bd = 0, fg = globals.blue, width = 7,
            command = self.exit)
        exitButton.pack(side = LEFT, fill = X)

        addButton = Button(buttonsFrame, text = "Créer", font = globals.fButton, bg = globals.blue, bd = 0, fg = globals.white, width = 7,
            command = self.addClasse)
        addButton.pack(side = RIGHT)

        buttonsFrame.pack(expand = YES, fill = X, pady = 16)
        mainFrame.pack(expand = YES)



    def exit(self):
        self.controller.showFrame("HomeView")

    def addClasse(self):
        nom = self.textField.get()
        if nom != "":
            if saveNewClasse(nom, uuid1()) != False:
                retrieveAllClasses()
                self.exit()
            else:
                msgBox = messagebox.showerror("Impossible d'enregistrer votre nouvelle classe", "La classe " + str(nom) + " existe deja.")
        else:
            msgBox = messagebox.showerror("Impossible d'enregistrer votre nouvelle classe",
                "La zone de texte est vide.\n\nSi tel n'est pas le cas, redemarez l'app ou contactez : thomaslb.mc@icloud.com")
            print("ERROR : Impossible d'enregistrer une nouvelle classe")

    def refresh(self):
        #lenTextField = len(list(self.textField.get()))
        #self.textField.delete(0, lenTextField)
        for child in self.winfo_children():
            child.destroy()
        self.initView()
        self.config(bg = globals.lightblue)