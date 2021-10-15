import random

angka = random.randint(0, 100)

print("Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0 s/d 100. Silakan tebak ya!!!")

tebakan = -1
score = 100
while tebakan != angka:

    tebakan = eval(input("masukkan angka anda :"))

    if tebakan == angka:
        print("Yeeee… Bilangan tebakan anda BENAR ", tebakan)
    elif tebakan > angka:
        print("Hehehe… Bilangan tebakan anda terlalu besar")
    else:
        print("Hehehe… Bilangan tebakan anda terlalu kecil")

    if tebakan == angka:
        score += 0
    elif tebakan > angka:
        score -= 2
    else:
        score -= 2

print("skor anda adalah", score)
