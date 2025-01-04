print('##  Program Python Menghitung umur  ##')
print('Ridwan Andrian (241351144)')
print('=' *54)
print()

from datetime import datetime

def hitung_umur(tanggal_lahir):

    tanggal_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")

    tanggal_sekarang = datetime.now()

    umur = tanggal_sekarang.year - tanggal_lahir.year

    if(tanggal_sekarang.month, tanggal_sekarang.day) < (tanggal_lahir.month, tanggal_lahir.day): umur -= 1

    return umur

tanggal_lahir = input("Masukkan tanggal lahir Anda (YYYY-MM-DD): ")
umur = hitung_umur(tanggal_lahir)

print(f"Umur Anda adalah: {umur} tahun.") 

