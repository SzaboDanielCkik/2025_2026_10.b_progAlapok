
def fajlbeovlasas():
    f = open("txt adatok/szeleromu.txt","r",encoding="utf-8")
    elsoSor = f.readline()
    sorok = f.readlines()
    #print(sorok)
    t = []
    for sor in sorok:
        st = sor.strip().split(";")
        t.append((st[0], st[1],st[2], int(st[3]), int(st[4]), int(st[5])))
    f.close()
    #print(t)
    return t

def hanyDbSzeleromu(t, ev):
    db = 0
    for i in range(len(t)):
        if(t[i][5] == ev):
            db += t[i][3]
    return db

def main():
    adatok = fajlbeovlasas()
    #1. Írjon egy fv-t, ami megadja, hogy hány darab szélerőmű lett telepítve a bekért évben?

    ev = int(input("Adjon meg egy évet: "))
    db = hanyDbSzeleromu(adatok,ev)
    print(db)


main()