# Házi feladat
# Töltsön fel egy 13 elemű listát [0,20] közötti véletlen számmal
# Számok átlaga
# Hány darab páros szám van a listában
# van-e benne nulla
import random

n = 5  # a lista elemszáma


lista = []
for index in range(0,n,1):    
    a = random.randint(0,20)
    lista.append(a)
    #lista.append(random.randint(0,20))

print(lista)

# Számok átlaga - összeadjuk a számokat és elosszuk az összeget a számok darabszámával.
osszeg = 0
for index in range(0,len(lista),1):
    osszeg += lista[index]
print(osszeg)