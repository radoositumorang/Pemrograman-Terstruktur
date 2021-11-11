buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
namabuah = input("masukkan nama buah yang ingin dibeli : ")
jumlahpesanan = int(input("berapa kg :"))
harga = int(buah[namabuah]) * jumlahpesanan
if namabuah in buah:
    print("Nama buah yang dibeli :", namabuah)
    print("Berapa Kg             :", jumlahpesanan)
    print("_____________________")
    print("total harga           :", harga)
else:
    print("format salah")
