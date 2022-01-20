def pile():
    """ crée de la pile vide """ 
    return []

def est_vide(p):
    """renvoie True si la pile est vide
     et False sinon"""
    return p == []

def empiler(p, x):
    """Ajoute l’élément x à la pile p"""
    p.append(x)

def depiler(p):
    """dépile et renvoie l’élément au sommet de la pile p""" 
    assert not est_vide(p), """Pile vide"""
    return p.pop()

def taille(p):
    i = 0
    while not est_vide(p):
        i += 1
        depiler(p)
    return i
    
def sommet(p):
    a = depiler(p)
    empiler (p, a)
    return a

class Pile:
    """ classe Pile : 
    création d’une instance Pile avec à partir d'une liste """
    def __init__(self):
        "Initialisation d’une pile vide"
        self.pile = []

    def est_vide(self):
        """teste si la pile est vide""" 
        return self.pile == []

    def depiler(self): 
        """dépile si la pile n'est pas vide"""
        assert not self.est_vide(), 'Pile vide'
        return self.pile.pop()

    def empiler(self,x): 
        """empile"""
        self.pile.append(x)
        
    def __len__(self):
        i = 0
        while not est_vide(self.pile):
            i += 1
            depiler(self.pile)
        return i
    
    def sommet(self):
        a = self.depiler()
        self.empiler(a)
        return a
    
def vérifier_parenthésage(expr : str) -> bool:
    j = Pile()
    for i in expr:
    
        if i  == "(" :
            j.empiler(i)
        if i  == ")" and not j.est_vide():
            j.depiler()
        elif i  == ")" and j.est_vide(): 
            return False
    if j.est_vide():
        return True
    else: return False


def vérifier_parenthésage_crochets(expr : str) -> bool:
    j = Pile()
    for i in expr:
        
        if i  == "["  or i == '(':
            j.empiler(i)
    
        if i  == "]" and not j.est_vide():
            if last_out == '(':
                return False
            j.depiler()
        elif i  == ")" and not j.est_vide():
            if last_out == '[':
                return False
            j.depiler()
        elif i  == "]" or i == ')' and j.est_vide(): 
            return False
        
        if not j.est_vide(): last_out= j.sommet()
        
    if j.est_vide():
        return True
    else: return False
            

print(vérifier_parenthésage_crochets('[x+1])(x_1)]'))
def evaluer_npi(expr : str) -> float:
    """
    npi = notation_polonaise_inversée
    (2 + 3) * 4 + 1    ----> 2 3 + 4 * 1 +
    
    (2 + 3) * (4 + 1)  <---- 2 3 + 4 1 + * 
    2 3 + 4 1 + *
    pile : 2                |
    pile : 2 3              |
    pile : 5                | op = + : 2+3 = 5
    pile : 5 4              | 
    pile : 5 4 1            | 
    pile : 5 5              | op = + : 4+1 = 5
    pile : 25               | op = * : 5*5 = 25
    renvoie le résultat : 25
    
    Il faut utiliser l'instruction **eval** : eval("3+3") donne 6 ou eval("abs(-7) + 3**2") donne 16
    """
    j= Pile()
    
    for op in expr:
        
        if  op in ['+', '-', '/', '*'] :
            b = j.depiler()
            a = j.depiler()
            j.empiler(str(eval(a + op + b)))
            
        elif op != " ":
            j.empiler(op)
            
    return j.pile
    
    
pile =Pile()

for i in range(5):
    pile.empiler(2*i)
    print(pile.pile)
    
#print(len(pile))
print(pile.sommet())
print(evaluer_npi("3 4  2 * +"))
