# Meminta input suhu ruangan dari pengguna
suhu = float(input("Masukkan suhu ruangan (°C): "))

# Menentukan kategori suhu ruangan
if suhu <= 18:
    kategori = "Dingin"
elif 19 <= suhu <= 29:
    kategori = "Normal"
else:
    kategori = "Panas"

# Menampilkan hasil kategori suhu ruangan dari inputan pengguna
print("\n=== Menampilkan Kategori Suhu Ruangan ===")
print(f"Suhu ruangan: {suhu}°C")
print(f"Kategori suhu: {kategori}")
