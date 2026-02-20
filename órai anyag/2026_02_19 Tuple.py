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

    # tördelés - split
    szoveg = "Jani 2000 10 03"
    print(szoveg)
    tordelt = szoveg.split(" ")
    print(tordelt)
    print(2026-int(tordelt[1]))

    adat = (tordelt[0], int(tordelt[1]), int(tordelt[2]), int(tordelt[3]))
    print(adat)

    szoveg2 = "2026.02.19 3 Programozás"
    # 2026.02.19
    # 2 - február
    szoveg2Tordel = szoveg2.split(" ")
    print(szoveg2Tordel)
    datum = szoveg2Tordel[0].split(".")
    print(datum[1])

    # ABC-123,Kis Pista,KJ358638351,1992.03.10
    # Év? 1992
    # Vezetéknév? Kis

    auto = "ABC-123,Kis Pista,KJ358638351,1992.03.10".split(",")
    print(auto)
    nev = auto[1].split(" ")
    datum = auto[3].split(".")
    print(nev[0], datum[0])

    # Hf 
    # "ABC123 Kis Pista KJ-358638351 1992_03_10"
    st = "ABC123 Kis Pista KJ-358638351 1992_03_10".split(' ')
    rendszam = st[0]
    print(rendszam[3],rendszam[4],rendszam[5],sep="")
    print(rendszam[3]+rendszam[4]+rendszam[5])
    # rendszám utolsó 3 száma
    # keretsznév
    # hónap

    #"Nagy Béla:2026_02_19 - 12:13:20"
    # Nagy Béla az adott napon és időben csekkolt be!
    # Nap?
    # óra?
    # Keresztnév?
main()
