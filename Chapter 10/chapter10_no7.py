
myfile = open('D:/acakkarakter.txt', 'r')
caesar = int(input("masukan n : "))
listA = list(myfile.readline())

result = ""
for charTeks in listA:
    if(charTeks.isalpha()):
        hurufAscii = ord(charTeks)
        indexAplha = hurufAscii - ord("A")
        newIndex = (indexAplha - caesar) % 26
        newCaesar = newIndex + ord("A")
        newChar = chr(newCaesar)
        result += newChar
    else:
        result += charTeks


hasil = open('D:/hasilacakkarakter.txt', 'w')
hasil.write(result)
hasil.close()
