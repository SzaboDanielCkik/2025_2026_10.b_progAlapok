
def fajlbeolvasas():
    f = open("txt adatok/resztvevok.txt","r",encoding="utf-8")
    elsoSor = f.readline()
    sorok = f.readlines()
    t = []
    for sor in sorok:
        st = sor.strip().split(';')
        t.append((st[0], st[1],st[2],int(st[3]),st[4]))

    f.close()
    return t, elsoSor

def feladat(t,allat):
    db = 0
    for i in range(len(t)):
        if(t[i][4] == allat):
            db += 1
    return db

def main():
    t,elsosor = fajlbeolvasas()
    #print(t)
    es = elsosor.strip().split(";")
    print(feladat(t,es[1]),"db")
main()