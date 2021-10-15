Nilaibahasaindonesia = int(input("Masukkan Nilai Bahasa Indonesia : "))
NilaiIpa = int(input("Masukkan Nilai IPA :"))
NilaiMatematika = int(input("Masukkan Nilai Matematika : "))
sebab1 = str(" Sebab : Nilai matematika Kurang dari 70")
sebab2 = str(" Sebab : Nilai bahasa indonesia Kurang dari 60")
sebab3 = str(" Sebab : Nilai Ipa Kurang dari 60")
if (NilaiMatematika > 70) or (NilaiIpa > 60) or (Nilaibahasaindonesia > 60):
    print("Lulus")
if (NilaiMatematika < 70):
    print("tidak lulus" + sebab1)
if (NilaiIpa < 600):
    print("tidak lulus" + sebab2)
if (Nilaibahasaindonesia < 60):
    print("tidak lulus" + sebab3)
