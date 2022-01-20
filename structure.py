class ListeC:
    def __init__(self):
        self.tete = None

    def est_vide(self):
        return self.tete is None
    
    def __len__(self):
        if self.est_vide():
            return 0
        
        compteur = 1
        maillon = self.tete
        
        while  maillon.suivant != None:
            maillon = maillon.suivant
            compteur += 1
            
        return compteur        
    
 
    def get_dernier_maillon(self):
        maillon = self.tete
        while maillon.suivant != None:
            maillon = maillon.suivant
        return maillon

    
    def __getitem__(self, i):
        if len(self) >= i:
            maillon1 = self.tete
            for _ in range (i):
                maillon1 = maillon1.suivant
            return maillon1            
    
    def __str__(self):
        liste = ' L ->'
        i = 1
        maillon = self.tete
        
        while  maillon != None:
            liste += f"[M{i} |{ maillon.valeur}] -> "
            i += 1
            maillon = maillon.suivant
        liste += "None"
        return liste
        
    def __appendleft__ (self, nM):
        
        nM.suivant =  self.tete
        self.tete  = nM
    
    def __appendright__(self, nM):
        mdernier = ListeC.get_dernier_maillon(L) 
        mdernier.suivant = nM
    
    def __appendnext__(self, M, nM):
        maillon = self.tete
        while maillon.suivant != M:
            maillon = maillon.suivant
        nM.suivant = M.suivant
        M.suivant = nM
    
    def __popleft__ (self):
        self.tete = self.tete.suivant
        
    def __pop__(self):
        maillon = self.tete
        mdernier = ListeC.get_dernier_maillon(L) 
        while maillon.suivant != mdernier :
            maillon = maillon.suivant
        maillon.suivant = None
        
    def __popnext__(self, M):
        maillon = self.tete
        while maillon.suivant != M :
            maillon = maillon.suivant
        maillon.suivant = M.suivant
        
        
    
    
class Maillon() :
    def __init__(self):
        self.valeur =None
        self.suivant = None
        
if __name__ == "__main__":
    
    L= ListeC()
    M1, M2, M3, M4, M5, M6, M7= Maillon(), Maillon(), Maillon(), Maillon(), Maillon(),Maillon() , Maillon()
    M1.valeur = " Magicien mais seulement dans le sous-sol de sa maman"
    M2.valeur = " Gazelle des fonds marins "
    M3.valeur = " Rocher carnivore"
    M4.valeur = "Girafe ailée des lacs "
    M5.valeur = "Anis etoilé sauvage"
    M6.valeur = "Chaîne de télévision française"
    M7.valeur = " Nébuleuse de poisson sur son lit d'asperges"

    L.tete = M1
    M1.suivant = M2
    M2.suivant = M3
    M3.suivant = M4


#     ListeC. __appendright__(L,M5)
#     ListeC. __appendright__(L,M6)
#     ListeC. __appendright__(L,M7)
#     ListeC.__popnext__(L, M3)  
    
    print(L)

  
