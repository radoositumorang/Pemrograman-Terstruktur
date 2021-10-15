Nilaibahasaindonesia = int(input("Masukkan Nilai Bahasa Indonesia : "))
NilaiIpa = int(input("Masukkan Nilai IPA :"))
NilaiMatematika = int(input("Masukkan Nilai Matematika : "))
if (NilaiMatematika > 70) and (NilaiIpa > 60) and (Nilaibahasaindonesia > 60):
    print("Lulus")
elif (NilaiMatematika < 0) or (NilaiIpa < 0) or (Nilaibahasaindonesia < 0):
    print("Input tidak valid")
else:
    print("Tidak Lulus")
