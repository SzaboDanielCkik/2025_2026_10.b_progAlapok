
def fajlbeolvasas():
    fajl = open("txt adatok/gyumolcsok.txt","r",encoding="utf-8")
    # osszesadat = []
    # osszesadat.append(fajl.read().split('\n'))
    # print(osszesadat)

    # sorok = fajl.readlines()
    # print(sorok)

    # sor = [fajl.readline().strip()]
    # print(sor)

    db = int(fajl.readline())
    print(db)

    t = []
    for i in range(db):
        sor = fajl.readline()
        sor2 = sor.strip().split(' ')
        t.append((sor2[0], int(sor2[1]), int(sor2[2])))
    fajl.close()
    return t


def main():
    t = fajlbeolvasas()
    print(t)

main()