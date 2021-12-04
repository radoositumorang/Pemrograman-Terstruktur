myfile = open("D:/datamhs.txt", "r")
dataMhs = {}

i = 1

for data in myfile:
    datasatu = {}
    datapusat = data.split("|")
    datasatu["nim"] = datapusat[0]
    datasatu["nama"] = datapusat[1]
    datasatu["tinggibadan"] = datapusat[2]

    dataMhs[i] = datasatu
    i += 1

print(dataMhs)
