import random

def listaFeltolt(db):
    lista = []
    for i in range(0,db,1):
        szam = random.randint(2,36)
        lista.append(szam)
    return lista

def osszegzes(lista):
    osszeg = 0
    for i in range(0,len(lista),1):
        osszeg += lista[i]
    return osszeg

def kinyert(slista, flista):
    if(slista > flista):
        return "Shrek nyert"
    elif(slista<flista):
        return "Fiona nyert"
    else:
        return "Döntetlen"

def kiiratas(lista, osszeg):
    for i in range(0, len(lista) - 1,1):
        print(lista[i],end=" + ")
    print(lista[len(lista)-1],end=" ")
    print("=",osszeg)

def volteEgyezoKor(slista, flista):
    i = 0
    while(i<len(slista) and slista[i] != flista[i]):
        i+=1
    volte = i<len(slista)
    return volte

def main():
    shrek = listaFeltolt(7)
    fiona = listaFeltolt(7)
    # print(shrek)
    # print(fiona)
    shrekOsszeg = osszegzes(shrek)
    fionaOsszeg = osszegzes(fiona)
    # print(shrekOsszeg)
    # print(fionaOsszeg)
    kiiratas(shrek,shrekOsszeg)
    kiiratas(fiona,fionaOsszeg)
    if(volteEgyezoKor(shrek, fiona)):
        print("Volt egyezés")
    else:
        print("Nem volt egyezés")



main()