loop = 0
data = []
while loop < 5:
    bilangan = int(input("masukkan bilangan bulat:"))
    data.append(bilangan)
    loop += 1

data.sort(reverse=True)
print("Susunan data dari yang terbesar hingga terkecil :", data)
