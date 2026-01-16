"""
Függvények
(scratch Blokkok)

Előr definiált (megírt, megfogalmazott) folyamatok, amik külső értékől függően, végrehajtják a belső utasításokat!

def fuggvenyNev():
    #Függvény tartalma

fuggvenyNev() # függvény meghívása
"""

import random


# Visszatérési érték nélküli függvények - eljárás
# Álatlában kiíratás során használjuk
# osszeadas függvény definiálása
def osszeadas():
    a = 12
    b = 17
    print(a+b)

# osszeadás külső értéktől függően PARAMÉTEREN keresztül
def osszeadasParam(a,b):
    c = a + b
    print(c)

#osszeadas függvény meghívása
osszeadas()
osszeadasParam(18,13)

# Visszatéréssel rendelkező függvények
def kettoAtizediken():
    # a = math.pow(2,10)
    a = 2**10
    return a

valtozo = kettoAtizediken()
print(valtozo)

def osszeadasVisszateressel(a,b):
    c = a + b
    return c

print(osszeadasVisszateressel(13,17))
print(osszeadasVisszateressel(11,10))

# házi feladat
# definiálj egy olyan eljárás (nem tér vissza értékkel), aminek a paraméterébe bekerül egy darabszám, és a függvény pedig kiír ennyi darab véletlen számot egymás mellé!

def veletlenszamKiiratas(db):
    for i in range(0,db,1):
        print(random.randint(100,999),end=" ")
    print()


veletlenszamKiiratas(10)

# készítsen egy eljárás, ami függ egy szövegtől, és kiírja a szót visszafele

def szovegVisszafele(szoveg):
    for index in range(len(szoveg)-1,-1,-1):
        print(szoveg[index], end="")
    print()

szovegVisszafele("kalapács")
# készítsen egy függvényt, ami függ egy szövegtől, és visszaadja a szót visszafele

def szovegVisszafeleFv(szoveg):
    visszaSzoveg = ""
    for index in range(len(szoveg)-1,-1,-1):
        visszaSzoveg += szoveg[index]
    return visszaSzoveg
    
print(szovegVisszafeleFv("abba"))

# Írjon egy fv-t, ami egy beküldött szóról eldönti, hogy palindrom-e és vissza adja válaszul? (Visszafele ugyan az)

def palindrome(szo):
    # i = 0
    # while(i<=len(szo)//2 and szo[i] == szo[len(szo)-1-i]):
    #     i+=1
    # if(i>len(szo)//2):
    #     return "palindrom"
    # else:
    #     return "nem palindrom"

    # if(szo == szovegVisszafeleFv(szo)):
    #     return "palindrom"
    # else:
    #     return "nem palindrom"

    if(szo == szovegVisszafeleFv(szo)):
        return True
    else:
        return False

print("palindrom-e a szó: ", palindrome("abba"))

def palindromeG(szo):
    for i in range(0,len(szo), 1):
        if(szo[i] != szo[len(szo)-1-i]):
            return False
    return True
print("palindrom-e a szó: ", palindromeG("abba"))