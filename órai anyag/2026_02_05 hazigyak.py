# HF 
# Szimuláljon egy matematika versenyt és az eredményeire készített statisztikát! Mind a 17 diák nagyon ügyes, így kevés rossz verseny dolgozat született. A döntőbe jutásésrt 70%-ot el kell érni.
# 1. Készítsen egy függvényt, amit feltölt egy listát úgy, hogy 50%-os eseéllyel szülessenek 120-200 közötti pontok, a maradék pedig 50-120 közötti pont legyen!
# 2. Írjon függvényt, ami visszaadja a versenydolgozatok átlagát!
# 3. Írjon függvényt, ami visszaadja a versenydolgozatok terjedelmét!
# 4. Írjon függvényt, ami visszaadja lett-e maximum pontos?
# 5. Írjon függvényt, ami visszaadja hány versenyző jutott a döntőbe?
# 6. Írjon függvényt, ami visszaadja, hogy volt-e 50 pontos, ha volt hányadik tanuló?
import random


def listaFeltoltes():
    lista = []
    for i in range(0,17,1):
        valsz = random.randint(0,100)
        if(valsz >= 50):
            lista.append(random.randint(120,200))
        else:
            lista.append(random.randint(50,120))
    return lista

def listaAtlag(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i]
    atlag = osszeg/len(lista)
    return atlag

def listaMaximuma(lista):
    maxe = lista[0]
    for i in range(1,len(lista),1):
        if(lista[i]>maxe):
            maxe = lista[i]
    return maxe

def listaMinimuma(lista):
    mine = lista[0]
    for i in range(1,len(lista),1):
        if(lista[i]<mine):
            mine = lista[i]
    return mine

def listaTerjedelme(lista):
    maximum = listaMaximuma(lista)
    minimum = listaMinimuma(lista)
    return maximum - minimum

def vaneMaxpontos(lista):
    #n = 200
    index = 0
    while(index<len(lista) and lista[index] != 200):
        index += 1
    vane = index < len(lista)
    return vane

def dontobeJutottakDb(lista):
    db = 0
    for i in range(0,len(lista),1):
        # szazalek = lista[i]/200*100
        # if( szazalek >= 70):
        ponthatar = 140 #200 / 100 * 70
        if( lista[i] >= ponthatar):
            db += 1
    return db

def ertek50Index(lista):
    i = 0
    while(i<len(lista) and lista[i] != 50):
        i+=1 
    vane = i<len(lista)
    if(vane):
        return i
    else:
        return -1

def main():
    pontok = listaFeltoltes()
    print(pontok)

    # 2. feladat
    atlag = listaAtlag(pontok)
    print("Átlag: ", round(atlag,2))

    # 3. feladat
    terjedelem = listaTerjedelme(pontok)
    print("Terjedelem: ",terjedelem)

    # 4. feladat
    vaneMaxpont = vaneMaxpontos(pontok)
    if(vaneMaxpont):
        print("Van max pontos")
    else:
        print("Nincs max pontos")

    # 5. feladat
    darab = dontobeJutottakDb(pontok)
    print(darab,"tanuló jutott a döntőbe")

    # 6. feladat
    index = ertek50Index(pontok)
    if(index == -1):
        print("Nincs 50 pontos dolgozat a versenyen")
    else:
        #print("A(z)", str(index+1) + ". van az 50 pontos dolgozat")
        print(f"A(z) {index+1}. van az 50 pontos dolgozat")
main()