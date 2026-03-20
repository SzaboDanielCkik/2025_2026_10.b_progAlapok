toto=[["A diftéria elleni védöoltás a világon elsöként Magyarországon lett kötelezö 1938-ban. A diftéria, azaza a torokgyik a legveszedelmesebb gyermekbetegségek egyike. 1924-ben Gaston Ramon fejlesztette kia hatékony védöoltást ellene",1],
    ["A földrengésbiztos rugós acélszerkezetű házakat Nagy Sándor mérnök dolgozta ki, aki egyébként kiváló sportoló is volt",0],
    ["Az elsö magyar elektronikus számitógépnek köszönhetjük, hgoy biztonsággal átbuszozhatunk az Erzsébet hidon. Az M-3 kábelhiddal kapcsoaltos statikai programja ugyanis kimutatott egy eltérést, amitöl a hid a Dunába roskadt volna",1],
    ["A magyar Novotrade játékfejlesztö külföldi kapcsolataihoz nagyban hozzájárult Steint Róbert, aAngliában élö üzletember. Stein egy budapesti útján figyelt fel egy szovjet játékra a Számitástechnikai Koordinációs Intézet terminálján. Az volt a Tetris",1],
    ["Ma kb. 100 aktiv és ugyanennyi használaton kivüli műhold kerint a Föld körül. Az aktiv műholdak harmada figyeli a földfelszinen és a légkörben lejátszódó természetes és ember által inditott folyamatokat, pl. a globális felmelegedés hatásait",0],
    ["Egy magyar szakember épitette az elsö Amereikában kiállitott automobilt. Stephen Balzer, azaz Balzer István 1894-ben New Yorkban épitett nagy sikerű járművét a Smithsonian Institute múzeumben állitották ki 1899-ben",1]]

def kerdes(sorszam):
    print(toto[sorszam-1][0])
    print("Igaz/vagy hamis az állitás?")
    valasz=int(input("1/0: "))
    return valasz

def eldont(adat,sorszam):
    if adat==toto[sorszam-1][1]:
        print("Helyes válasz")
    else:
        print("Helytelen válasz")

#Kérjen be a felhasználótól egy 1 és 6 közé esö számot!
jatek=True
while (jatek):
    sorszam=0
    while (sorszam<1 or sorszam>6):
        sorszam=int(input("Kérdés sorszáma: "))

    valasz=kerdes(sorszam)
    eldont(valasz,sorszam)
    kilep=input("Ki szeretne lépni [I/N]")
    jatek=kilep=="N"

#Jelenitse meg a kész függvény, eljárás segitségével a sorszámnak megfelelö kérdést


#Jelenitse meg a kész függvény, eljárás segitségével a bekért sorszámnak megfelelöen
#hogy a válasz helyes, vagy helytelen
