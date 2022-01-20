class File:
    def __init__(self):
        self.file = []
        
    def est_vide(self):
        return self.file == []

    def enfiler(self, val):
        self.file.append(val)

    def defiler(self):
        return self.file.pop(0)


f_1 = File()
f_1.file = [0,1,1,0,1]
f_2 = File()
f_2.file = [0,2,2,2,0,2,0]


def croisement(f1, f2):
    f3 = File()
    top1= f1.defiler()
    f1.enfiler(top1)
    top2= f2.defiler()
    f2.enfiler(top2)
    
    while not f1.est_vide() or not f2.est_vide() :
        
        if f1.est_vide() :
            f3.enfiler(top2)
            top2 = f2.defiler()
                        
        elif f2.est_vide() :
            f3.enfiler(top1)
            top1 = f1.defiler()
                             
        elif top1 == 0:
            f3.enfiler(top2)
            top2 = f2.defiler()
            top1 = f1.defiler()
        
        elif top2 == 0 and top1 != 0:
            f3.enfiler(top1)
            top2 = f2.defiler()
            top1 = f1.defiler()
            
        else :
            f3.enfiler(top1)
            top1 = f1.defiler()
                    
    return f3.file

print(croisement(f_1,f_2))
