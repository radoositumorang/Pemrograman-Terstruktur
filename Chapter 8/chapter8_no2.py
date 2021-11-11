

def datastat(x):
    if(isinstance(x, list)):
        tupleX = tuple(x)
        a = sum(tupleX) / len(tupleX)
        b = max(tupleX)
        c = min(tupleX)

        return[a, b, c]


def dapatdatadariuser():
    loop = 0
    data = []
    while loop < 5:
        bilangan = int(input("masukkan bilangan bulat:"))
        data.append(bilangan)
        loop += 1

    return data


datalist = dapatdatadariuser()
if(datalist):
    hasil = datastat(datalist)
    print("Rata-Ratanya adalah {0} : {1}" .format(datalist, hasil[0]))
    print("nilai tertingginya adalah{0} : {1}" .format(datalist, hasil[1]))
    print("Nilai terendahnya adalah {0} : {1}" .format(datalist, hasil[2]))
