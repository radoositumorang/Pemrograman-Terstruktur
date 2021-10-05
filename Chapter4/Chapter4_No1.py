masuk=int(input("Masukkan Jam Masuk = "))
keluar=int(input("Masukkan Jam Keluar ="))
lama=keluar-masuk
payment=2000
print("Lama Parkir = ", lama, "jam")
if lama <=1:
    satu_jam_pertama=payment
    print("Biaya Parkir = Rp", satu_jam_pertama)
elif lama <10:
    biaya_selanjutnya = (lama-1)*1000+payment
    print("Biaya Parkir =  Rp", biaya_selanjutnya)
elif lama >= 10:
    print("Biaya Parkir =  Rp", 10000)
else:
    print("nul")

