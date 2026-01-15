"""
Függvények
(scratch Blokkok)

Előr definiált (megírt, megfogalmazott) folyamatok, amik külső értékől függően, végrehajtják a belső utasításokat!

def fuggvenyNev():
    #Függvény tartalma

fuggvenyNev() # függvény meghívása
"""

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

# készítsen egy eljárás, ami függ egy szövegtől, és kiírja a szót visszafele

# készítsen egy függvényt, ami függ egy szövegtől, és visszaadja a szót visszafele