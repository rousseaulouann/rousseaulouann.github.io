import turtle

turtle.tracer(0,0)
turtle.screensize(2000,2000)
turtle.pu()
turtle.goto(-500,0)
turtle.pd()

def dessiner(courbe, longueur, angle):

    for caractere in courbe:
        if caractere == '+': turtle.left(angle)
        elif caractere == '-': turtle.right(angle)
        elif caractere in ['F', 'G']: turtle.forward(longueur)



def regleKoch(chaine):
    nouvelleChaine = ''
    for lettre in chaine:
        if lettre == 'F':
            nouvelleChaine = nouvelleChaine + 'F - G + F + G - F'
        elif lettre == 'G' :
            nouvelleChaine = nouvelleChaine + 'GG'
        else :
            nouvelleChaine = nouvelleChaine + lettre
    return nouvelleChaine


def courbeKoch(motifInitial, niter):

    motifInitial = 'F - G - G'
    courbe = motifInitial
    for i in range(niter):
        nouveauMotif = regleKoch(courbe)
        courbe = nouveauMotif
    return courbe


def Sierpinski(motifInitial, niter):
    courbe = courbeKoch(motifInitial, niter)
    Sierpinski = ''
    for _ in range(niter):
        Sierpinski += courbe
        Sierpinski += '--'
    return Sierpinski

longueur = 10
angle = 120
niter = 6

dessiner(courbeKoch('F - G - G', niter), longueur, angle)

turtle.update()
turtle.exitonclick()