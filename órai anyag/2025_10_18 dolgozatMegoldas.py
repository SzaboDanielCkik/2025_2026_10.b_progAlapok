import random
import math

# 1. feladat ---------------------------
szerencse = random.randint(0,9)
if(szerencse == 1 or szerencse == 6): # if(szerencse % 5 == 1)
    print("labda")
elif(szerencse == 2 or szerencse == 7):# if(szerencse % 5 == 2)
    print("ceruza")
elif(szerencse == 3 or szerencse == 8): # if(szerencse % 5 == 3)
    print("színes papír")
elif(szerencse == 4 or szerencse == 9): # if(szerencse % 5 == 4)
    print("bicikli")
else:
    print("nem nyert")

# 2. feladat --------------------------------------
# 891 óra 
ora = int(input("Adja meg a tenger alatt töltött időt, órában: "))
het = ora // 168 
nap = (ora - het * 168) // 24 
ora2 = (ora - het * 168) - nap * 24   # ora % 24
print("Átszámolva:",het,"hét",nap,"nap",ora2,"óra")

# 3. feladat --------------------------------------
szam = random.randint(100,999)
print("Generált háromjegyű szám:",szam)
elso = szam // 100
masodik = (szam - elso * 100) // 10
harmadik = szam % 10
# elso *100 + masodik *10 + harmadik == elso ** 3 + masodik ** 3 
# if(math.pow(elso, 3)+math.pow(masodik,3) + math.pow(harmadik,3) == szam):
if(elso ** 3 + masodik ** 3 + harmadik ** 3 == szam):
    print("A szám Armstong szám")
else:
    print("A szám nem Armstrong szám")

# 4. feladat ---------------------------------------
a = random.randint(0,10)
b = random.randint(0,10)
c = random.randint(0,10)
print("Véletlen számok:",a,b,c)
if(a != 0 and b != 0 and c != 0):
    harmonk = 3 / (1/a + 1/b + 1/c)
elif(a == 0 and b != 0 and c != 0):
    harmonk = 2 / (1/b + 1/c)
elif(b == 0 and a != 0 and c != 0):
    harmonk = 2 / (1/a + 1/c)
elif(c == 0 and a != 0 and b != 0):
    harmonk = 2 / (1/a + 1/b)
elif(a == 0 and b == 0 and c != 0):
    harmadik = 2 / (1/c)
elif(a == 0 and c == 0 and b != 0):
    harmadik = 2 / (1/b)
elif(c == 0 and b == 0 and a != 0):
    harmadik = 2 / (1/a)
else:
    print("nincs megoldás")
print("Harmonikus közép:",round(harmonk,3))
