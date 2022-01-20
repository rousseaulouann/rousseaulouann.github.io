class Noeud:

    def __init__(self, v, g, d):
        self.gauche = g
        self.valeur = v
        self.droit = d

def initialiser_tableau_huffman(phrase):
    dico_occurrence = dict()
    for i in phrase():
        dico_occurrence['i'] += 1
    pass

def ordonner(tableau_arbre):
    return sorted(tableau_arbre, key = lambda x:x.valeur[1])

def créer_arbre_huffman(phrase):
    pass

def encoder(arbre, code= "", dictionnaire = {}):
    pass

def compresser(phrase):
    pass

def affiche(A):
    """ affiche un arbre sous une forme spéciale !"""
    if A is None: return
    print("[", end="")
    affiche(A.gauche)
    print(A.valeur[0], end="")
    affiche(A.droit)
    print("]", end="")
    
D = créer_arbre_huffman("code de morse")
affiche(D)
print(encoder(D))
print(compresser("code de morse"))