def centimeterben(m,dm,cm):
    return int(m)*100+int(dm)*10+int(cm)
        #return int(m+dm+cm)

def sztringben(cm):
    m=cm//100
    dm=(cm%100)//10
    uj_cm=cm%10
    #uj_cm=str(cm)[len(str(cm))-1]
    #dm=str(cm)[len(str(cm))-2]
    #m=str(cm)[len(str(cm))-2]
    return f"{m}:{dm}:{uj_cm}"

def vizsgal(m,dm,cm):
    jo=True
    if m!="0" and m[0]==0:
        jo=False
    if str(int(dm))==dm and int(dm)>=10:
        jo=False
    if str(int(cm))==cm and int(cm)>=10:
        jo=False
    if jo:
        return f"{m}:{dm}:{cm}"
    else:
        return f"Nem megfelelő bemenet"
    
def feltolt():
    t=[]
    f=open("csigalimpia.txt","r",encoding="utf-8")
    osszessor=f.readlines()
    for i in range(len(osszessor)):
        adatok=osszessor[i].strip().split(";")
        t.append((int(adatok[0]),adatok[1],adatok[2],int(adatok[3]),int(adatok[4]),int(adatok[5])))

    f.close()
    return t

def kiiras(t):
    for i in range(len(t)):
        print(f"{t[i][0]},{t[i][1]},{t[i][2]},{t[i][3]},{t[i][4]},{t[i][5]}")

def maximumkivalasztas(t):
    maxi=0
    for i in range(1,len(t),1):
        if centimeterben(t[i][3],t[i][4],t[i][5])>centimeterben(t[maxi][3],t[maxi][4],t[maxi][5]):
            maxi=i
    return maxi

def atlagkivalogat(t):
    osszeg=0
    db=0
    for i in range(len(t)):
        if t[i][2]=="CVSE":
            osszeg+=centimeterben(t[i][3],t[i][4],t[i][5])
            db+=1
    return osszeg/db


def main():

    print("1. feladat")
    m=input("Meter: ")
    dm=input("Decimeter: ")
    cm=input("Centimeter: ")
    print(vizsgal(m,dm,cm))
    print(centimeterben(m,dm,cm))
#print(sztringben(centimeterben(m,dm,cm)))
    print("2. feladat")
    print(f"A beolvasott adatok centimeterben:{centimeterben(m,dm,cm)}")
    print(vizsgal(m,dm,cm))
    print(centimeterben(m,dm,cm))
    print("3. feladat")
    t=feltolt()
    i=maximumkivalasztas(t)
    print(f" A versenyt nyerte:{t[i][1]}--{t[i][3]}--{t[i][4]}--{t[i][5]}")
    print(f" A hazaiak atlagos eredmenye: {sztringben(atlagkivalogat(t))}")
main()