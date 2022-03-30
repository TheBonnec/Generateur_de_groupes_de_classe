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






class HomeView(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg = globals.bg1)
        self.controller = controller
        self.initView()


    def initView(self):

        # Frame
        leftBlockFrame = Frame(self, bg = globals.bg2, bd = 0)
        classeButtonFrame = Frame(self, bg = globals.bg2, bd = 0)
        rightBlockFrame = Frame(self, bg = globals.bg1)
        titleFrame = Frame(rightBlockFrame, bg = globals.bg1)

        ''' Gauche '''

        # left Texte
        title = Label(leftBlockFrame, text = "Liste des classes", font = globals.fSubtitle, bg = globals.bg2, fg = globals.blue)
        title.place(x = '2.5m', y = '2.5m')

        # ScrollView
        self.listbox = Listbox(leftBlockFrame, activestyle = 'none', selectbackground = globals.lightblue, selectforeground = globals.blue, highlightthickness = 0, font = globals.fBody, bg = globals.bg2, bd = 0, fg = globals.gray)
        self.listbox.place(x = '3.6m', y = '11m', relheight = 1.0)
        for c in globals.classes:
            self.listbox.insert(END, c.nom)

        # GetInButton and DeleteButton
        getInButton = Button(classeButtonFrame, text = "Accéder à cette classe", font = globals.fButton, bd = 0, bg = globals.blue, fg = globals.white,
            command = self.switchToClasseDetailView)
        getInButton.place( anchor = SW, x = '2.5m', y = '-14m', width = '53m', height = '9m', rely = 1.0)

        getInButton = Button(classeButtonFrame, text = "Supprimer cette classe", font = globals.fButton, bd = 0, bg = globals.bg2, fg = globals.red,
            command = self.deleteClasse)
        getInButton.place( anchor = SW, x = '2.5m', y = '-2.5m', width = '53m', height = '9m', rely = 1.0)


        ''' Droite '''

        # Texte
        title = Label(titleFrame, text = "Générateur de demi-classe", font = globals.fMainTitle, bg = globals.bg1, fg = globals.blue)
        title.pack() # expand = YES, pour mettre au milieu     side = RIGHT, pour coller a droite

        # Button
        newClasseButton = Button(titleFrame, text = "Ajouter une classe", font = globals.fButton, bg = globals.blue, bd = 0, fg = globals.white,
            command = self.switchToNewClasseView)
        newClasseButton.pack(pady = 32)


        ''' Copyright and version (please do not edit these lines) '''
        version = Label(self, text = "Version " + globals.version, font = globals.fCaption, bg = globals.bg1, fg = globals.lightgray)
        version.place(anchor = SW, x = '60.5m', y = '-2.5m', rely = 1.0)

        copyrightText = Label(self, text = "© Copyright : Le Bonnec Thomas, 2021", font = globals.fCaption, bg = globals.bg1, fg = globals.lightgray)
        copyrightText.place(anchor = SE, x = '-2.5m', y = '-2.5m', relx = 1.0, rely = 1.0)


        classeButtonFrame.place(x = 0, y = 0, anchor = SW, width = '58m', height = '25.5m', rely = 1.0)
        leftBlockFrame.place(x = 0, y = 0, anchor = NW, width = '58m', relheight = 1.0) #width = 220
        titleFrame.pack(expand = YES)
        rightBlockFrame.place(x = 110, y = 0, anchor = N, relx = 0.5, relheight = 1.0)



    def deleteClasse(self):
        try:
            classeName = self.listbox.selection_get()
            msgBox = messagebox.askokcancel('Supprimer ' + classeName, 'Voulez-vous vraiment supprimer la classe ' + classeName + ' ?', icon = 'error')
            if msgBox == True:
                for c in globals.classes:
                    if c.nom == classeName:
                        classeID = c.id
                deleteClasse(classeName, classeID)
                self.refresh()
        except:
            msgBox = messagebox.showerror('Erreur', "Vous n'avez pas selectionné de classe à supprimer")


    def switchToClasseDetailView(self):
        if globals.classes != []:
            try:
                classeName = self.listbox.selection_get()
                for c in globals.classes:
                    if c.nom == classeName:
                        globals.selectedClasse = c.id
                self.controller.showFrame("ClasseDetailView")
            except:
                msgBox = messagebox.showerror("Erreur", "Pour acceder à une classe, vous devez d'abord en selectionner une dans le menu 'Liste des classes'")
                print("No Selection")
        else:
            print("classes = None")
            msgBox = messagebox.showerror("Erreur", "Vous devez d'abord créer une classe avant de pouvoir y acceder")


    def switchToNewClasseView(self):
        self.controller.showFrame("NewClasseView")


    def refresh(self):
        retrieveAllClasses()
        retrieveSettings()
        for child in self.winfo_children():
            child.destroy()
        self.initView()
        self.config(bg = globals.bg1)