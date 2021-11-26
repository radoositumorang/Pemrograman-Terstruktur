def ubahhuruf(teks, a, b):
    listteks = list(teks)

    for char in listteks:
        if char == a:
            b == a
    hasil = teks.replace(a, b)
    print("hasilnya adalah :", hasil)


ubahhuruf("MATEMATIKA", "T", "S")
