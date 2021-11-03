masukkannamafile = str(input("masukkan nama file :"))
file = open(f'D:/{masukkannamafile}.txt', "r")
print("isi file adalah ", file.read())
