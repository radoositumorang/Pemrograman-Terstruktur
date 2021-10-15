Nilaibahasaindonesia = int(input("Masukkan Nilai Bahasa Indonesia : "))
NilaiIpa = int(input("Masukkan Nilai IPA :"))
NilaiMatematika = int(input("Masukkan Nilai Matematika : "))
if (NilaiMatematika > 70) and (NilaiIpa > 60) and (Nilaibahasaindonesia > 60):
    print("Status kelulusan : Lulus")
else:
    print("Status Kelulusan : Tidak Lulus")
