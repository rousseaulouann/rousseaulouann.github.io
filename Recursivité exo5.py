# Créé par louan, le 28/09/2021 en Python 3.7
def etoile(n):
    print('*'*n)

def afficheTop(n):
    if n == 0:
        return

    return afficheTop(n-1),etoile(n)


def afficheDown(n):
    if n == 0:
        return
    return etoile(n),afficheDown(n-1)

afficheDown(6)
