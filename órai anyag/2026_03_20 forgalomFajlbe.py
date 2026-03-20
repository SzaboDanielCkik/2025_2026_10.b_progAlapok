
def fajlbeolvasas():
    f = open("txt adatok/forgalom.txt")
    elsoSor = f.readline()
    sorok = f.readlines()
    t = []
    for sor in sorok:
        st = sor.strip().split(' ')
        t.append((int(st[0]),int(st[1]),int(st[2]), int(st[3]),st[4]))
    #print(t)
    f.close()
    return t, elsoSor


def main():
    # adatok = fajlbeolvasas()
    # t = adatok[0]
    # elsoSor = adatok[1]
    t, elsoSor = fajlbeolvasas()
    

main()