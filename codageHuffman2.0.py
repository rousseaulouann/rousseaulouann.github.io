class Noeud:

    def __init__(self, v, g, d):
        self.gauche = g
        self.valeur = v
        self.droit = d

def initialiser_tableau_huffman(phrase):
    dico_occurrence = dict()
    for lettre in phrase:
        if lettre in dico_occurrence:
            dico_occurrence[lettre] += 1
        else:
            dico_occurrence[lettre] = 1
    tableau_arbre = [Noeud((clé, valeur), None, None) for clé, valeur in dico_occurrence.items()]
    return tableau_arbre

def ordonner(tableau_arbre):
#     for i in tableau_arbre:
#         print(i.valeur)
    return sorted(tableau_arbre, key = lambda x:x.valeur[1])

def créer_arbre_huffman(phrase):
    
    a=  initialiser_tableau_huffman(phrase)
    a_ordonner = ordonner(a)
    
    while len(a_ordonner) > 1:
        a_gauche = a_ordonner.pop(0)
        a_gauche_lettre = a_gauche.valeur[0]
        a_gauche_rep = a_gauche.valeur[1]
        
        a_droite = a_ordonner.pop(0)
        a_droite_lettre = a_droite.valeur[0]
        a_droite_rep = a_droite.valeur[1]
        
        concaténation = a_gauche_lettre + a_droite_lettre
        somme = a_gauche_rep + a_droite_rep
        
        a_ordonner.append (Noeud((concaténation, somme), a_gauche, a_droite))
        a_ordonner = ordonner(a_ordonner)
    return a_ordonner[0]

def encoder(arbre, code= "", dictionnaire = {}):
    if arbre is None:
        return
    encoder(arbre.gauche, code + "0", dictionnaire)
    if len(arbre.valeur[0]) == 1 :
        dictionnaire[arbre.valeur[0]] = code
    encoder(arbre.droit, code + "1", dictionnaire)
    return dictionnaire
    

def compresser(phrase):
    dico = encoder(créer_arbre_huffman(phrase))
    phrasebinaire = ""
    for i in phrase:
        phrasebinaire  += dico[i] 
    return phrasebinaire

def affiche(A):
    if A is None: return
    print("[", end="")
    affiche(A.gauche)
    print(A.valeur[0], end="")
    affiche(A.droit)
    print("]", end="")
#     
D = créer_arbre_huffman("code de morse")
print(D.valeur, D.gauche.valeur, D.droit.valeur)
affiche(D)

print(encoder(D))
print(compresser("code de morse"))
# 
# A = initialiser_tableau_huffman("code de morse")
# A_ordonner =ordonner(A )
# 
# for i in A_ordonner:
#         print(i.valeur)
        
#print(initialiser_tableau_huffman("code de morse"))
