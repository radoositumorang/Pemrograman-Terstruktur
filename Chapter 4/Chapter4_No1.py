print("Program Menghitung uang parkir otomatis")
print("---------------------------------------")
jammasuk1=int(input("Masukkan Jam Masuk = "))
menitmasuk1=int(input("masukkan menit masuk ="))
menitmasuk1=menitmasuk1/60
totalmasuk=jammasuk1+menitmasuk1
jamkeluar2=int(input("Masukkan Jam Keluar ="))
menitkeluar2=int(input("masukkan menit keluar ="))
menitkeluar2=menitkeluar2/60
totalkeluar=jamkeluar2+menitkeluar2
lama=(totalkeluar)-(totalmasuk)
payment=200000
print("Lama Parkir = ", lama, "jam")
if lama ==12:
    Duabelas_jam_pertama=payment
    print("Biaya Parkir = Rp", Duabelas_jam_pertama)
elif lama >12:
    biaya_selanjutnya = (lama-12)*10000+payment
    print("Biaya Parkir =  Rp", biaya_selanjutnya)
elif lama > 13:
    biaya_lanjutan = (lama-12)*10000+payment
    print("Biaya Parkir =  Rp", biaya_lanjutan)
else:
    print("nul")