def harga_tiket_bioskop(usia, waktu):
    if usia < 12:
        harga_awal = 25000
    elif usia >= 12 and usia <= 60:
        harga_awal = 50000
    else:
        harga_awal = 20000

    if waktu < 12:
        diskon = 0.10
    elif waktu > 18 :
        diskon = 0.05
    else:
        diskon = 0

    harga_diskon = harga_awal - (harga_awal * diskon)
    return harga_diskon

print("Program Menghitung Harga Tiket Bioskop")
print("=" * 55)
usia= int(input("Masukkan usia Anda: "))
waktu = int(input("Masukkan waktu pemesana (dalam format 24 jam misal 10:00 itu 10): "))
print("Harga tiket Anda adalah:", harga_tiket_bioskop(usia, waktu))