# -*- coding: utf-8 -*-
#   Generateur de demi classe
#   version Alpha 1.0
#
#   © Copyright, Thomas Le Bonnec, all right reserved
#   24 march 2021
#   --------------------

from uuid import *
from gdcCSV import *



class Classe:
    def __init__(self, id, nom, matieres, eleves):
        self.id = id                # uuid
        self.nom = nom              # str
        self.matieres = matieres    # [Matiere]
        self.eleves = eleves        # [Eleve]
        self.configurations = None  # [Configuration]
    
    def updateNom(self, nom):
        self.nom = nom
    
    def addMatiere(self, matiere):
        self.matieres.append(matiere)
        addInFile("classes/" + self.nom, self.nom + "_matieres.csv", [matiere.id, matiere.nom, matiere.nbEleves, matiere.margeDerreur], -1)
    
    def removeMatiere(self, matiere):
        i = self.matieres.index(matiere)
        self.matieres.pop(i)
        removeFromFile("classes/" + self.nom, self.nom + "_matieres.csv", matiere)
    
    def updateMatieres(self, matiere):
        for m in self.matieres:
            if m.id == matiere.id:
                i = self.matieres.index(m)
                self.matieres[i] = matiere
                updateInFile("classes/" + self.nom, self.nom + "_matieres.csv", matiere)
    
    def addEleve(self, eleve):
        self.eleves.append(eleve)
    
    def removeEleve(self, eleve):
        i = self.eleves.index(eleve)
        self.eleves.pop(i)
    
    def updateEleves(self, eleve):
        for e in self.eleves:
            if e.id == eleve.id:
                i = self.eleves.index(e)
                self.eleves[i] = eleve
    
    def addConfiguration(self, config):
        self.configurations.append(config)
    
    def removeConfiguration(self, config):
        i = self.configurations.index(config)
        self.configurations.pop(i)



class Configuration:
    def __init__(self, id, nom, groupeA, groupeB, repartition):
        self.id = id                    # uuid
        self.nom = nom                  # str
        self.groupeA = groupeA          # [uuid1], liste d'ids d'eleves
        self.groupeB = groupeB          # [uuid1], liste d'ids d'eleves
        self.repartition = repartition  # [[nomMatiere, repartition groupeA, repartition groupeB]]
    
    def updateNom(self, nom):
        self.nom = nom



class Matiere:
    def __init__(self, id, nom, nbEleves, margeDerreur):
        self.id = id                        # uuid
        self.nom = nom                      # str
        self.nbEleves = nbEleves            # int
        self.margeDerreur = margeDerreur    # int
    
    def updateNom(self, nom):
        self.nom = nom



class Eleve:
    def __init__(self, id, nom, idsMatieres):
        self.id = id                    # uuid
        self.nom = nom                  # str
        self.idsMatieres = idsMatieres  # [uuid1]
    
    def updateNom(self, nom):
        self.nom = nom
    
    def addMatiere(self, idMatiere):
        self.idsMatieres.append(idMatiere)
    
    def removeMatiere(self, matiere):
        i = self.matieres.index(matiere)
        self.matieres.pop(i)
    
    def updateMatieres(self, matiere):
        for m in self.matieres:
            if m.id == matiere.id:
                i = self.matieres.index(m)
                self.matieres[i] = matiere



