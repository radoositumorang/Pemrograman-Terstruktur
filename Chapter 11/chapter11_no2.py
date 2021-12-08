from datetime import *
myfile = open("D:/datamhs.txt", "a")

while True:
    nim = input("Masukkan NIM :")
    nama = input("Masukkan Nama :")
    judulbuku = input("Masukkan Judul Buku :")
    skrg = datetime.date(datetime.now())
    wa = str(str(skrg.year) + "-" + str(skrg.month) + "-" + str(skrg.day))
    wp = str(skrg + timedelta(days=7))

    myString = nim+"|"+nama+"|"+judulbuku+"|"+wa+"|"+wp + "\n"
    myfile.write(myString)

    Q = input("Mau lagi? (y/n) ?")

    if Q in ("N", "n"):
        break
myfile.close()
