kodekaryawan = input("Masukkan kode karyawan :")
namakaryawan = input("Masukkan Nama Karyawan :")
golongan = input("Masukkan golongan : ")
status = input("Masukkan Status (1:menikah,2:blm) :")

# potonganpersen
if golongan == "A":
    persenan = 2.5
elif golongan == "B":
    persenan = 2.0
elif golongan == "C":
    persenan = 1.5
else:
    persenan = 1.0


# golongan
if golongan == "A":
    gajipokok = 10000000
elif golongan == "B":
    gajipokok = 8500000
elif golongan == "C":
    gajipokok = 7000000
else:
    gajipokok = 5500000

# potongan
if golongan == "A":
    potongan = 10000000*2.5/100
elif golongan == "B":
    potongan = 8500000*2/100
elif golongan == "C":
    potongan = 7000000*1.5/100
else:
    potongan = 5500000*1/100


# gajibershih
if golongan == "A":
    gajibershih = 10000000 - potongan
elif golongan == "B":
    gajibershih = 8500000 - potongan
elif golongan == "C":
    gajibershih = 7000000 - potongan
else:
    gajibershih = 5500000 - potongan

# status
if status == "menikah":
    jumlahanak = int(input("jumlah anak :"))
else:
    print("belum menikah")


# tunjangansuamiistri
if golongan == "A":
    tunjangansuamiistri = 10000000*10/100
elif golongan == "B":
    tunjangansuamiistri = 8500000*10/100
elif golongan == "C":
    tunjangansuamiistri = 7000000*10/100
else:
    tunjangansuamiistri = 5500000*10/100

# tunjangananak
if golongan == "A":
    tunjangananak = jumlahanak * 10000000*5/100
elif golongan == "B":
    tunjangananak = jumlahanak * 8500000*5/100
elif golongan == "C":
    tunjangananak = jumlahanak*7000000*5/100
else:
    tunjangananak = jumlahanak*5500000*5/100
# rumus
gajikotor = gajipokok+tunjangansuamiistri+tunjangananak
rumus = gajikotor-potongan

print("==============================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("------------------------------")
print("Nama Karyawan :", namakaryawan)
print("Golongan :", golongan)
print("Status Menikah :", status)
print("Jumlah anak :", jumlahanak)
print("-----------------------------")
print("Gaji Pokok :",  gajipokok)
print("Tunjangan istri/suami :", tunjangansuamiistri)
print("Tunjangan Anak :", tunjangananak)
print("----------------------------- +")
print("gajikotor :", gajikotor)
print("Potongan :", persenan, "%", potongan)
print("----------------------------- -")
print("Gaji Bersih :",  rumus)
