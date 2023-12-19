from buku import Buku

class Perpustakaan:
    def __init__(self):
        self.koleksi = []

    def tambahkan_buku(self, buku):
        self.koleksi.append(buku)

    def tampilkan_koleksi(self):
        for buku in self.koleksi:
            print(buku.tampilkan_info())