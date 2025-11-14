# Változó deklarálása és inicializálása
# Változó létrehozása és kezdőérték adása
# valtozoNev = "kezdoertek"
nev = "Szabo Daniel"
osztaly = '10.b'
datum = "2025.09.08"
# "'"
# '"'
print(nev,osztaly, datum,sep="\n")

# operátor

# + konkatenálás, concat, összefűzés - két szöveget!!!!! 
osszefuzes = nev+" bármit, akármit "+osztaly
print(osszefuzes)

# * többszörözés
soknev = nev * 5
print(soknev)

"""
Elemi típusok
- szöveg - string - str
(- karakter)
- szám - egész (integer - int), lebegőpontos (tört) (float)
- logikai - true, false
"""

aEgesz = 123
bTort = 34.23
szSzam = "12"
logikai = True

print("a Egész:", aEgesz)
print("b Tört:", bTort)
print("sz Szam:",szSzam)
print("logikai:",logikai)

# Egesz operatorok
print("a + 2 =",aEgesz + 2)
print("a - 2 = ",aEgesz - 2)
print("a * 2 =",aEgesz * 2)
print("a / 2 = ",aEgesz / 2)

# Div - egészrész, Mod - modulus(maradék)
# div - //
# mod - %

print("a div 8 =", aEgesz // 8)
print("a mod 8 =", aEgesz % 8)

print(int(szSzam)+aEgesz)
print(szSzam+str(aEgesz))

print(str(aEgesz)+szSzam)
print(aEgesz+int(szSzam))
#\\ckik-pdc\kozos

