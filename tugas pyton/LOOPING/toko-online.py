# Data pesanan
pesanan = [
    (101, "Laptop", 1, 15000000),
    (102, "HP", 2, 3000000),
    (103, "Headphone", 3, 500000),
    (104, "Keyboard", 4, 250000),
    (105, "Mouse", 5, 100000),
]

# a. Tampilkan semua data pesanan
print("Semua data pesanan:")
for p in pesanan:
    print(p)

# b. Hitung total harga untuk setiap pesanan dan tampilkan hasilnya
print("\nTotal harga untuk setiap pesanan:")
for p in pesanan:
    id_pesanan, nama_barang, jumlah, harga_per_unit = p
    total_harga = jumlah * harga_per_unit
    print(f"ID {id_pesanan} ({nama_barang}): Rp{total_harga}")

# c. Cari pesanan dengan ID 103 dan tampilkan detailnya
id_cari = 103
detail_pesanan = next((p for p in pesanan if p[0] == id_cari), None)
if detail_pesanan:
    print(f"\nDetail pesanan dengan ID {id_cari}: {detail_pesanan}")
else:
    print(f"\nPesanan dengan ID {id_cari} tidak ditemukan.")

# d. Hitung total pendapatan dari semua pesanan
total_pendapatan = sum(jumlah * harga_per_unit for _, _, jumlah, harga_per_unit in pesanan)
print(f"\nTotal pendapatan dari semua pesanan: Rp{total_pendapatan}")
