from datetime import datetime

catatan = input("Masukkan catatan hari ini: ")
waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open('catatan_harian.txt', 'a') as file:
    file.write(f"{waktu_sekarang}: {catatan}\n")

print("Catatan berhasil ditambahkan.")