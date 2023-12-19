while True:
    bulan = input("Masukkan nama bulan (atau ketik 'keluar' untuk berhenti): ").lower()
    if bulan == 'keluar':
        break
    elif bulan in ['januari', 'maret', 'mei', 'juli', 'agustus', 'oktober', 'desember']:
        hari = 31
    elif bulan in ['april', 'juni', 'september', 'november']:
        hari = 30
    elif bulan == 'februari':
        hari = 28
    else:
        print("Nama bulan tidak valid.")
        continue

    print(f"Bulan {bulan.capitalize()} memiliki {hari} hari.")