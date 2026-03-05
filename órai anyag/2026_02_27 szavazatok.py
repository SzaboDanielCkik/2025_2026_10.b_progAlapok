
def listaFeltoltes():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(' ')
        lista.append((int(st[0]), int(st[1]), st[2], st[3],st[4]))
    return lista

def kereses(lista, vn, kn):
    i = 0
    #while(i<len(lista) and (lista[i][2]!= vn or lista[i][3]!= kn)):
    while(i<len(lista) and not (lista[i][2]== vn and lista[i][3]== kn)):
        i+=1
    if(i<len(lista)):
        return i
    else:
        return -1

def feladat3(adatok):
    vezeteknev = input("Adja meg a vezetéknevet: ")
    keresztnev = input("Adja meg a keresztnevet: ")
    #nev = input("Adjam egy teljes nevét szóközzel elválasztva: ").split(" ")
    # nev[0] - vezeteknev, nev[1] - keresztnev
    index = kereses(adatok,vezeteknev,keresztnev)
    if(index >= 0 ):
        print(adatok[index][1])
    else:
        print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")

def osszesSzavazat(adatok):
    osszeg = 0
    for i in range(len(adatok)):
        osszeg += adatok[i][1]
    return osszeg


def feladat4(adatok):

    szavazatokSzama = osszesSzavazat(adatok)
    mindenki = 12345
    szazalek = szavazatokSzama / mindenki * 100
    print(f"A választáson {szavazatokSzama} állampolgár, a jogosultak {round(szazalek,2)}%-a vett részt.")
    # A választáson 5001 állampolgár, a jogosultak 40,51%-a vett részt.

def partDarab(adatok, part):
    db = 0
    for i in range(len(adatok)):
        if(adatok[i][4] == part):
            db+=1
    return db

def feladat5(adatok):
    gyep = partDarab(adatok,"GYEP")
    hep = partDarab(adatok,"HEP")
    tisz = partDarab(adatok,"TISZ") 
    zep = partDarab(adatok,"ZEP")
    fugg = partDarab(adatok,"-")
    print("Gyümölcsevők Pártja =",gyep)
    print("Húsevők Pártja =",hep)
    print("Tejivók Szövetsége =",tisz)
    print("Zöldségevők Pártja =",zep)
    print("Független Párt =",fugg)

    #Gyümölcsevők Pártja (GYEP), a Húsevők Pártja (HEP), a Tejivók Szövetsége (TISZ) vagy a Zöldségevők Pártja (ZEP)

def maximumSzavazatok(adatok):
    maxe = adatok[0][1]
    for i in range(len(adatok)):
        if(adatok[i][1]>maxe):
            maxe = adatok[i][1]
    return maxe

def feladat6(adatok):
    maxe = maximumSzavazatok(adatok)
    for i in range(len(adatok)):
        if(adatok[i][1] == maxe):
            print(f"{adatok[i][2]} {adatok[i][3]} - {adatok[i][4]}")

def main():
    adatok = listaFeltoltes()
    #print(adatok)

    # 2. feladat
    print("A helyhatósági választáson",len(adatok),"képviselőjelölt indult.")

    # 3. feladat
    feladat3(adatok)

    # 4. feladat
    feladat4(adatok)

    # 5. feladat
    feladat5(adatok)

    # 6. feladat
    feladat6(adatok)

    # aminosavas feladat
main()