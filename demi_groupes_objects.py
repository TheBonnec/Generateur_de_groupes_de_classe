'''
©Copyright 2021, Thomas Le Bonnec, All right reserved
16 mars 2021
'''


class Eleve:
    def __init__(self, prenom, matieres):
        self.prenom = prenom        # Str
        self.matieres = matieres    # Liste de type [Matiere]



class Matiere:
    def __init__(self, nom, nbEleve, incidence, margeDerreur):
        self.nom = nom                      # Str
        self.nbEleve = nbEleve              # Int
        self.incidence = incidence          # Int; mutliplicateur du pourcentage d'erreur ajoute a la config si la marge d'erreur est depassee
        self.margeDerreur = margeDerreur    # Int; pourcentage de difference maximum entre 2 groupes. Si depasse, incidence ajouter a marge d'erreur de la config



class GroupeAmis:
    def __init__(self, prenom1, prenom2, incidence):
        self.prenom1 = prenom1
        self.prenom2 = prenom2
        self.incidence = incidence




