# -*- coding: utf-8 -*-
#   Generateur de demi classe
#   version Alpha 1.0
#
#   ©  Copyright, Thomas Le Bonnec, all right reserved
#   31 march 2021
#   --------------------

from tkinter import *
from gdcMain import *
from gdcCSV import *
from uuid import *
import globals
import gdcAlgo


class GroupeView(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg = globals.lightbluebg)
        self.controller = controller
        self.classe = None
        self.algoResult = None

        self.initView()
    




    def initView(self):
        if self.classe != None and self.algoResult != None:

            # Frames
            menusFrame = Frame(self, bg = globals.bg1, bd = 0)
            leftBlockFrame = Frame(menusFrame, bg = globals.bg1, bd = 0)
            rightBlockFrame = Frame(menusFrame, bg = globals.bg1, bd = 0)



            # Main Title
            mainTitle = Label(self, text = "Groupes de : " + self.classe.nom, font = globals.fMainTitle, bg = globals.lightbluebg, fg = globals.blue)
            mainTitle.pack(fill = X, anchor = N, pady = 16)
            


            ''' Left Frame '''


            # Frames and ScrollBar
            leftBlockFrame = Frame(menusFrame, bg = globals.lightbluebg, bd = 0)
            leftCanvaFrame = Frame(leftBlockFrame, bg = globals.lightbluebg, bd = 0)
            leftcanvas = Canvas(leftCanvaFrame, bg = globals.lightbluebg, bd = 0, highlightthickness = 0)
            leftscrollBar = Scrollbar(leftCanvaFrame, orient = "vertical", command = leftcanvas.yview, bd = 0, bg = globals.lightbluebg)
            leftInnerFrame = Frame(leftcanvas, bg = globals.lightbluebg, bd = 0)
            leftInnerFrame.bind("<Configure>", lambda e: leftcanvas.configure(scrollregion = leftcanvas.bbox("all")))
            leftcanvas.create_window((0,0), window = leftInnerFrame, anchor = NW)
            leftcanvas.configure(yscrollcommand = leftscrollBar.set)

            # Légende
            nameEText = Label(leftInnerFrame, text = "Groupe A", font = globals.fBody, bg = globals.lightbluebg, fg = globals.gray)
            matieresText = Label(leftInnerFrame, text = "Groupe B", font = globals.fBody, bg = globals.lightbluebg, fg = globals.gray)
            nameEText.grid(row = 0, column = 0)
            matieresText.grid(row = 0, column = 1)

            # Eleves List
            i = 1
            for a in self.algoResult.groupeA:
                eleveName = Label(leftInnerFrame, text = str(a.nom), font = globals.fBody, fg = globals.black, bg = globals.lightbluebg)
                eleveName.grid(row = i, column = 0)
                i += 1
            i = 1
            for b in self.algoResult.groupeB:
                eleveName = Label(leftInnerFrame, text = str(b.nom), font = globals.fBody, fg = globals.black, bg = globals.lightbluebg)
                eleveName.grid(row = i, column = 1)
                i += 1




            ''' Right Frame '''

            # Frames and ScrollBar
            rightInnerFrame = Frame(rightBlockFrame, bg = globals.lightbluebg, bd = 0)
            rightCanvaFrame = Frame(rightBlockFrame, bg = globals.lightbluebg, bd = 0)
            rightcanvas = Canvas(rightCanvaFrame, bg = globals.lightbluebg, bd = 0, highlightthickness = 0)
            rightscrollBar = Scrollbar(rightCanvaFrame, orient = "vertical", command = rightcanvas.yview, bd = 0, bg = globals.lightbluebg)
            rightInnerFrame = Frame(rightcanvas, bg = globals.lightbluebg, bd = 0)
            rightInnerFrame.bind("<Configure>", lambda e: rightcanvas.configure(scrollregion = rightcanvas.bbox("all")))
            rightcanvas.create_window((0,0), window = rightInnerFrame, anchor = NW)
            rightcanvas.configure(yscrollcommand = rightscrollBar.set)

            # Légende
            nameMText = Label(rightInnerFrame, text = "Matière", font = globals.fBody, bg = globals.lightbluebg, fg = globals.gray)
            nbElevesText = Label(rightInnerFrame, text = "Nombre\nd'élèves\nGroupe A", font = globals.fBody, bg = globals.lightbluebg, fg = globals.gray)
            margederreurText = Label(rightInnerFrame, text = "Nombre\nd'élèves\nGroupe B", font = globals.fBody, bg = globals.lightbluebg, fg = globals.gray)
            nameMText.grid(row = 0, column = 0)
            nbElevesText.grid(row = 0, column = 1)
            margederreurText.grid(row = 0, column = 2)

            self.matieresRow = []
            i = 1
            for r in self.algoResult.repartition[0]:
                matiereNameText = Label(rightInnerFrame, text = r[0].nom, font = globals.fBody, bg = globals.lightbluebg, fg = globals.black)
                matiereNameText.grid(row = i, column = 0)

                groupeAText = Label(rightInnerFrame, text = r[2], font = globals.fBody, bg = globals.lightbluebg, fg = globals.black)
                groupeAText.grid(row = i, column = 1)

                groupeBText = Label(rightInnerFrame, text = r[3], font = globals.fBody, bg = globals.lightbluebg, fg = globals.black)
                groupeBText.grid(row = i, column = 2)
                i += 1
            


            leftBlockFrame.place(anchor = NW, x = 0, y = 0, relheight = 1.0, relwidth = 0.5)
            leftCanvaFrame.pack(side = TOP, fill = BOTH, expand = YES)
            leftcanvas.place(anchor = NW, x = '-45m', y = 0, relx = 0.5, relheight = 1.0, relwidth = 1.0)
            leftscrollBar.place(anchor = NE, x = 0, y = 0, relx = 1.0, relheight = 1.0)

            rightBlockFrame.place(anchor = NE, x = 0, y = 0, relx = 1.0, relheight = 1.0, relwidth = 0.5)
            rightCanvaFrame.pack(side = TOP, fill = BOTH, expand = YES)
            rightcanvas.place(anchor = NW, x = '-37m', y = 0, relx = 0.5, relheight = 1.0, relwidth = 1.0)
            rightscrollBar.place(anchor = NE, x = 0, y = 0, relx = 1.0, relheight = 1.0)

            menusFrame.pack(expand = YES, fill = BOTH, anchor = CENTER, pady = 16)



            ''' Bottom '''

            # Pourcentage Text
            pourcentageText = Label(self, text = "Pourcentage d'erreur : " + str(self.algoResult.repartition[1]) + "%", font = globals.fSubtitle, bg = globals.lightbluebg, fg = globals.black)
            pourcentageText.pack(pady = 8)

            # Back Button
            bottomColorFrame = Frame(self, bg = globals.bg1, bd = 0)
            backButton = Button(bottomColorFrame, text = "Retour", font = globals.fButton, bg = globals.blue, bd = 0, fg = globals.white, width = 20,
                command = self.exit)
            backButton.pack(anchor = S, side = BOTTOM, pady = 16)
            bottomColorFrame.pack(side = BOTTOM, fill = X)
    



    
    def refresh(self):
        retrieveAllClasses()
        for child in self.winfo_children():
            child.destroy()
        for c in globals.classes:
            if c.id == globals.selectedClasse:
                self.classe = c
        self.algoResult = gdcAlgo.groupes(self.classe)
        self.initView()
        self.config(bg = globals.lightbluebg)
    

    def exit(self):
        self.controller.showFrame("ClasseDetailView")