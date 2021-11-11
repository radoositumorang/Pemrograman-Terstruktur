buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
total = 0
while True:
    namabuah = input("masukkan nama buah yang ingin dibeli : ")
    jumlahpesanan = int(input("berapa kg :"))
    total += (buah[namabuah] * jumlahpesanan)
    if namabuah in buah:
        print("Nama buah yang dibeli :", namabuah)
        print("Berapa Kg             :", jumlahpesanan)
    ulang = str(input("beli buah yang lain ?(y/n) :"))
    if ulang == "y":
        print(end='')
    elif ulang == "n":
        print("total harga           :", total)
        break
