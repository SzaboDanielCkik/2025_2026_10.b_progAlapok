# Házi feladat
# Jancsi és Juliska elmennek minden nap gombát gyűjteni. 14 napig folyamatosan gyűjtik majd összevetik az adatokat.
# Szimuláld a gyűjtést. kosarak nagysága [2,9] közötti lebegőpontos (tört szám, 2 tizedesjegy pontossággal.) Mindkettőjük adatát külön listában tárold! 
# Van-e bármelyikőjüknél 8.5 kg-nál több? Ha igen kinél?
# Van-e olyan közöttük, aki 4.9-5.1 közötti kosarat gyűjtött!
# Max, min, átlag,  db (2.1-2,4) között?

def vaneKetjegyuListaban(lista):
    i = 0
    # ciklus amíg (i<hossz(lista) és NEM Ttul(lista[i]))
    while(i<len(lista) and not (lista[i]>=10 and lista[i]<=99)):
        i += 1
    # c.v.
    # vane = i < hossz(lista)
    vane = i < len(lista)
    # vissza: vane
    return vane

def main():
    szamok = [2,5,6,3,7,1,9,1,2]
    print(szamok)
    # van-e kétjegyű szám a listában?
    vaneKetjegyu = vaneKetjegyuListaban(szamok)
    print(vaneKetjegyu)

main()