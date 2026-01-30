# Házi feladat
# Jancsi és Juliska elmennek minden nap gombát gyűjteni. 14 napig folyamatosan gyűjtik majd összevetik az adatokat.
# Szimuláld a gyűjtést. kosarak nagysága [2,9] közötti lebegőpontos (tört szám, 2 tizedesjegy pontossággal.) Mindkettőjük adatát külön listában tárold! 
# Van-e bármelyikőjüknél 8.5 kg-nál több? Ha igen kinél?
# Van-e olyan közöttük, aki 4.9-5.1 közötti kosarat gyűjtött!
# Max, min, átlag,  db (2.1-2,4) között?
import random

def listaFeltolt(n):
    lista = []
    for i in range(0,n,1):
        lista.append(random.randint(200,900)/100)
        #lista.append(round(random.random()*7+2,2)) # [0,1]*(9-2)+2
    return lista

def vaneSzamnalNagyobb(szam, lista):
    index = 0
    while(index < len(lista) and not(lista[index] > szam)): 
    # while(index < len(lista) and lista[index] <= szam): 
    # Ttul: lista[index] > szam  NEM Ttul: lista[index] <= szam
        index += 1
    vane = index < len(lista)
    # ha index < len(lista) akkor vane értéke true
    # különben (index >= len(lista)) akkor vane értéke false
    return vane

def vaneKetszamKozott(a,b,lista):
    index = 0
    #while(index < len(lista) and (lista[index] < a or lista[index] < b)):
    while(index < len(lista) and not (lista[index] >= a and lista[index]<=b)):
    # Ttul: lista[index] >= a and lista[index]>=b  
        index += 1
    vane = index < len(lista)
    return vane

def main():
    jancsi = []
    juliska = []
    #db = int(input())
    #db = random.randint(12,96)
    #print(listaFeltolt(14))
    jancsi = listaFeltolt(14)
    juliska = listaFeltolt(14)
    print("Juliska: ", juliska)
    print("Jancsi: ", jancsi)
    vaneJuliska = vaneSzamnalNagyobb(8.5,juliska)
    if(vaneJuliska):
        print("Van Juliskánál 8.5-nél nagyobb")
    else:
        print("Nincs Juliskánál 8.5-nél nagyobb")

    vaneJancsi = vaneSzamnalNagyobb(8.5, jancsi)
    if(vaneJancsi):
        print("Van Jancsinál 8.5-nél nagyobb")
    else:
        print("Nincs Jancsinál 8.5-nél nagyobb")

    vaneJuliskaKozott = vaneKetszamKozott(4.9, 5.1, juliska)
    if(vaneJuliskaKozott):
        print("Julsikának van 4.9 és 5.1 közötti értéke")
    else:
        print("Julsikának nincs 4.9 és 5.1 közötti értéke")

    vaneJancsiKozott = vaneKetszamKozott(4.9, 5.1, jancsi)
    if(vaneJancsiKozott):
        print("Jancsinak van 4.9 és 5.1 közötti értéke")
    else:
        print("Jancsinak nincs 4.9 és 5.1 közötti értéke")

main()