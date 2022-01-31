class  Noeud:
    def __init__(self, val, g = None, d= None):
        self.valeur = val
        self.gauche = g
        self.droite = d
        
        
class ABR:
    
    def __init__(self ):
        self.racine = None
    
    def  ajouter (self, x): 
        self.racine =  ajoute(x, self.racine) # ajoute est une helper function
    
    def contient (self, x):
        return appartient( x, self.racine)
    
    def  __len__ (self):
        return taille(self.racine)
           
    def hauteur(self):
        return hauteuré(self.racine)
    
    def parcours_infixe(self, A):
        if A is None :
            return
        self.parcoursInfixe(A.gauche)
        print(A.valeur)
        self.parcoursInfixe(A.droite)
    
    def min (self):
        pass
    
    def max (self):
        pass
    

        
B = Noeud(55, Noeud(21, Noeud(10), Noeud(30, Noeud(22),Noeud(45))),Noeud(89, Noeud(60, Noeud(59),Noeud(67)),Noeud(121)))

def appartient(x, A):
    if A is None:
        return False
    if A.valeur == x:
        return True
    elif A.valeur > x:
        return appartient(x, A.gauche)
    elif A.valeur < x:
        return appartient(x, A.droite)

def ajoute (x, A):
    if A is None:
        return Noeud(x)
    if A.valeur > x:
        return Noeud(A.valeur, ajoute(x, A.gauche), A.droite)
    elif A.valeur <= x:
        return Noeud(A.valeur, A.gauche ,ajoute(x, A.droite))

def taille(a):
    if a == None:
        return 0
    return 1 + taille(a.droite) + taille(a.gauche)

def hauteuré(a):
    if a == None:
        return 0
    return 1 + max(hauteur(a.droite), hauteur(a.gauche))

a = ABR()
a.ajouter(3)
a.ajouter(1)
a.ajouter(2)


print(a.racine)
print(a.contient(2))
print(len(a))
print(a.parcours_infixe(a))