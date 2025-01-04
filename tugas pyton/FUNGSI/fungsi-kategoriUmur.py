def tentukan_kategori_usia(umur):
    if 0 <= umur <= 2:
        return "bayi"
    elif 3 <= umur <= 12:
        return "anak-anak"
    elif 13 <= umur <= 17:
        return "remaja"
    elif 18 <= umur <= 64:
        return "dewasa"
    else:
        return "lansia"

print("Program Menghitung Kategori Usia")
print("=" * 55)
while True:
    try:
        umur = int(input("Masukkan umur Anda: "))
        if umur < 0:
            print("Umur tidak boleh negatif. Silakan masukkan ulang.")
            continue
        break
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")
kategori = tentukan_kategori_usia(umur)
print(f"Kategori usia anda adalah: {kategori}")
