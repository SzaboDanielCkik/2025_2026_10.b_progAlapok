def feltolt():
    t=[]
    f=open("feltalalok.txt","r",encoding="utf-8")
    osszesSor=(f.readlines())
    for i in range(len(osszesSor)):
        adatok=osszesSor[i].strip().split("/")
        halalozas=0
        if (adatok[2]!=""):
            halalozas=int(adatok[2])
        t.append((adatok[0],int(adatok[1]),halalozas,adatok[3]))

    f.close
    return t


def kiir(t):
    for nev,_,_,talalmany in t:
        print(f"{nev}=>{talalmany}")

def feladat4(t,ev):
    f=open("kiiras.txt","w",encoding="utf-8")
    for nev,sz,h,_ in t:
        if (h-sz>ev):
            print(nev)
            f.write(f"{nev}\n")
    f.close


def main():
    t=feltolt()
    print(f"2. feladat: A fájlban {len(t)} tudós adata szerepel")
    print(f"3. feladat: feltalálpk-találmányok")
    kiir(t)
    ev=int(input())
    feladat4(t,ev)
main()