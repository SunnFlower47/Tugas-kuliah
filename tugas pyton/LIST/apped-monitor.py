# Data awal
barang = ["Laptop", "HP", "Headphone", "Mouse", "Keyboard"]
stok = [10, 20, 15, 25, 30]

# a. Tambahkan barang baru "Monitor" dengan stok awal 12
barang.append("Monitor")
stok.append(12)

# b. Hapus barang "Mouse" dari daftar barang dan stoknya
index_mouse = barang.index("Mouse")  # Cari indeks barang "Mouse"
barang.pop(index_mouse)  # Hapus barang
stok.pop(index_mouse)    # Hapus stok yang sesuai

# c. Perbarui stok untuk barang "Keyboard" menjadi 40
index_keyboard = barang.index("Keyboard")  # Cari indeks barang "Keyboard"
stok[index_keyboard] = 40  # Perbarui stok

# d. Hitung total stok semua barang
total_stok = sum(stok)

# Cetak hasil
print("Daftar barang:", barang)
print("Daftar stok:", stok)
print("Total stok semua barang:", total_stok)
