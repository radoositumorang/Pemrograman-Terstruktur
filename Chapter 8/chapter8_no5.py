def kuadrat(bil):
    if(isinstance(bil, list)):
        for i in range(len(bil)):
            bil[i] **= 2
        return bil
    return False


def getlistdariuser():
    loop = 0
    data = []
    while loop < 5:
        bilangan = int(input("masukkan bilangan bulat:"))
        data.append(bilangan)
        loop += 1

    return data


datalist = getlistdariuser()

if(datalist):
    print("hasil kuadratnya adalah :", datalist)
    result = kuadrat(datalist)
    print(result)
