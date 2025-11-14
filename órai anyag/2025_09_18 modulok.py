import math # math-ban lévő függvényeket tudjuk használni
import random # random-ban lévő függvényeket tudjuk meghívni, használi

a = 2
gyoka = math.sqrt(a)
print("gyök(" + str(a) +") = ",gyoka)

felkerekit = math.ceil(gyoka)
print("felsőegészrész:", felkerekit)
lekerekit = math.floor(gyoka)
print("alsóegészrész:", lekerekit)
kerekites = round(gyoka,2)
print("kerekites 2 tizedes jegyre:",kerekites)
hatvanyozas1 = math.pow(gyoka, 2)
print("gyoka négyzete:",hatvanyozas1)

alap = 2
kitevo = 5
#hatvanyozas2 = math.pow(alap,kitevo) 
hatvanyozas2 = alap ** kitevo
print(alap,"^",kitevo,"=",hatvanyozas2)

vszam1 = random.randint(2,10)
print(vszam1)

# HF pdf 3-5