'''
Thomas Le Bonnec
@TBonnec
13 mars 2021
'''
from demi_groupes_objects import *
from random import *
from math import *


global groupeA, groupeB, matieres, classe
groupeA = []
groupeB = []
matieres = []
classe = []



def groupes(elements, groupesEleve):
    global groupeA, groupeB
    stage = 0

    best = (groupeA, groupeB, __test__(elements, groupesEleve))

    # Les méthodes suivantes sont effectués à la suite

    # Méthode 1
    for i in range(len(groupeA)):
        for j in range(stage, len(groupeB)):
            groupeA[j], groupeB[j] = groupeB[j], groupeA[j]
            test = __test__(elements, groupesEleve)
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
            test = __test__(elements, groupesEleve)
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
        newBest = (groupeA, groupeB, __test__(elements, groupesEleve))
        if newBest[-1] < best[-1]:
            best = newBest
        #else:
        #    groupeA[r1], groupeB[r2] = groupeB[r2], groupeA[r1]
        tour += 1
        if tour % 10000 == 0:
            print(tour)'''

    return best




# Teste si la combinaison actuelle rentre des les ecarts
def __test__(elements, groupesEleve):
    global groupeA, groupeB
    el1 = {}
    for e in elements:
        el1[e] = 0

    # Compte combien délèves sont par matière (elements) dans le groupe 1
    for eleve in groupeA:
        for matiereEleve in eleve.matieres:
            el1[matiereEleve] += 1

    meta = []
    for e in elements:
        el2 = e.nbEleve - el1[e]
        # Si nombre d'élève dans un groupe impair
        if e.nbEleve % 2 == 1 and abs(el1[e]-el2) == 1:
            meta.append((e, 0.0, el1[e], el2))
        # Si pair
        else:
            meta.append((e, max((abs(el1[e]-el2) * 100 / e.nbEleve) / 2 - e.margeDerreur, 0) * e.incidence, el1[e], el2))

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




def launch():
    global groupeA, groupeB, matieres, classe
    matieresDict = {}
    while True:
        nom = input("Nom de la matiere : ")
        nbEleve = int(input("Nombre d'eleves : "))
        matieresDict[nom] = Matiere(nom, nbEleve, 1, 0)
        matieres.append(matieresDict[nom])
        c = int(input("Autre matiere ? "))
        if c != 1:
            break
    print("\n\nEleves\n\n")
    while True:
        prenom = input("Prenom : ")
        matieresEleve = []
        print("Matieres de", prenom)
        while True:
            matiere = input("Nom de la matiere : ")
            matieresEleve.append(matieresDict[matiere])
            encore = int(input("Encore ? "))
            if encore != 1:
                break
        classe.append(Eleve(prenom, matieresEleve))
        c = int(input("Autre Eleve ? "))
        if c != 1:
            break
    
    for g in range(int(len(classe)/2)):
        groupeA.append(classe[g])
    for h in range(int(len(classe)/2), len(classe)):
        groupeB.append(classe[h])
        






groupesAmis = None

launch()

g = groupes(matieres, groupesAmis)


# Affichage console

print("\n\n\n\n")
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

print("\n", g[2][1], "\n\n")

