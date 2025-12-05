import random

gondolt_szam = random.randint(10,99)
print(gondolt_szam)

probalkozasok = 1
print("Melyik kétjegyű számra gondoltam?")
print(str(probalkozasok)+". próbálkozás:")
szam = int(input("Szám: "))

while(szam != gondolt_szam):
    if(szam > 9 and szam < 100):
        if(szam > gondolt_szam):
            print("A szám nagyobb mint a gondolt szám.")
        elif(szam < gondolt_szam):
            print("A szám kisebb mint a gondolt szám.")
        probalkozasok += 1
    else:
        print("Nem kétjegyű számot adott meg!")
    print(str(probalkozasok)+". próbálkozás:")
    szam = int(input("Próbálkozz még egyszer: "))    

print("Eltaláltad")
print("Próbálkozások száma:", probalkozasok)

# Írassa ki hány darab próbálkozás volt!
# Figyeljen arra, hogyha nem kétjegyű számot adott meg, az ne legyen új próbálkozás, és figyelmeztesse a felhasználót!
# Minden szám bekérésénél írja, ki az aktuális próbálkozások számát!