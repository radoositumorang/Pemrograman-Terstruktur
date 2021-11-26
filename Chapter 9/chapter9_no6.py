data = [{'nim': 'A01', 'nama': 'Agustina', 'mid': 50, 'uas': 80},
        {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
        {'nim': 'A03', 'nama': 'Chicha', 'mid': 100, 'uas': 50},
        {'nim': 'A04', 'nama': 'Donna', 'mid': 20, 'uas': 100},
        {'nim': 'A05', 'nama': 'Fatimah', 'mid': 70, 'uas': 100}]
print("="*80)
print("NIM".ljust(10), "Nama".ljust(15), "N.MID".ljust(15),
      "N.UAS".ljust(15), "N.AKHIR".ljust(15), "STATUS".ljust(15))
print("-"*80)

for data in data:
    print(data['nim'].ljust(5), end='')
    print(data['nama'].rjust(12), end='')
    print(str(data['mid']).rjust(15), end='')
    print(str(data['uas']).rjust(15))
    Na = (data['mid'] + (2 * data['uas'])) // 3
    status = 'LULUS'

    if (Na < 60):
        status = 'Tidak Lulus'
    print(str(round(Na)).rjust(65), status.rjust(16))

print('='*80)
