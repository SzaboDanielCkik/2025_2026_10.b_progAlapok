# Egy szövegben hány darab szóköz van?

szoveg = "Géza kék az ég"
print(szoveg)
db = 0

for karakter in szoveg:
    if(karakter == " "):
        db += 1

print(db, "db szóköz van a szövegben.")

# Adja meg, hogy a szövegben van-e cs betű (két karakter egymás mellett)
# pl. alma, kacsa, filc

sz = input("Adjon meg egy szöveget: ")
index = 0
while(index<len(sz)-1 and not(sz[index] == "c" and sz[index+1] == "s")):
#while(index<len(sz)-1 and (sz[index] != "c" or sz[index+1] != "s")):
    index += 1

print(index)
if(index < len(sz)-1):
    print("Van benne cs")
else:
    print("Nincs benne cs")

# De Morgan azonosság