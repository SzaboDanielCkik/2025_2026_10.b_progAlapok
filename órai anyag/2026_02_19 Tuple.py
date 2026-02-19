# a = 23
# b = "alma"
# c = True

# t = [a,b,c,["k1","k2"]]
# t[0]

# Írj egy függvényt, ami megadja, melyik hónapban volt a legjobb az eredménye!

def maxIndex(lista):
    maxi = 0
    #for i in range(0, len(lista),1):
    for i in range(len(lista)):
        if(lista[i]>lista[maxi]):
            maxi = i
    return maxi

def maxIndex2(szamok, honapok):
    maxi = 0
    honap = honapok[0]
    for i in range(len(szamok)):
        if(szamok[i]>szamok[maxi]):
            maxi = i
            honap = honapok[i]
    return (honap,maxi, szamok[maxi])

def main():
    honapok = ["Január","Február","Március","Április","Május","Június","Július","Augusztus","Szeptember","Október","November","December"]
    Jani = [4.0, 3.8, 4.2, 4.1, 3.8, 4.2, 3.0, 3.6, 4.2, 4.1, 4.7, 4.2]
    maxi = maxIndex(Jani)
    print(honapok[maxi])
    valasz = maxIndex2(Jani,honapok)
    #valasz[2] = 5.0
    print(valasz)



main()
