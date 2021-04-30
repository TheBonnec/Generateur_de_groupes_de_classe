# -*- coding: utf-8 -*-
#   Generateur de demi classe
#   version Alpha 1.0
#
#   © Copyright, Thomas Le Bonnec, all right reserved
#   24 march 2021
#   --------------------

import csv
import os
import shutil
from uuid import *


''' ----- Fonctions Primaires ----- '''


def createFolder(path, name):
    dir_path = "{0:s}/{1:s}".format(path, name)
    try:
        os.mkdir(dir_path)
    except FileExistsError as err:
        print("Le dossier '" + name + "' ne peut pas etre cree car il existe déjà")
        return False



def rightInBlankFile(path, fileName, headers, content):
    file = open(path + "/" + fileName, "w")
    try:
        writer = csv.writer(file)
        writer.writerow(headers)
        for c in content:
            # TODO: Trouver une meilleur solution
            if content != [] and content != "" and content != " ":
                writer.writerow(c)
    finally:
        file.close()



def readFile(path, fileName):
    try:
        file = open(path + "/" + fileName, "r")
        reader = csv.reader(file)
        lines = []
        for row in reader:
            if row != [] and row != "" and row != " ":
                lines.append(row)
        file.close()
        return lines
    except:
        print("Impossible d'ouvrir le fichier " + fileName)
        return False





''' ----- Fonctions Composees ----- '''


def addInFile(path, fileName, content, index):
    lines = readFile(path, fileName)
    if lines != False:
        lines.insert(index + 1, content)
        headers = lines.pop(0)
        rightInBlankFile(path, fileName, headers, lines)




def removeFromFile(path, fileName, id):
    lines = readFile(path, fileName)
    if lines != False:
        for l in lines:
            if l[0] == str(id):
                lines.remove(l)
        headers = lines.pop(0)
        rightInBlankFile(path, fileName, headers, lines)




def updateInFile(path, fileName, element):
    lines = readFile(path, fileName)
    if lines != False:
        for l in range(len(lines)):
            if lines[l][0] == element[0]:
                lines[l] = element
        headers = lines.pop(0)
        rightInBlankFile(path, fileName, headers, lines)



def saveNewClasse(nom, classeID):
    try:
        if nom != "":
            n = createFolder("classes", nom)
            if n != False:
                addInFile("classes", "manifeste.csv", [classeID, nom], 1)
                rightInBlankFile("classes/" + nom,
                    nom + "_matieres" + ".csv",
                    ["id", "nom", "nbEleves", "margeDerreur"],
                    [])
                rightInBlankFile("classes/" + nom,
                    nom + "_eleves" + ".csv",
                    ["id", "nom", "idsMatieres"],
                    [])
                rightInBlankFile("classes/" + nom,
                    nom + "_configurations" + ".csv",
                    ["id", "nom", "groupeA", "groupeB"],
                    [])
                return True
        return False
    except:
        return False



def deleteClasse(nom, classeID):
    try:
        shutil.rmtree("classes/" + nom)
        removeFromFile("classes", "manifeste.csv", str(classeID))
    except:
        print("Cannot delete Classe : " + str(nom))




#saveNewClasse("TG09", uuid1())
#addInFile("classes/TG09", "TG09_matieres.csv", [uuid1(), "Philo", 14, 10], 1)
#addInFile("classes/TG09", "TG09_matieres.csv", [uuid1(), "Litterature Anglaise", 9, 10], 1)
#addInFile("classes/TG09", "TG09_matieres.csv", [uuid1(), "Litterature Espagnol", 12, 10], 1)
#addInFile("classes/TG09", "TG09_eleves.csv", [uuid1(), "Enzo", [UUID("712fd564-9256-11eb-b82a-8863dfcce78e"), UUID("573898ac-8fa9-11eb-8cb6-b88d1207ebd4")]], 3)
#addInFile("classes/TG09", "TG09_eleves.csv", [uuid1(), "Pierre", [UUID("573898ac-8fa9-11eb-8cb6-b88d1207ebd4"), UUID("61b6efae-8fa9-11eb-998c-b88d1207ebd4")]], 3)
