from datetime import datetime, timedelta

tanggal_sekarang = datetime.now()
print("Tanggal saat ini:", tanggal_sekarang.strftime("%Y-%m-%d %H:%M:%S"))

tanggal_target = datetime(2023, 12, 31)
selisih = tanggal_target - tanggal_sekarang
print("Selisih hari hingga akhir tahun:", selisih.days)