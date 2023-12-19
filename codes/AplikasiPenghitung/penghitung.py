def bagi(a, b):
    try:
        hasil = a / b
    except ZeroDivisionError:
        print("Error: Tidak bisa membagi dengan nol")
        return None
    except TypeError:
        print("Error: Pastikan kedua input adalah angka")
        return None
    else:
        return hasil

# Contoh penggunaan
print(bagi(10, 2))  # Harusnya menampilkan 5
print(bagi(10, 0))  # Harusnya menampilkan error pembagian dengan nol
print(bagi("10", 2))  # Harusnya menampilkan error tipe data