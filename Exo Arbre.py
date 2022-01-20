
class  Noeud2:
    def __init__(self, val, g, d):
        self.valeur = val
        self.gauche = g
        self.droite = d
        
def hauteur(a):
    if a == None:
        return 0
    return 1 + max(hauteur(a.droite), hauteur(a.gauche))

def taille(a):
    if a == None:
        return 0
    return 1 + taille(a.droite) + taille(a.gauche)

"""Exercice 4"""


def parfait(h):
    if h == 0 :
        return 
    A = Noeud2(h-1, parfait(h-1) , parfait(h-1))
    print(A.valeur)
       
print(parfait(4))   