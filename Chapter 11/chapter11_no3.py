from datetime import *


def terlambat(x):
    skrg = datetime.date(datetime.now())
    wn = datetime.strptime(x, "%Y-%m-%d").date()
    return int((wn-skrg).days)


myfile = open("D:/datamhs.txt", "r")
cari = input("Masukkan Kode :")

hasil = False
for data in myfile:
    data1 = data.split("|").copy()
    kode = data.split("|")[0]
    if (kode == cari):
        hasil = data1
        break
if (hasil):
    makspinjam = data1[4].rstrip('\n')
    lambat = terlambat(makspinjam)
    if (lambat <= 0):
        teks = "-"
        denda = "-"
    elif(lambat > 0):
        teks = str(lambat) + "hari"
        denda = "Rp " + str(terlambat*2000)

    print("Data Mahasiswa")
    print("Kode Member                 :", data1[0])
    print("Nama Member                 :", data1[1])
    print("Nama Buku                   :", data1[2])
    print("Tanggal Mulai Peminjaman    :", data1[3])
    print("Tanggal Maks Peminjaman     : ", makspinjam)
    print("Tanggal Pengembalian        : ", datetime.date(datetime.now()))
    print("Terlambat                   : ", teks)
    print("Denda                       : ", denda)
