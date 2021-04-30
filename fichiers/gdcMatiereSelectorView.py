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




class MatiereSelectorView(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg = globals.bg1)
        self.controller = controller
        self.classe = None
        self.eleve = None
        self.matieresRow = []



    def initView(self):
        if self.eleve != None and self.eleve.idsMatieres != None:

            buttonsFrame = Frame(self, bg = globals.bg1, bd = 0)

            canvas = Canvas(buttonsFrame, bg = globals.bg1, bd = 0, highlightthickness = 0)
            scrollBar = Scrollbar(buttonsFrame, orient = "vertical", command = canvas.yview, bd = 0, bg = globals.bg1, troughcolor = globals.bg1, highlightcolor = globals.bg1)
            innerFrame = Frame(canvas, bg = globals.bg1, bd = 0)
            innerFrame.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
            canvas.create_window((0,0), window = innerFrame, anchor = NW)
            canvas.configure(yscrollcommand = scrollBar.set)

            # Main Title
            mainTitle = Label(self, text = "Matières de : " + str(self.eleve.nom), font = globals.fMainTitle, bg = globals.bg1, fg = globals.blue)
            mainTitle.pack(fill = X, anchor = N, pady = 16)

            self.matieresRow = []
            for m in self.classe.matieres:
                # Matiere Check Button
                buttonIntVar = IntVar()
                for em in self.eleve.idsMatieres:
                    if m.id == em:
                        buttonIntVar.set(1)

                matiereCheckButton = Checkbutton(innerFrame, text = m.nom, font = globals.fSubtitle,
                    bg = globals.bg1, fg = globals.black, selectcolor = globals.lightblue, indicatoron = 0, variable = buttonIntVar, bd = 0, width = 24)
                matiereCheckButton.pack(anchor = CENTER, pady = 4)
                self.matieresRow.append([m.id, buttonIntVar])


            buttonsFrame.pack(side = TOP, fill = BOTH, expand = YES, pady = 16)
            canvas.place(anchor = NW, x = '-40m', y = 0, relx = 0.5, relheight = 1.0, relwidth = 1.0)
            scrollBar.place(anchor = NE, x = 0, y = 0, relx = 1.0, relheight = 1.0)
            #canvas.pack(anchor = CENTER, side = LEFT, expand = YES, fill = Y)
            #scrollBar.pack(side = LEFT, expand = YES, fill = Y)


            # Exit Button
            bottomColorFrame = Frame(self, bg = globals.bg2, bd = 0)
            exitButton = Button(bottomColorFrame, text = "Enregistrer", font = globals.fBody, bg = globals.blue, bd = 0, fg = globals.white, width = 20,
                command = self.saveAndExit)
            exitButton.pack(anchor = CENTER, pady = 16)
            bottomColorFrame.pack(side = BOTTOM, fill = X)



        else:
            frame = Frame(self, bg = globals.bg1, bd = 0)

            errorText = Label(frame, text = "Une erreur est survenue.\n\nSi le problème persiste : thomaslb.mc@icloud.com\n", font = globals.fBody, bg = globals.bg1, fg = globals.gray)
            errorText.grid(row = 0, column = 0, pady = 16)
            returnButton = Button(frame, text = "Retour", font = globals.fBody, bg = globals.bg2, bd = 0, fg = globals.blue, width = 7,
                command = self.exit)
            returnButton.grid(row = 1, column = 0)

            frame.pack(expand = YES)





    def refresh(self):
        if globals.dataGate[1] == 77821:
            self.classe = globals.dataGate[0][0]
            self.eleve = globals.dataGate[0][1]
            globals.dataGate = [None, 0]
        for c in globals.classes:
            if globals.selectedClasse == c.id:
                self.classe = c
        for e in self.classe.eleves:
            if globals.selectedEleveID == e.id:
                self.eleve = e
        for child in self.winfo_children():
            child.destroy()
        self.config(bg = globals.bg1)
        self.initView()


    def saveAndExit(self):
        self.softSave()
        self.exit()
    
    def softSave(self):
        if self.eleve != None:
            idsMatieres = []
            for i in self.matieresRow:
                if i[1].get() == 1:
                    idsMatieres.append(i[0])
            for e in self.classe.eleves:
                if e.id == self.eleve.id:
                    e.idsMatieres = idsMatieres
            globals.dataGate = [self.classe, 47236]

    '''def saveEleve(self):
        if self.eleve != None:
            idsMatieres = []
            for i in self.matieresRow:
                if i[1].get() == 1:
                    idsMatieres.append(i[0])
            e = self.eleve
            updateInFile("classes/" + self.classe.nom, self.classe.nom + "_eleves.csv", [str(e.id), e.nom, idsMatieres])
    '''

    def exit(self):
        globals.selectedEleveID = None
        self.controller.showFrame("ClasseDetailView")