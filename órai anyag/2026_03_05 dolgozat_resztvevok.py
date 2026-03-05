
def adatokFeltoltese():
    lista = []
    db = int(input())
    for i in range(db):
        st = input().split(";")
        lista.append((st[0],st[1],st[2],int(st[3]),st[4]))
    return lista

def kereses(adatok, datum):
    i = 0
    while(i<len(adatok) and not (adatok[i][0] == datum)):
        i+=1
    vane = i<len(adatok)
    if(vane):
        return i
    else:
        return -1

def main():
    adatok = adatokFeltoltese()
    #print(adatok)

    # 5. feladat
    datum = input("Adjon meg egy dátumot: ")
    index = kereses(adatok, datum)
    if(index>-1):
        print(adatok[index][1],adatok[index][2], "született ekkor")
    else:
        print("Nem született senki a résztvevők közül ilyen dátummal")
main()