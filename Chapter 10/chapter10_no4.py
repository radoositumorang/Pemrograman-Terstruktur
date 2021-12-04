myfile = open("D:/datamhs.txt", "r")
cari = input("Masukkan Nim yang ingin di cari :")

for data in myfile:
    data1 = data.split("|").copy()
    nim = data.split("|")[0]
    if nim == cari:
        print("Data Mahasiswa")
        print("NIM               :", data1[0])
        print("Nama              :", data1[1])
        print("Tinggi Badan      :", data1[2])
    else:
        ("Data Mahasiswa tidak ditemukan")
