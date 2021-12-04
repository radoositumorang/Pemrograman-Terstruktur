myFile = open("D:/hitung.txt", "r")
ganjil = 0
genap = 0

for data in myFile:
    if (int(data) % 2 == 0):
        ganjil += 1
    else:
        genap += 1

print("Banyaknya bilangan genap :", genap)
print("Banyaknya bilangan ganjil :", ganjil)
