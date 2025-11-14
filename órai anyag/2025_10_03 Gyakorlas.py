# Generálj ki egy páros véletlen számot [-10, 10] között!
# Írasd ki az adott számot!

import random 
import math

a = random.randint(-5,5)*2
print("szám: "+ str(a))

# vegyük a szám abszolut értékét!
# ha a szám negatív akkor szám*(-1) különben önmaga
if a<0 :
    print("abs: "+str(a*(-1)))
else: # a>=0
    print("abs: "+str(a))

# Írassa ki a szám gyökét!
# gyök(a) - a négyzetgyök(a) jelenti azt a nemnegatív számot ,amit ha négyzetre emelünk megkapjuk az a-t!
# negatív, nulla, pozitív
# nem negatív = nulla vagy pozitív
# nem pozitív = nulla vagy negatív

if(a >= 0 ):
    print("gyök(a): "+str(math.sqrt(a)))
else:
    print("A negatív számnak nincs gyöke.")

# döntse el a számról, hogy pozitív, negatív vagy nulla

if(a>0):
    print("pozitív")
else:
    if(a==0):
        print("nulla")
    else:
        print("negatív")

if(a>0):
    print("pozitív")
elif(a==0):
    print("nulla")
else:
    print("negatív")

# Felhasználótól bekérés

#szoveg = input("Adjon meg egy számot: ")
#print(szoveg)

# HF 8-13

# Szekvencia -  utasítások sorozata
# Szelekció - Elágazás
# Iteráció - ciklus, ismétlés

# HF 13. megoldás 

sec = 3923 #15917
# 1 óra 5 perc 23 másodpert
# 1*3600 + 5*60 + 23 = 3923 sec

ora = sec // 3600
perc = (sec - ora * 3600) // 60 
#mp =  (sec - ora * 3600) - (perc * 60)
mp = sec % 60
print(ora,"óra")
print(perc,"perc")
print(mp,"másodperc")

