import statistics


def jumlah(*myData):
    sum = +0

    for data in myData:
        sum += data

    jumlah1 = sum
    print('jumlahnya :', jumlah1)


jumlah(5, 10, 4, 9, 30, 16, 2, 11)
jumlah(81, 98, 12, 83, 45, 77, 69, 30, 56)


def avarage(*myData):
    sum = 0
    i = 0

    for data in myData:
        sum += data
        i += 1

    avarage1 = sum/i
    print('avarage :', avarage1)


avarage(5, 10, 4, 9, 30, 16, 2, 11)
avarage(81, 98, 12, 83, 45, 77, 69, 30, 56)


def nilaimaksimal(*myData):

    for data in myData:
        max(myData) == data

    nilaimaksimal1 = max(myData)
    print('nilai maksimal :', nilaimaksimal1)


nilaimaksimal(5, 10, 4, 9, 30, 16, 2, 11)
nilaimaksimal(81, 98, 12, 83, 45, 77, 69, 30, 56)


def nilaiminimum(*myData):

    for data in myData:
        min(myData) == data

    nilaiminimum1 = min(myData)
    print('nilai minimum :', nilaiminimum1)


nilaiminimum(5, 10, 4, 9, 30, 16, 2, 11)
nilaiminimum(81, 98, 12, 83, 45, 77, 69, 30, 56)
