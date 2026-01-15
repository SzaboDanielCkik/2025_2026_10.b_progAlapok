# Generáljon egy listába 13 db olyan négyejgyű véletlen számot, ami 3,5,7-re végződik!
# Hány darab 3-ra, 5-re, és 7-re végződő szám van?
import random

lista = []

for i in range(0,13,1):
    valtozo = random.randint(100,999)
    veletlen = random.randint(1,3)
    if(veletlen == 1):
        lista.append(valtozo*10+3)
    elif(veletlen == 2):
        lista.append(valtozo*10+5)
    else:
        lista.append(valtozo*10+7)
print(lista)

haromra = 0
otre = 0
hetre = 0
for i in range(0,len(lista),1):
    if(lista[i] % 10 == 3):
        haromra += 1
    elif(lista[i] % 10 == 5):
        otre += 1
    else:
        hetre += 1 
print("háromra végződő:",haromra)
print("ötre végződő:",otre)
print("hétre végződő:",hetre)

# 30 db 13, 17-re végződő számokkal, hány osztható 13-mal és 17-tel
# számtani átlag
# hány darab szám van átlag alatt
# mértani átlag
# a mértani átlag alatti számok összege

# bekérsz egy hosszabb szöveget, hány darab felhasználó által megadott betű van benne?
# bekérsz két szót, mond meg adott indexen hány darab betű eltérés van! (pl. alma, alkat -> 2 db különbség )
