myfile = open("D:/angka.txt", "r")
text = ""
for data in myfile:
    angka = data.split('|')
    angka = angka
    hasil = int(angka[0]) + int(angka[1].rstrip("\n"))
    text += str(hasil) + "\n"

filehasil = open("D:/hasil.txt", "w")
filehasil.write(text)
filehasil.close()
