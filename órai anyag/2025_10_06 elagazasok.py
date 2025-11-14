import random
import math
# kérjen be egy egész számot és döntse el, hogy páros vagy páratlan?

szam = 23 #int(input("Adjon meg egy egész számot:"))
if(szam % 2 == 0):
    print("páros")
else: # szam % != 0
    print("páratlan")

# kérjen be a felhasználótól egy számot és mondja meg, hogy 10-zel osztható -e? Ha nem osztható 10-zel írja ki az utolsó számjegyét!
# pl. be: 10 ki: tízzel osztható
# pl. be: 12 ki: tízzel nem osztható, utolsó számjegy 2

if(szam % 10 == 0):
    print("tízzel osztható")
else: 
    print("tízzel nem osztható")
    print("az utolsó számjegy: " + str(szam % 10))

# Kérjen be egy másik számot és írassa ki a két szám reciprokának összegét!

szam2 = 12 #int(input("Adjon meg egy másik számot: "))

if(szam != 0):
    if(szam2 != 0):
        rec = 1/szam
        rec2 = 1/szam2
        print(rec+rec2)
    else:
        print("a második számnak nincs reciproka")
else:
    print("az első számnak nincs reciproka")

# Adja meg a két szám össegének gyökét!

if(szam + szam2 >= 0):
    print(math.sqrt(szam+szam2))
else:
    print("A két szám összege negatív")

# Logikai operátorok
# and, or, xor, not

if(szam != 0 or szam2 != 0):
        rec = 1/szam
        rec2 = 1/szam2
        print(rec+rec2)
else:
    print("A két szám valamelyik nulla!")

# HF: bool algebra
# HF: Kérjen be a felhasználótól 3 db számot (lehet tört is). Ez a három szám egy háromszög három oldala. 
# 1. Derékszögű-e a háromszög?
# 2. Egyenlőszarú-e a háromszög?
# 3. Szabályos-e a háromszög?

# HF python - ciklusok, loops, iterációk, ...


# Generáljon ki három véletlen háromjegyű számot, amelyek 13-al oszthatók! 
# Adja meg az átlaguk!
# Állítsa ezeket sorrendbe!
# Van-e közöttük 4-el végződő?

# Otthon tessék lemásolni a github-os repository tartalmát (pull)
# Házi feladat elkészítése
# add, commit, push

# páros kétjegyű [5,44]*2 
# 100/13 = 7,6
# 999/13 = 76,8
a = random.randint(8,76)*13
b = random.randint(8,76)*13
c = random.randint(8,76)*13

szamjegy = int(input("adjon meg egy számjegyet"))

print(a,b,c)

if(a % 10 == szamjegy or b % 10 == szamjegy or c % 10 == szamjegy):
    print("Van közte "+str(szamjegy)+"-re végződő")
else:
    print("Nincs közte "+str(szamjegy)+"-re végződő")

