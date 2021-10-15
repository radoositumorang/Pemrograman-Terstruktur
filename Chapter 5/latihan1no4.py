kodekaryawan = input("Masukkan kode karyawan :")
namakaryawan = input("Masukkan Nama Karyawan :")
golongan = input("Masukkan golongan : ")

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

print("==========================")
print("STRUK RINCIAN GAJI KARYAWAN")
print("-------------------------")
print("Nama Karyawan :", namakaryawan)
print("Golongan :", golongan)
print("-------------------------")
print("Gaji Pokok :",  gajipokok)
print("Potongan :", persenan, "%", potongan)
print("----------------------------- -")
print("Gaji Bersih :",  gajibershih)
