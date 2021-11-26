data = [{'nim': 'A01', 'nama': 'Agustina', 'mid': 50, 'uas': 80},
        {'nim': 'A02', 'nama': 'Budi', 'mid': 40, 'uas': 90},
        {'nim': 'A03', 'nama': 'Chicha', 'mid': 100, 'uas': 50},
        {'nim': 'A04', 'nama': 'Donna', 'mid': 20, 'uas': 100},
        {'nim': 'A05', 'nama': 'Fatimah', 'mid': 70, 'uas': 100}]
print("="*20)
print("NIM     NamaMHS     MID   UAS   NA   STATUS")
print("-"*20)

for i in range(len(data)):
    print(data[i]['nim'].ljust(5), end='')
    print(data[i]['nama'].ljust(10), end='')
    print(str(data[i]['mid']).rjust(8), end='')
    print(str(data[i]['uas']).rjust(8))
