myfile = open("D:/datamhs.txt", "a")

while True:
    nim = input("Masukkan NIM :")
    nama = input("Masukkan Nama :")
    alamat = input("Masukkan Alamat :")

    myString = nim+"|"+nama+"|"+alamat+"\n"
    myfile.write(myString)

    Q = input("Mau lagi? (y/n) ?")

    if Q in ("N", "n"):
        break
myfile.close()
