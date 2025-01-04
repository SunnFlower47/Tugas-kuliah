inventaris = {
    "B001": {"nama": "Laptop", "kategori": "Elektronik", "stok": 10},
    "B002": {"nama": "HP", "kategori": "Elektronik", "stok": 15},
    "B003": {"nama": "Meja", "kategori": "Furniture", "stok": 8},
    "B004": {"nama": "Kursi", "kategori": "Furniture", "stok": 20},
    "B005": {"nama": "Mouse", "kategori": "Elektronik", "stok": 25}
}

# a. Tampilkan semua data barang dalam format: Kode: [Nama] - [Kategori] (Stok: [Jumlah]).
print("Data Barang:")
for id_barang, detail in inventaris.items():
    print(f"kode:{id_barang}: [{detail['nama']}] - [{detail['kategori']}] (Stok: {detail['stok']})")

# b. Tambahkan barang baru dengan kode B006, nama Keyboard, kategori Elektronik, dan stok 12
inventaris["B006"] = {"nama": "Keyboard", "kategori": "Elektronik", "stok": 12}
print("\nBarang setelah penambahan:")
for id_barang, detail in inventaris.items():
    print(f"kode:{id_barang}: [{detail['nama']}] - [{detail['kategori']}] (Stok: {detail['stok']})")

#c. Perbarui stok barang dengan kode B002 menjadi 18.
inventaris["B002"]["stok"] = 18
print("\nBarang setelah perubahan stok:")
for id_barang, detail in inventaris.items():
    print(f"kode:{id_barang}: [{detail['nama']}] - [{detail['kategori']}] (Stok: {detail['stok']})")

# d. Hapus barang dengan kode B003.
del inventaris["B003"]
print("\nBarang setelah penghapusan:")
for id_barang, detail in inventaris.items():
    print(f"kode:{id_barang}: [{detail['nama']}] - [{detail['kategori']}] (Stok: {detail['stok']})")

# e. Tampilkan semua barang dalam kategori Elektronik.
print("\nBarang dalam kategori Elektronik:")
for id_barang, detail in inventaris.items():
    if detail["kategori"] == "Elektronik":
        print(f"kode:{id_barang}: [{detail['nama']}] - [{detail['kategori']}] (Stok: {detail['stok']})")

# f. Hitung total stok semua barang di gudang.
total_stok = sum(detail["stok"] for detail in inventaris.values())
print(f"\nTotal stok semua barang: {total_stok}")
