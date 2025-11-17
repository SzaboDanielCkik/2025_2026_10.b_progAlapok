import random
"""
Elől tesztelős ciklus
While ciklus

- Nem tudjuk, hogy hányszor fog lefutni (hányszor ismétel)
- Feltételhez kötött!
- Akkor ismétel, ha feltétel igaz

while(Feltétel):
    Utasítások (szekvencia)
"""

# Generáljon véletlen számokat [0,10] között, amíg nullát nem kapunk!

velszam = random.randint(0,10)
print(velszam, end=" ")
while(velszam != 0):
    velszam = random.randint(0,10)
    print(velszam,end=" ")
print()

# Kérjen be számokat, addig amíg nullát nem adnak meg!
# Adja meg a beírt számok átlagá!

osszeg = 0
db = 0
szam = int(input("Adjon meg egy számot (0-nál kilép): "))
# osszeg += szam
# db += 1
while(szam != 0):    
    osszeg += szam
    db += 1
    szam = int(input("Adjon meg egy számot (0-nál kilép): "))
print(round(osszeg/db,2))

# Adott egy szöveg. Adja meg, hogy van-e benne x betű!

