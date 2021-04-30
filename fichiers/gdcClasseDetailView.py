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
from gdcObjects import *
from gdcCSV import *
from uuid import *
import globals





class ClasseDetailView(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg = globals.bg1)
        self.controller = controller

        self.elevesRow = []
        self.matieresRow = []
        self.classe = None
        self.skipRefreshWhenBack = False

        self.initView()


    def initView(self):

        if globals.selectedClasse != None and self.classe.eleves != None:

            menusFrame = Frame(self, bg = globals.bg1, bd = 0)
            leftBlockFrame = Frame(menusFrame, bg = globals.bg1, bd = 0)
            rightBlockFrame = Frame(menusFrame, bg = globals.bg1, bd = 0)


            # Main Title
            mainTitle = Label(self, text = str(self.classe.nom), font = globals.fMainTitle, bg = globals.bg1, fg = globals.blue)
            mainTitle.pack(fill = X, anchor = N, pady = 16)




            ''' Left Frame '''


            # Frames and ScrollBar
            leftBlockFrame = Frame(menusFrame, bg = globals.bg1, bd = 0)
            leftCanvaFrame = Frame(leftBlockFrame, bg = globals.bg1, bd = 0)
            leftcanvas = Canvas(leftCanvaFrame, bg = globals.bg1, bd = 0, highlightthickness = 0)
            leftscrollBar = Scrollbar(leftCanvaFrame, orient = "vertical", command = leftcanvas.yview, bd = 0, bg = globals.bg1, troughcolor = globals.bg1, highlightcolor = globals.bg1)
            leftInnerFrame = Frame(leftcanvas, bg = globals.lightbluebg, bd = 0)
            leftInnerFrame.bind("<Configure>", lambda e: leftcanvas.configure(scrollregion = leftcanvas.bbox("all")))
            leftcanvas.create_window((0,0), window = leftInnerFrame, anchor = NW)
            leftcanvas.configure(yscrollcommand = leftscrollBar.set)

            # Légende
            nameEText = Label(leftInnerFrame, text = "Nom", font = globals.fBody, bg = globals.lightbluebg, fg = globals.gray)
            matieresText = Label(leftInnerFrame, text = "Matieres", font = globals.fBody, bg = globals.lightbluebg, fg = globals.gray)
            nameEText.grid(row = 0, column = 1)
            matieresText.grid(row = 0, column = 2)

            self.elevesRow = []
            i = 1
            for e in self.classe.eleves:
                # Delete Button
                deleteButton = Button(leftInnerFrame, text = "X", font = globals.fButton, bg = globals.lightbluebg, bd = 0, fg = globals.red, width = 3,
                    command = lambda r = i - 1: self.removeEleve(r))
                deleteButton.grid(row = i, column = 0, padx = 4)

                # Eleve Name
                nameTextVar = StringVar()
                nameTextVar.set(e.nom)
                eleveName = Entry(leftInnerFrame, bd = 0, bg = globals.bg3, fg = globals.black, font = globals.fBody,
                    textvariable = nameTextVar, justify = CENTER, width = 16, insertbackground = globals.black)
                eleveName.grid(row = i, column = 1, padx = 4)

                # Eleve Matieres
                matieresEleve = ""
                for m in e.idsMatieres:
                    for cm in self.classe.matieres:
                        if cm.id == m:
                            matieresEleve += cm.nom + "\n"
                matieresEleve = matieresEleve[:-1]
                matieresText = Label(leftInnerFrame, text = matieresEleve, font = globals.fBody, bg = globals.lightbluebg, fg = globals.black, width = 16)
                matieresText.grid(row = i, column = 2, padx = 4, pady = 8)

                # Edit Matiere Button
                editMatiereButton = Button(leftInnerFrame, text = "Edit", font = globals.fButton, bg = globals.lightbluebg, bd = 0, fg = globals.blue, width = 5,
                    command = lambda r = i - 1: self.switchToMatiereSelectorView(r))
                editMatiereButton.grid(row = i, column = 3, padx = 4)

                i += 1
                self.elevesRow.append([e.id, nameTextVar, e.idsMatieres])


            # New Eleve Button
            newEleveButton = Button(leftBlockFrame, text = "Nouvel Elève", font = globals.fButton, bg = globals.blue, bd = 0, fg = globals.white, width = 15,
                command = self.newEleve)




            ''' Right Frame '''

            # Frames and ScrollBar
            rightInnerFrame = Frame(rightBlockFrame, bg = globals.bg1, bd = 0)
            rightCanvaFrame = Frame(rightBlockFrame, bg = globals.bg1, bd = 0)
            rightcanvas = Canvas(rightCanvaFrame, bg = globals.bg1, bd = 0, highlightthickness = 0)
            rightscrollBar = Scrollbar(rightCanvaFrame, orient = "vertical", command = rightcanvas.yview, bd = 0, bg = globals.bg1)
            rightInnerFrame = Frame(rightcanvas, bg = globals.lightbluebg, bd = 0)
            rightInnerFrame.bind("<Configure>", lambda e: rightcanvas.configure(scrollregion = rightcanvas.bbox("all")))
            rightcanvas.create_window((0,0), window = rightInnerFrame, anchor = NW)
            rightcanvas.configure(yscrollcommand = rightscrollBar.set)

            # Légende
            nameMText = Label(rightInnerFrame, text = "Nom", font = globals.fBody, bg = globals.lightbluebg, fg = globals.gray)
            nbElevesText = Label(rightInnerFrame, text = "Nombre d'élèves", font = globals.fBody, bg = globals.lightbluebg, fg = globals.gray)
            margederreurText = Label(rightInnerFrame, text = "Marge d'erreur", font = globals.fBody, bg = globals.lightbluebg, fg = globals.gray)
            nameMText.grid(row = 0, column = 1)
            nbElevesText.grid(row = 0, column = 2)
            margederreurText.grid(row = 0, column = 3)

            self.matieresRow = []
            i = 1
            for m in self.classe.matieres:
                # Delete Button
                deleteButton = Button(rightInnerFrame, text = "X", font = globals.fButton, bg = globals.lightbluebg, bd = 0, fg = globals.red, width = 3,
                    command = lambda r = i - 1: self.removeMatiere(r))
                deleteButton.grid(row = i, column = 0, padx = 4)

                # Matiere Name
                matiereNameTextVar = StringVar()
                matiereNameTextVar.set(m.nom)
                matiereName = Entry(rightInnerFrame, bd = 0, bg = globals.bg3, fg = globals.black, font = globals.fBody,
                    textvariable = matiereNameTextVar, justify = CENTER, width = 17, insertbackground = globals.black)
                matiereName.grid(row = i, column = 1, padx = 4, pady = 8)

                # Matiere nb Eleves
                matierenbElevesTextVar = StringVar()
                matierenbElevesTextVar.set(m.nbEleves)
                matierenbEleves = Entry(rightInnerFrame, bd = 0, bg = globals.bg3, fg = globals.black, font = globals.fBody,
                    textvariable = matierenbElevesTextVar, justify = CENTER, width = 3, insertbackground = globals.black)
                matierenbEleves.grid(row = i, column = 2, padx = 4)

                # Marge d'erreur
                margederreurTextVar = StringVar()
                margederreurTextVar.set(m.margeDerreur)
                margederreur = Entry(rightInnerFrame, bd = 0, bg = globals.bg3, fg = globals.black, font = globals.fBody,
                    textvariable = margederreurTextVar, justify = CENTER, width = 3, insertbackground = globals.black)
                margederreur.grid(row = i, column = 3, padx = 4)
                i += 1
                self.matieresRow.append([m.id, matiereNameTextVar, matierenbElevesTextVar, margederreurTextVar])

            # New Matiere Button
            newMatiereButton = Button(rightBlockFrame, text = "Nouvelle Matière", font = globals.fButton, bg = globals.blue, bd = 0, fg = globals.white, width = 15,
                command = self.newMatiere)



            leftBlockFrame.place(anchor = NW, x = 0, y = 0, relheight = 1.0, relwidth = 0.5)
            leftCanvaFrame.pack(side = TOP, fill = BOTH, expand = YES)
            leftcanvas.place(anchor = NW, x = '-57m', y = 0, relx = 0.5, relheight = 1.0, relwidth = 1.0)
            leftscrollBar.place(anchor = NE, x = 0, y = 0, relx = 1.0, relheight = 1.0)

            rightBlockFrame.place(anchor = NW, x = 0, y = 0, relx = 0.5, relheight = 1.0, relwidth = 0.5)
            rightCanvaFrame.pack(side = TOP, fill = BOTH, expand = YES)
            rightcanvas.place(anchor = NW, x = '-60m', y = 0, relx = 0.5, relheight = 1.0, relwidth = 1.0)
            rightscrollBar.place(anchor = NE, x = 0, y = 0, relx = 1.0, relheight = 1.0)

            menusFrame.pack(expand = YES, fill = BOTH, anchor = CENTER, pady = 16)

            newEleveButton.pack(anchor = CENTER, side = BOTTOM, pady = 16)
            newMatiereButton.pack(anchor = CENTER, pady = 16)



            ''' ----- Bottom Buttons ----- '''

            bottomColorFrame = Frame(self, bg = globals.bg2, bd = 0)
            bottomButtonsFrame = Frame(bottomColorFrame, bg = globals.bg2, bd = 0)
            # Save Button
            saveButton = Button(bottomButtonsFrame, text = "Enregistrer", font = globals.fButton, bg = globals.bg2, bd = 0, fg = globals.blue, width = 22,
                command = self.saveClasse)
            saveButton.pack(anchor = W, side = LEFT, fill = X, padx = 32, pady = 16)

            # ExitandSave Button
            exitNSaveButton = Button(bottomButtonsFrame, text = "Quitter et enregistrer", font = globals.fButton, bg = globals.bg1, bd = 0, fg = globals.blue, width = 22,
                command = self.saveAndQuit)
            exitNSaveButton.pack(anchor = W, side = LEFT, fill = X, padx = 32, pady = 16)

            # Home Button
            exitButton = Button(bottomButtonsFrame, text = "Quitter sans sauvegarder", font = globals.fButton, bg = globals.bg1, bd = 0, fg = globals.red, width = 22,
                command = self.exitWithoutSaving)
            exitButton.pack(anchor = W, side = LEFT, fill = X, padx = 32, pady = 16)

            # Groupe View Button
            groupeViewButton = Button(bottomButtonsFrame, text = "Générer des groupes", font = globals.fButton, bg = globals.blue, bd = 0, fg = globals.white, width = 22,
                command = self.switchToGroupeView)
            groupeViewButton.pack(anchor = E, side = LEFT, fill = X, padx = 32, pady = 16)

            bottomButtonsFrame.pack(side = BOTTOM)
            bottomColorFrame.pack(side = BOTTOM, fill = X)


        else:

            frame = Frame(self, bg = globals.bg1, bd = 0)

            errorText = Label(frame, text = "Une erreur est survenue.\nIl se peut que vous n'ayez pas selectionné de classe,\nou que la classe que vous cherchez à afficher rencontre un problème.\n\nSi le problème persiste : thomaslb.mc@icloud.com\n", font = globals.fBody, bg = globals.bg1, fg = globals.gray)
            errorText.grid(row = 0, column = 0, pady = 16)
            returnButton = Button(frame, text = "Retour", font = globals.fBody, bg = globals.bg2, bd = 0, fg = globals.blue, width = 7,
                command = self.exit)
            returnButton.grid(row = 1, column = 0)

            frame.pack(expand = YES)





    def switchToGroupeView(self):
        if len(self.elevesRow) > 1 and len(self.matieresRow) > 1:
            if self.saveClasse():
                self.controller.showFrame("GroupeView")
        else:
            msgBox = messagebox.showerror("Erreur", "Impossible de generer des groupes, car aucun eleve et/ou aucune matiere n'a ete saisie.")


    def switchToMatiereSelectorView(self, id):
        self.skipRefreshWhenBack = True
        self.partialSave()
        if self.elevesRow != [] and self.matieresRow != []:
            for e in self.classe.eleves:
                if e.id == self.elevesRow[id][0]:
                    globals.dataGate = [[self.classe, e], 77821]
                    self.controller.showFrame("MatiereSelectorView")
                    break
        else:
            msgBox = messagebox.showerror("Erreur", "Impossible d'acceder au menu des matieres, car aucun eleve et/ou aucune matiere n'a ete saisie.")


    def removeMatiere(self, id):
        if self.matieresRow != []:
            matiereID = self.matieresRow[id][0]
            for m in self.classe.matieres:
                print(type(m.id), type(matiereID))
                if m.id == matiereID:
                    print("Remove Matiere")
                    self.classe.matieres.remove(m)
                    #self.partialSave()
                    self.softRefresh()
                    break

    def newMatiere(self):
        newMatiere = Matiere(id = uuid1(), nom = "", nbEleves = 1, margeDerreur = 0)
        self.classe.matieres.append(newMatiere)
        self.classe.matieres.sort(key = lambda matiere: matiere.nom)
        self.partialSave()
        self.softRefresh()


    def removeEleve(self, id):
        if self.elevesRow != []:
            eleveID = self.elevesRow[id][0]
            for e in self.classe.eleves:
                if e.id == eleveID:
                    print("Remove Eleve")
                    self.classe.eleves.remove(e)
                    self.partialSave()
                    self.softRefresh()
                    break

    def newEleve(self):
        newEleve = Eleve(id = uuid1(), nom = "", idsMatieres = [])
        self.classe.eleves.append(newEleve)
        self.classe.eleves.sort(key = lambda eleve: eleve.nom)
        self.partialSave()
        self.softRefresh()

    def saveAndQuit(self):
        if self.saveClasse():
            self.exit()

    def saveClasse(self):
        rightInBlankFile("classes/" + self.classe.nom, self.classe.nom + "_eleves.csv", ["id", "nom", "idsMatieres"], [])
        for e in self.classe.eleves:
            addInFile("classes/" + self.classe.nom, self.classe.nom + "_eleves.csv", [e.id, e.nom, e.idsMatieres], 1)
        
        rightInBlankFile("classes/" + self.classe.nom, self.classe.nom + "_matieres.csv", ["id", "nom", "nbEleves", "margeDerreur"], [])
        for m in self.classe.matieres:
            addInFile("classes/" + self.classe.nom, self.classe.nom + "_matieres.csv", [m.id, m.nom, m.nbEleves, m.margeDerreur], 1)


        for e in self.elevesRow:
            try:
                nom = e[1].get()
                updateInFile("classes/" + self.classe.nom, self.classe.nom + "_eleves.csv", [str(e[0]), nom, e[2]])
            except:
                print("ERROR : Impossible d'obtenir le nom des eleves")
                msgBox = messagebox.showerror("Erreur", "Impossible de sauvegarder les élèves.\nVeuillez recommencer.")
                return False

        for m in self.matieresRow:
            try:
                nom = m[1].get()
                try:
                    nbEleve = int(m[2].get())
                    try:
                        marge = int(m[3].get())
                        if nbEleve == 0:
                            nbEleve = 1
                        updateInFile("classes/" + self.classe.nom, self.classe.nom + "_matieres.csv", [str(m[0]), nom, nbEleve, marge])
                    except:
                        print("ERROR : Only Numbers ! \nLocation : gdcClasseDetail.py / saveClasse()")
                        msgBox = messagebox.showerror("Erreur", "Veuillez ne rentrer uniquement des nombres dans les cases 'marge d'erreur'")
                        return False
                except:
                    print("ERROR : Only Numbers ! \nLocation : gdcClasseDetail.py / saveClasse()")
                    msgBox = messagebox.showerror("Erreur", "Veuillez ne rentrer uniquement des nombres dans les cases 'nombre d'eleves'")
                    return False
            except:
                print("ERROR : Impossible d'obtenir le nom des matieres")
                msgBox = messagebox.showerror("Erreur", "Impossible de sauvegarder les matières.\nVeuillez recommencer.")
                return False
        return True


    def partialSave(self):
        for e in self.classe.eleves:
            for er in self.elevesRow:
                if e.id == er[0]:
                    e.nom = er[1].get()
        for m in self.classe.matieres:
            for mr in self.matieresRow:
                if m.id == mr[0]:
                    m.nom = mr[1].get()
                    m.nbEleves = mr[2].get()
                    m.margeDerreur = mr[3].get()


    def refresh(self):
        if self.skipRefreshWhenBack == False:
            retrieveAllClasses()
            for c in globals.classes:
                if globals.selectedClasse == c.id:
                    self.classe = c
        self.softRefresh()
    
    def softRefresh(self):
        if globals.dataGate[1] == 47236:
            self.classe = globals.dataGate[0]
            globals.dataGate = [None, 0]
        for child in self.winfo_children():
            child.destroy()
        self.initView()
        self.config(bg = globals.bg1)
        self.skipRefreshWhenBack = False
    
    def exitWithoutSaving(self):
        msgBox = messagebox.askokcancel("Quittez sans sauvegarder", "Voulez-vous vraiement quitter sans sauvegarder. Tous les chagements non enregistrés seront perdus", icon = "error")
        if msgBox:
            self.exit()

    def exit(self):
        globals.selectedClasse = None
        self.controller.showFrame("HomeView")