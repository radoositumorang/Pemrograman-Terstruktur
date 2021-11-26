mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']

print("="*80)
print("NIM     NamaMHS               TGL LAHIR               TEMPAT LAHIR")
print("-"*80)

for data in mhs:
    List = data.split(":")
    nim = List[0]
    nama = List[1]

    tglLahir = List[2]
    dataTglLahir = tglLahir.split('-')
    FormatTglLahir = "{0}/{1}/{2}".format(
        dataTglLahir[2], dataTglLahir[1], dataTglLahir[0])

    tempatlahir = List[3]

    print(nim.ljust(5), end='')
    print(nama.ljust(24), end='')
    print(FormatTglLahir.ljust(30), end='')
    print(tempatlahir.ljust(20))

print("-"*80)
