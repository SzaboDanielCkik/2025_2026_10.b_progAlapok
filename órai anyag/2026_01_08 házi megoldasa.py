# 30 db 13, 17-re végződő számokkal, hány osztható 13-mal és 17-tel
# számtani átlag
# hány darab szám van átlag alatt
# mértani átlag
# a mértani átlag alatti számok összege
import random
import math

n = 31
lista = []

for i in range(0,n,1):
    valtozo = random.randint(10,99)
    veletlen = random.randint(1,2)
    if(veletlen == 1):
        lista.append(valtozo*100+17)
    else:
        lista.append(valtozo*100+13)

print(lista)

osszeg = 0
# for index in range(0,n,1):
#     osszeg += lista[index]
for elem in lista:
    osszeg += elem
#atlag = osszeg / len(lista)
atlag = osszeg / n
print(round(atlag,2))

# hány darab szám van az (sz)átlag alatt?
dba = 0
for index in range(0,n,1):
    #if(atlag>lista[index]):
    if lista[index]<atlag:
        dba += 1
print("számtani átlag alatti értékek elemszáma:",dba)

szorzat = 1
for elem in lista:
    szorzat *= elem
matlag = math.pow(szorzat,1/n) 

# a mértani átlag alatti számok összege
mossz = 0
for a in lista:
    if(matlag > a):
        mossz += a
print("mértani átlag alatti számok összege:",mossz)
# bekérsz egy hosszabb szöveget, hány darab felhasználó által megadott betű van benne?


szoveg = "bekérsz egy hosszabb szöveget, hány darab felhasználó által megadott betű van benne?"
print(szoveg)
betu = input("adjon meg egy betűt: ")

dbbetu = 0
for karakter in szoveg:
    if(karakter == betu):
        dbbetu += 1 
print(dbbetu)

# bekérsz két szót, mond meg adott indexen hány darab betű eltérés van! (pl. alma, alkat -> 2 db különbség )

szo1 = "alma"
szo2 = "alkat"
print(szo1)
print(szo2)
#len(szo1)
kulonbseg = 0
minimumhossz = 0
if(len(szo1)>len(szo2)):
    minimumhossz = len(szo2)
else:
    minimumhossz = len(szo1)
for i in range(0,minimumhossz,1):
    if(szo1[i] != szo2[i]):
        kulonbseg += 1
print(kulonbseg+)