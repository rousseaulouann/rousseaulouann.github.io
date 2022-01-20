#class  Noeud:
#     def __init__(self, val):
#         self.valeur = val
#         self.gauche = None
#         self.droite = None
class File:
    def __init__(self):
        self.file = []
        
    def est_vide(self):
        return self.file == []
    
    def enfiler(self, val):
        self.file.append(val)
        
    def defiler (self):
        return self.file.pop(0)

class  Noeud2:
    def __init__(self, val, g, d):
        self.valeur = val
        self.gauche = g
        self.droite = d
        
    def parcoursInfixe(self,   A) :
        if A is None :
            return
        self.parcoursInfixe(A.gauche)
        print(A.valeur)
        self.parcoursInfixe(A.droite)
        
def parcoursL ( A):
    f = File()
    x = None
    f.enfiler(A)
    while not f.est_vide():
        x = f.defiler()
        print(x.valeur)
        if x.gauche != None :
            Ag = x.gauche
            f.enfiler(Ag)
        if x.droite != None:
            Ad = x.droite
            f.enfiler(Ad)
    return 
                
            
F = Noeud2("A", Noeud2("B", None, Noeud2("C", None, None)), Noeud2("D", None, None))
Z =  Noeud2("D", Noeud2("B", Noeud2("A", None, None), Noeud2("C", None, None)), Noeud2("F", Noeud2("E", None, None), Noeud2("G", Noeud2("I", None, None), Noeud2("H", None, None))))
Y = Noeud2("A", Noeud2("B", Noeud2("C", None, Noeud2("E", None, None)), Noeud2("D", None, None)),  \
           Noeud2("F", Noeud2("G", Noeud2("I", None, None), None), Noeud2("H", None, Noeud2("J", None, None))))

def hauteur(a):
    if a == None:
        return 0
    return 1 + max(hauteur(a.droite), hauteur(a.gauche))


def taille(a):
    if a == None:
        return 0
    return 1 + taille(a.droite) + taille(a.gauche)
    


parcoursL(Y)
print(taille(Z), hauteur(Z))    