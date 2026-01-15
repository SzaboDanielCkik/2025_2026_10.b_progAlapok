# Jancsi és Juliska autós kártyát gyűjtenek. Hogy ne legyen vita és gyorsan meg tudják különböztetni melyik autó kié, ezért a következőt találták ki. Mivel minden autó végsebessége 3 jegyű, ezért megnézik a középső számot. Ha páros akkor Jancsié, ha páratlan akkor Juliskáé. 
# Van összesen 30 kártyájuk. Szeretik egymás mellé rakni a kártyákat. Szimuláld a feladatot!
# Írj egy programot, ami kigenerál [300, 499] között egy számot úgy, hogy minden páros helyen Jancsi kártyája van, minden páratlan helyen Juliskáé!
# Add meg Jancsi autóinak végsebességének átlagát!
# Add meg hány darab autója van Juliskának, ami 380-nál nagyobb a végsebessége!

import random as rnd

kartyak = []

for i in range(0,30,1):
    elso = rnd.randint(3,4)
    masodik = -1
    if(i % 2 == 1): # Jancsi száma
        masodik = rnd.randint(0,4)*2
    else: # Juliska száma
        masodik = rnd.randint(0,4)*2+1
    harmadik = rnd.randint(0,9)
    #szam = int(str(elso)+str(masodik)+str(harmadik))
    szam = elso * 100 + masodik * 10 + harmadik
    kartyak.append(szam)
print(kartyak)

# Jancsi kártyáinak lekérése

osszeg = 0
for i in range(1,len(kartyak),2):
    #print(kartyak[i])
    osszeg += kartyak[i]

db = len(kartyak)/2
atlag = osszeg / db
print("Jancsi autoinak végsebességének átlaga: ", round(atlag,2))

# Juliska kártyái

db_juliska = 0
for i in range(0, len(kartyak),2):
    if(kartyak[i] > 380):
        db_juliska += 1
print("Juliskának",db_juliska,"db autója van, ami 380-nál gyorsabb")

# 
