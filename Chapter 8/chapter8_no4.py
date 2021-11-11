print("Menu :")
print("A. Tambah data sayur")
print("B. Hapus data sayur")
print("C. Tampilkan Data Sayur")

datasayur = ['bayam', 'kangkung', 'wortel', 'selada']
pilih = str(input("masukkkan pilihan anda : "))
if pilih == "A":
    print("Pilihan anda adalah Tambah data sayur")
    datasayur.append(
        input("silahkan masukkan nama sayur yang ingin ditambahkan :"))
    print("data sekarang :", datasayur)
elif pilih == "B":
    try:
        print("Pilihan anda adalah Hapus data sayur")
        datasayur.remove(
            input("silahkan masukkan nama sayur yang ingin dihapus :"))
        print("data sekarang :", datasayur)
    except ValueError:
        print("Data tidak ditemukan")
elif pilih == "C":
    print("Pilihan anda adalah Tampilkan Data Sayur")
    print("Data sayur saat ini : ", datasayur)
