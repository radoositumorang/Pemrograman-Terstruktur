def rataratabuah(data):
    tupleData = tuple(data.values())
    tambah = sum(tupleData)
    hitung = len(tupleData)
    return tambah/hitung


buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
hasil = rataratabuah(buah)
if(hasil):
    print("rata rata keseluruhannya adalah :", hasil)
