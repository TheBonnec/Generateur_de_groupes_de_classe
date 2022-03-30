# -*- coding: utf-8 -*-
#   Generateur de demi classe
#   version Alpha 1.0
#
#   ©  Copyright, Thomas Le Bonnec, all right reserved
#   31 march 2021
#   --------------------

from gdcObjects import *
from random import *
from uuid import *
from math import *
import globals



def groupes(classe):
    if len(classe.eleves) % 2 != 0:
        classe.eleves.append(Eleve(uuid1(), "Au59k-47JeN-2Hwn6-P0oi3", []))     # Ajout d'un "eleve vide" pour le nombre d'élève soit pair

    matieres = classe.matieres
    eleveLen = int(round(len(classe.eleves) / 2, 0))
    groupeA = classe.eleves[:eleveLen]
    groupeB = classe.eleves[eleveLen:]
    groupesEleve = None # Groupes d'amis

    stage = 0
    
    best = (groupeA, groupeB, testConfig(groupeA, groupeB, matieres, groupesEleve))

    # Les méthodes suivantes sont effectuées à la suite

    # Méthode 1
    for i in range(len(groupeA)):
        for j in range(stage, len(groupeB)):
            groupeA[j], groupeB[j] = groupeB[j], groupeA[j]
            test = testConfig(groupeA, groupeB, matieres, groupesEleve)
            if test[-1] < best[-1][-1]:
                best = (deepCopy(groupeA), deepCopy(groupeB), test)
            else:
                groupeA[j], groupeB[j] = groupeB[j], groupeA[j]
        groupeA[stage], groupeB[stage] = groupeB[stage], groupeA[stage]
        stage += 1

    # Méthode 2
    for i in range(len(groupeA)):
        for j in range(len(groupeB)):
            groupeA[i], groupeB[j] = groupeB[j], groupeA[i]
            test = testConfig(groupeA, groupeB, matieres, groupesEleve)
            if test[-1] < best[-1][-1]:
                best = (deepCopy(groupeA), deepCopy(groupeB), test)

    # Méthode 3 (méthode aléatoire)
    # Cette méthode ne permet rien de plus que la combinaison des 2 méthodes précédentes (au vu de ce qui a été testé)
    '''tour = 0
    for i in range(400000):
        ran = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        g1, g2 = [], []
        for i in range(30):
            r = ran[randint(0,len(ran)-1)]
            if r == 0:
                g1.append(classe[i])
            else:
                g2.append(classe[i])
        newBest = (groupeA, groupeB, test(groupeA, groupeB, matieres, groupesEleve))
        if newBest[-1] < best[-1]:
            best = newBest
        #else:
        #    groupeA[r1], groupeB[r2] = groupeB[r2], groupeA[r1]
        tour += 1
        if tour % 10000 == 0:
            print(tour)'''


    # Suppression de "l'eleve vide" s'il à été ajouté au début pour equilibrer
    for e in best[0]:
        if e.nom == "Au59k-47JeN-2Hwn6-P0oi3":
            best[0].remove(e)
    for e in best[1]:
        if e.nom == "Au59k-47JeN-2Hwn6-P0oi3":
            best[1].remove(e)
    
    best[0].sort(key = lambda eleve: eleve.nom)
    best[1].sort(key = lambda eleve: eleve.nom)

    return Configuration(uuid1(), classe.nom, best[0], best[1], [best[2][0], best[2][1]])




# Teste si la combinaison actuelle rentre des les ecarts
def testConfig(groupeA, groupeB, matieres, groupesEleve):
    el1 = {}
    for m in matieres:
        el1[m.id] = 0

    # Compte combien délèves sont par matière (matieres) dans le groupe 1
    for eleve in groupeA:
        for matiereEleve in eleve.idsMatieres:
            el1[matiereEleve] += 1

    meta = []
    for m in matieres:
        el2 = m.nbEleves - el1[m.id]
        # Si nombre d'élève dans un groupe impair
        if m.nbEleves % 2 == 1 and abs(el1[m.id]-el2) == 1:
            meta.append((m, 0.0, el1[m.id], el2))
        # Si pair
        else:
            pourcentageErreur = m.margeDerreur * 100 / m.nbEleves       # Passer d'un nombre d'élève d'erreur à un pourcentage
            meta.append((m, max((abs(el1[m.id]-el2) * 100 / m.nbEleves) / 2 - pourcentageErreur, 0), el1[m.id], el2))
            # AVEC INCIDENCE:
            #meta.append((m, max((abs(el1[m.id]-el2) * 100 / m.nbEleves) / 2 - pourcentageErreur, 0) * m.incidence, el1[m.id], el2))

    if groupesEleve != None:
        ge = __testGroupesDeleves__(groupesEleve)
        for i in ge:
            meta.append(i)

    tot = 0
    for m in meta:
        tot += m[1]
    tot = tot / len(meta)
    return [meta, tot]





def __testGroupesDeleves__(groupesAmis):
    global groupeA, groupeB
    meta = []
    for duo in groupesAmis:
        elevesTrouves = [0,0]
        for eleveA in groupeA:
            if eleveA.prenom == duo.prenom1 or eleveA.prenom == duo.prenom2:
                elevesTrouves[0] += 1
        if elevesTrouves[0] < 2:
            for eleveB in groupeB:
                if eleveB.prenom == duo.prenom1 or eleveB.prenom == duo.prenom2:
                    elevesTrouves[1] += 1
            if elevesTrouves[0] + elevesTrouves[1] <= 1:
                print("Des élèves inscrits dans la liste des groupes sont manquants dans celle des élèves ! Reverifier.", duo.prenom1, duo.prenom2)
            elif elevesTrouves[1] >= 2:
                meta.append(((duo.prenom1, duo.prenom2), 0))
            else:
                meta.append(((duo.prenom1, duo.prenom2), duo.incidence))
        else:
            meta.append(((duo.prenom1, duo.prenom2), 0))

    return meta



# Copie un liste
# Resoud le probleme PB01
def deepCopy(liste):
    r = []
    for l in liste:
        r.append(l)
    return r






# Affichage console

'''print("\n\n\n\n")
for i in g[0]:
    p = i.prenom + "\t\t"
    for k in i.matieres:
        p += k.nom + "\t\t"
    print(p)
print("\n")

for i in g[1]:
    p = i.prenom + "\t\t"
    for k in i.matieres:
        p += k.nom + "\t\t"
    print(p)
print("\n")

for i in g[2][0]:
    if type(i[0]) == Matiere:
        print(i[0].nom, i[1], i[2], i[3])
    else:
        print(i)

print("\n", g[2][1], "\n\n")'''

