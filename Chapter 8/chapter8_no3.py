loop = 0
data = []
while loop < 5:
    inputnamamahasiswa = input("Nama mahasiswa :")
    data.append(inputnamamahasiswa)
    loop += 1

data.sort()
for inputnamamahasiswa in data:
    print("{0} ({1} karakter)".format(
        inputnamamahasiswa, len(tuple(inputnamamahasiswa))))
