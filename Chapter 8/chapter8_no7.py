def buahyangpalingmahal(data):
    listdata = list(data.values())
    listdata.sort(reverse=True)
    for x, y in data.items():
        if(listdata[0] == y):
            return x
    return False


buah = {'apel': 5000, 'jeruk': 8500, 'mangga': 7800, 'duku': 6500}
hasil = buahyangpalingmahal(buah)
if(hasil):
    print("buah yang paling mahal adalah :", hasil)
