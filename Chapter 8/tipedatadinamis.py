a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]
print("Data Awal a:", a)
print("Data Awal b:", b)
print("="*60)

a.insert(3, 10)
b.insert(2, 15)
print("hasil setelah disisipkan nilai 10 ke indeks 3", a)
print("hasil setelah disisipkan nilai 15 ke indeks 2", b)
print("="*60)

a.append(4)
b.append(8)
print("hasil list a setelah disisipkan angka 4", a)
print("hasil list a setelah disisipkan angka 8", b)
print("="*60)

a.sort()
b.sort()
print("hasil list a disorting secara ascending", a)
print("hasil list b disorting secara ascending", b)
print("="*60)

c = a[:8]
d = b[2:10]
print("list c yang merupakan sublist dari a(indeks 0-7)", c)
print("list c yang merupakan sublist dari b(indeks 2-9)", d)
print("="*60)

e = []
for i in range(len(d)):
    e += [c[i] + d[i]]
print('hasil list e yang merupakan penjumlahan dari setiap elemen list c dan d', e)
e = tuple(e)
print('hasil list e yang dijadikan tuple', e)
print('='*60)

min = min(e)
max = max(e)
sum = sum(e)

print("hasil min dari tuple", min)
print("hasil max dari tuple", max)
print("hasil sum dari tuple", sum)
print("="*60)

myString = "python adalah bahasa pemrograman yang menyenangkan"
myString = set(myString)

print("variabel myString", myString)
print("karakter hurug yang menyusun myString", myString)
print("="*60)

myStringSetList = list(myString)
print("bentuk list myString", myStringSetList)
myStringSetList.sort()
print("bentuk list myString setelah di sorting ascending", myStringSetList)
