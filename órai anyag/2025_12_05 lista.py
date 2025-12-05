"""
lista - dinamikus
- tudunk bele új elemet rakni, ezzel nő az elemszáma
- tudunk belőle törölni, ezzel csökken az elemszáma
- lekérhető bármelyik eleme
- módosítható bármelyik elem
deklarálás + inicializálás:
létrehozás + kezdőérték adás:
lista_neve = []
új elem hozzáadása:
lista_neve.append(ujelem)
elem törlése:
lista_neve.remove(elem)
beégetett lista:
lista_neve = [3,2,5,7,1]
lista hossza:
len(lista_neve)
"""
szamok = [3,2,5,7,1]
print(szamok)
szamok.append(12)
print(szamok)
szamok.remove(3)
print(szamok)
print("első elem:", szamok[0])
print("lista hossza:",len(szamok))
print("utolsó elem:", szamok[len(szamok)-1])
#print("utolsó elem:", szamok[-1])

# Házi feladat
# Töltsön fel egy 13 elemű listát [0,20] közötti véletlen számmal
# Számok átlaga
# Hány darab páros szám van a listában
# van-e benne nulla

# a szövegben van-e sz betű

# if "sz" in szoveg:
#     print("benne van az sz betű")
# else:
#     print("nincs benne sz betű")

szoveg = "gezakekazeg"
dube = "ny" # dupla betű
print(szoveg)
index = 0
while(index < len(szoveg)-1 and not(szoveg[index] == dube[0] and szoveg[index+1] == dube[1])):
    index+=1
if(index<len(szoveg)-1):
    print("benne van az",dube,"betű")
else:
    print("nincs benne",dube,"betű")

# palindrom-e
ujszoveg = ""
for index in range(len(szoveg)-1, -1, -1):
    ujszoveg += szoveg[index]
if(ujszoveg == szoveg):
    print("A szoveg, palindrom")
else:
    print("A szoveg nem palindrom")

j = 0
while(j<len(szoveg)/2 and szoveg[j] == szoveg[len(szoveg)-1-j]):
    j+=1
if(j<len(szoveg)/2):
    print("A szoveg nem palindrom")
else:
    print("A szoveg palindrom")

