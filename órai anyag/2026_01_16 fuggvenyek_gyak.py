# Készítsen egy függvényt, ami egy db számtól függ, és visszaad egy felötltött listát [-10,50] közötti számokkal!
# Készítsen egy függvényt, ami bármilyen lista elemeit megvizsgálva visszaadja, hogy hány db pozitív szám van!
import random

def listaFeltolt(db):
    lista = []
    for i in range(0,db,1):
        szam = random.randint(-10,50)
        lista.append(szam)
    return lista

def pozitivDb(szamokLista):
    darab = 0
    #ciklus i = 0-tól (n-1)-ig egyesével # n-1: <len(lista)
    for i in range(0,len(szamokLista),1):
        #ha(Ttul(lista[i]))
        if(szamokLista[i]>0):
            darab += 1
        #elág. vége
    #c.v.
    #Vissza: darab
    return darab

def main():
    # lista feltöltése
    lista = listaFeltolt(13)
    print(lista)
    # darabszámolás
    print(pozitivDb(lista))
main()