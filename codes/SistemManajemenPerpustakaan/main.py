from perpustakaan import Perpustakaan
from buku import Buku

perpus = Perpustakaan()
buku1 = Buku("Harry Potter", "J.K. Rowling")
buku2 = Buku("The Hobbit", "J.R.R. Tolkien")

perpus.tambahkan_buku(buku1)
perpus.tambahkan_buku(buku2)
perpus.tampilkan_koleksi()