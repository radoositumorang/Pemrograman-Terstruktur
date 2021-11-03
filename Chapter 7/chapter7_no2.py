try:
    masukkannamafile = str(input("masukkan nama file :"))
    file = open(f'D:/{masukkannamafile}.txt', "a")
except OSError:
    print('inputan salah')


while True:

    tambahfile = str(input("masukkan teks yang ingin ditambahkan :"))
    isifile = file.write(tambahfile)
    ulang = str(input("mau lagi ?(y/n) :"))
    if ulang == "y":
        print(end='')
    elif ulang == "n":
        file.close()
        break
    else:
        print("data tidak valid")
        break
