import random
# lebegőpontos - float - tört
a = 1.25
b = float(input("adjon meg egy tizedes törtet: "))
print(b*4)

# generáljon ki [1,10[ közötti tört számot 2 tizedesjegyre
# pl. 1.36, 2.30

#c = random.randint(100,999)/100
c = random.random() # [0,1[
print(round(c,2))
# HF befejezni

# Szövegkezelés 
szoveg = input("adjon meg egy szöveget: ")
print(szoveg)
print("szöveg hossza: ",len(szoveg)),
print("első karakger",szoveg[0])
# szöveg karakterekből épül fel
# szöveg = karakter lánc
karakter = szoveg[0]
kod = ord(szoveg[0])
print(kod)
ujkod = kod + 1
ujkarakter = chr(ujkod)
print(ujkarakter)

a = chr(random.randint(97,122))
b = chr(random.randint(97,122))
c = chr(random.randint(97,122))
print(a,b,c)

# Kérje a felhasználó keresznevét! Generáljon neki egy jelszót, az első 3 karakterének ascii kódjának szorzatát! Ha nincs a név 3 jegyű, akkor kettő esetén a hossz érték legyen a szorzat 3. taja 1 esetén pedig a szám köbe legyen.
# Alma - 65 * 108 * 109 
# Co - 67 * 111 * 2
# G - 71 * 71 *71 