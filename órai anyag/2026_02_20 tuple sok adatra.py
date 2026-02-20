
def listaFeltoltes():
    db = int(input())
    t = []
    #for i in range(0,db,1):
    for i in range(db):
        sor = input() # alma 12 500
        st = sor.split(' ') # segéd lista : ['alma', '12', '500']
        #st = input().split(' ')
        tupe = (st[0],int(st[1]),int(st[2]))
        t.append(tupe)
        #t.append((st[0],int(st[1]),int(st[2])))
    return t

def mazsaOsszegzese(adatok):
    osszeg = 0
    for i in range(0,len(adatok),1):
        osszeg += adatok[i][1]
    return osszeg

def hanyArNagyobb(adatok, ar):
    db = 0
    for i in range(0,len(adatok),1):
        if(adatok[i][2]>ar):
            db += 1
    return db

def main():
    adatok = listaFeltoltes()
    print(adatok)
    adat = adatok[2]
    print(adat[0])
    # print(adatok[2][0])

    # írjon függvényt, ami visszaadja az összetett szerkezetből, hogy összesen hány mázsa gyümölcs van!
    osszesen = mazsaOsszegzese(adatok)
    print(osszesen," q gyümölcsünk van.")
    # írjon függvényt, ami visszaadja a paraméterben megadott értéktől nagyobb összeggel rendelkező gyümölcsök darabszámát!
    ar = 500
    db = hanyArNagyobb(adatok, ar)
    print(db,"gyümölcs ára nagyobb mint ",ar)

    # Hf
    # Írjon függvényt, ami megadja a legdrágább gyümölcs nevét!
    # Írjon fv-t, ami bekér a felhasználótól egy gyömlcsöt, és ha van ilyen gyümölcs kiírja az adatait BE: szilva: Ki: 13 q, 300 Ft/kg
    # ha nincs ilyen adat, akkor írja ki, hogy nincs ilyen gyümölcs!
    # Hf - szeleromu.txt
    # telepules, vármegye, tájolás, hány darab szélerőmű, szélerőművenkénti teljesítmény kw/h, mikor telepítették
    # Magyarországon hány szélerőmű van?
    # Írjuk ki, hogy melyik településen és melyik évben telepítették a legtöbb szélerőművet
    # Kérjünk be egy települést! Nézzük meg, hogy van-e ott szélerőmű (pl.: Cegléd: nincs)
main()