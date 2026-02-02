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
import random

def kartyaGeneralas():
    lista = []
    for i in range(1,14,1):
        lista.append("T"+str(i))
        lista.append("P"+str(i))
        lista.append("K"+str(i))
        lista.append("S"+str(i))
    return lista

def keveres(pakli):
    for i in range(500):
        a = random.randint(0,len(pakli)-1)
        b = random.randint(0,51)
        sv = pakli[a]
        pakli[a] = pakli[b]
        pakli[b] = sv

def lapIndexe(lap, pakli):
    index = 0
    # ciklus amíg (NEM Ttul(lista[i]))
    while( pakli[index] != lap):
        index+=1
    # c.v.
    # vissza: index
    return index

def main():
    pakli = kartyaGeneralas()
    #print(pakli)
    keveres(pakli)
    print(pakli)
    lap = input("Adjon meg egy lapot - T,P,S,K + [1,13] (pl P1): ")
    index = lapIndexe(lap, pakli)
    print(index)
    
main()

# HF 
# Szimuláljon egy matematika versenyt és az eredményeire készített statisztikát! Mind a 17 diák nagyon ügyes, így kevés rossz verseny dolgozat született. A döntőbe jutásésrt 70%-ot el kell érni.
# 1. Készítsen egy függvényt, amit feltölt egy listát úgy, hogy 50%-os eseéllyel szülessenek 120-200 közötti pontok, a maradék pedig 50-120 közötti pont legyen!
# 2. Írjon függvényt, ami visszaadja a versenydolgozatok átlagát!
# 3. Írjon függvényt, ami visszaadja a versenydolgozatok terjedelmét!
# 4. Írjon függvényt, ami visszaadja lett-e maximum pontos?
# 5. Írjon függvényt, ami visszaadja hány versenyző jutott a döntőbe?
# 6. Írjon függvényt, ami visszaadja, hogy volt-e 50 pontos, ha volt hányadik tanuló?