# [-950,950] közötti x50, x00 típusú számok.
# [-19, 19]*50 
# Készítsen egy fv-t ,amiben visszaadjuk egy listából, hogy hány darab negatív x00-ra végződő szám van.

import random
# eljárás - visszatérési érték nélküli függvény - olyan függvény, aminek nincs visszatérési értéke

# HF 
# Írjon egy fv-t, ami bármilyen lista elemei közül megadja a legnagyobb szám indexét!
# Írjon egy fv-t, ami bármilyen lista elemeire kiszámolja az átlagot!
# Írjon egy fv-t, ami bármilyen lista elemeire kiszámolja a pozitív számok átlagát!

# Írjon fv-t, ami visszaadja a listánk terjedelmét. Terjedelem = maximum-minimum


# def terjedelem(lista):
#     maxe = lista[0]
#     mine = lista[0]
#     for i in range(1,len(lista),1):
#         if(lista[i]>maxe):
#             maxe = lista[i]
#         if(lista[i]<mine):
#             mine = lista[i]
#     terjedelem = maxe - mine
#     return terjedelem
    
def maximumErtek(lista):
    maxe = lista[0]
    for i in range(1,len(lista),1):
        if(lista[i]>maxe):
            maxe = lista[i]
    return maxe

def minimumErtek(lista):
    mine = lista[0]
    for i in range(1,len(lista),1):
        if(lista[i]<mine):
            mine = lista[i]
    return mine

def terjedelem(lista):
    maxe = maximumErtek(lista)
    mine = minimumErtek(lista)
    return maxe - mine

def maximumIndex(lista):
    maxi = 0 # maxi - maximum index
    # ciklus i = 1-tól (n-1)-ig egyesével
    for i in range(1,len(lista),1):
    #   ha(lista[i]>lista[maxi])
        if(lista[i]>lista[maxi]):
            maxi = i
    #   e.v.
    #c.v.
    # vissza: maxi
    return maxi

def pozitivSzamokAtlaga(lista):
    db = 0
    osszeg = 0
    for elem in lista: # végigmegyünk a lista összes elemén
        if(elem > 0): # ha pozitív az aktuális szám, akkor
            db+=1   # a db változót növeljük 1-gyel
            osszeg += elem
    atlag = osszeg / db
    return atlag

    


def listaAtlaga(lista):
    osszeg = 0
    # for elem in lista:
    #     osszeg += elem
    for i in range(0,len(lista), 1):
        osszeg += lista[i]
    atlag = osszeg / len(lista)
    return atlag
    

def veletlenLista(n):
    #n = 13
    lista = []
    for i in range(0,n,1):
        negative = random.randint(0,1)
        vszam = random.randint(2,19)*50
        if(negative == 0):        
            lista.append(-1*vszam)
        else:
            lista.append(vszam)
    #print(lista)
    return lista

def negativ00raVegzodo(barmilyenLista):
    db = 0
    for i in range(0,len(barmilyenLista),1):
        if(barmilyenLista[i] % 100 == 0):
            db+=1
    return db

def main():
    lista1 = veletlenLista(13)
    print(lista1)
    lista2 = veletlenLista(7)
    print(lista2)

    print("00-ra végződőek lista1: ",negativ00raVegzodo(lista1))
    print("00-ra végződőek lsita2: ",negativ00raVegzodo(lista2))

    lista1atalaga = listaAtlaga(lista1)
    print("az elso lista átlaga: ", lista1atalaga)
    print("a második lista átlaga: ", listaAtlaga(lista2))

    print("Az első lista pozitív számainak átlaga: ", 
          pozitivSzamokAtlaga(lista1))
    print("A második lista pozitív számainak átlaga: ", 
          pozitivSzamokAtlaga(lista2))
    
    maxIndexLista1 = maximumIndex(lista1)
    print("Első lista legnagyobb elem helye: ", maxIndexLista1+1)

    print("lista1 maximum:",maximumErtek(lista1))
    print("lista1 minimum:", minimumErtek(lista1))
    print("lista1 terjedelme:",terjedelem(lista1))

main()