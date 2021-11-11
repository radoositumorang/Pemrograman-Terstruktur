print("Menu :")
print("A. Tambah data Buah")
print("B. Beli Buah")
databuah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
pilih = str(input("masukkkan pilihan anda : "))
if pilih == "A":
    buahbaru = input("masukkan nama buah :")
    if(buahbaru in databuah):
        print("Buah sudah ada")
    else:
        while True:
            hargabaru = int(input("masukkan harga satuan :"))
            databuah[buahbaru] = hargabaru
            print("Data buah sekarang : ", databuah)
            break
elif pilih == "B":
    total = 0
    while True:
        namabuah = input("masukkan nama buah yang ingin dibeli : ")
        jumlahpesanan = int(input("berapa kg :"))
        total += (databuah[namabuah] * jumlahpesanan)
        if namabuah in databuah:
            print("Nama buah yang dibeli :", namabuah)
            print("Berapa Kg             :", jumlahpesanan)
        ulang = str(input("beli buah yang lain ?(y/n) :"))
        if ulang == "y":
            print(end='')
        elif ulang == "n":
            print("total harga           :", total)
            break
