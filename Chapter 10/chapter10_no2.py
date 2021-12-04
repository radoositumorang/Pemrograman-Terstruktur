myfile = open("D:/datamhs.txt", "a")

while True:
    nim = input("Masukkan NIM :")
    nama = input("Masukkan Nama :")
    tinggibadan = input("Masukkan tinggi badan :")

    myString = nim+"|"+nama+"|"+tinggibadan+"\n"
    myfile.write(myString)

    Q = input("Mau lagi? (y/n) ?")

    if Q in ("N", "n"):
        break
myfile.close()
