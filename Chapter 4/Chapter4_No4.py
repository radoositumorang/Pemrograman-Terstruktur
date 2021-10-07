# menghitung jarak A ke B dan B ke C
jarakAkeB = float(input("masukkan jarak A ke B :"))
rataratakecepatanAkeB = float(input("masukkan rata rata kecepatan:"))
waktutempuhAkeB = jarakAkeB/rataratakecepatanAkeB
print("waktu tempuh adalah :", round(jarakAkeB//rataratakecepatanAkeB), "jam",
      round((jarakAkeB/rataratakecepatanAkeB-jarakAkeB//rataratakecepatanAkeB)*60), "Menit")

jarakBkeC = float(input("masukkan jarak B ke C :"))
rataratakecepatanBkeC = float(input("masukkan rata rata kecepatan:"))
waktutempuhBkeC = jarakBkeC/rataratakecepatanBkeC
print("waktu tempuh adalah :", round(jarakBkeC//rataratakecepatanBkeC), "jam",
      round((jarakBkeC/rataratakecepatanBkeC-jarakBkeC//rataratakecepatanBkeC)*60), "Menit")

# Jam Sampai di C setelah ada istirahat 45 Menit di B
jamberangkat = int(input("Masukkan Jam berangkat = "))
menitberangkat = int(input("Masukkan menit berangkat ="))
menitberangkat = menitberangkat/60
jamsampaiAmenujuC = int(11)
menitsampaiAmenujuC = 60
print("input jam istirahat di B")
jamistirahat = int(input("Masukkan jam istirahat ="))
menitistirahat = int(input("Masukkan menit istirahat ="))
print("Jam sampai di C", int(jamistirahat+1 + jamsampaiAmenujuC))
print("menit sampai di C", int(menitsampaiAmenujuC+20-menitistirahat))
