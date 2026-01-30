# 1. Írjon egy FV-t, ami bekér a felhasználótól egy számot, [10,20] között úgy, hogyha rossz értéket adott meg ismételje meg a bekérést! Adja vissza a bekért helyes értéket!
# 2. Írjon egy FV-t, ami visszaad egy listát. A korábban bekért szám legyen a darabszám. A számok pedig 2 jegyű, de 4-gyel nem osztható számok!
# 3. Írjon egy Fv-t, ami visszaadja a listából az első 7-re végződő szám indexét, ha van ilyen!
import random

def szamBekerese():
    szam = int(input("Adjon meg egy számot [10,20] között: "))
    #while(not(szam>=10 and szam<=20)):
    while(szam<10 or szam>20):
        print("Hibásan adta meg a számot!")
        szam = int(input("Adjon meg egy számot [10,20] között: "))
    return szam

def listaFelolt(n):
    lista = []
    for i in range(0,n,1):
        szam = random.randint(10,99)
        # while(szam % 4 == 0):
        #     szam = random.randint(10,99)
        if(szam % 4 == 0):
            szam += 1
        lista.append(szam)
    return lista

def kereses(lista):
    i = 0
    # ciklus amíg (i<hossz(lista) és NEM Ttul(lista[i]))
    while(i<len(lista) and lista[i] % 10 != 7):
        i+=1
    # c.v.
    # vane = i < hossz(lista)
    vane = i < len(lista)
    # ha(vane) vissza: i
    if(vane): return i
    # különben vissza: -1
    else: return -1

def main():
    db = szamBekerese()
    szamokLista = listaFelolt(db)
    print(szamokLista)
    index = kereses(szamokLista)
    if(index == -1):
        print("Nincs a listában 7-tel osztható elem")
    else:
        print("Van a listában 7-tel osztható elem, az",index+1,"helyen")

main()

# HF
# 1. Írjon egy függvéynt, ami visszatér egy listaáva. Töltse fel a listát a francia kártya lapjaival! T - treff, K-káró, S-szív, P-pikk Tehát:  T1, T2, ... T13, K1, K2, ..., K13, P1, P2, ..., P13, S1,S2, ... S13
# 2. Írjon egy függvényt, amit megkeveri a pakolit (véletlen hely kiválasztásával)
# index1, index2 cseréje
# seged = index1
# index1 = index2 
# index2 = seged
# 3. Írjon egy paraméteres függvényt, ami megadja, hogy hányadik helyen szerepel a paraméterben megadott lap!
# 4. Kérjen be a felhasználótól egy lap értéket, és adja meg hányadik helyen van.
# Írassa ki a megkevert pakolit az ellenőrzéshez!