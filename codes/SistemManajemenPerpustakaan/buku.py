class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def tampilkan_info(self):
        return f"Buku: {self.judul} oleh {self.penulis}"