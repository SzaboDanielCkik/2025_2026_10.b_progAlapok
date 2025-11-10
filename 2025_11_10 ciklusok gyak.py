import random

# generáljon ki 10 db egy jegyű nem nulla véletlen számot!
# írassa ki a számok összegét!

osszeg = 0
for a in range(1,11,1):
    velSzam = random.randint(1,9)
    osszeg += velSzam
    print(velSzam, end=" ")
print()
print("Összeg:",osszeg)

# Hány darab páros véletlen számot generált ki?
# Melyik a legnagyobb véletlen szám?