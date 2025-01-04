def hitung_gaji_pokok(jam_kerja, gaji_per_jam):
    return jam_kerja * gaji_per_jam

def hitung_gaji_lembur(jam_kerja, gaji_per_jam):
    if jam_kerja <= 40:
        return 0
    jam_lembur = jam_kerja - 40
    return jam_lembur * gaji_per_jam * 1.5

def hitung_total_gaji(gaji_pokok, gaji_lembur):
    return gaji_pokok + gaji_lembur

print ("Program Menghitung Gaji Karyawan")
print("=" * 50)
while True:
    try:
        jam_kerja = int(input("Masukkan jumlah jam kerja: "))
        if jam_kerja < 0:
            print("Jam kerja tidak boleh kurang dari nol/negatif.")
            continue
        break
    except ValueError:
        print("Masukkan angka yang valid.")

gaji_per_jam = 3000
gaji_pokok = hitung_gaji_pokok(min(jam_kerja, 40), gaji_per_jam)
gaji_lembur = hitung_gaji_lembur(jam_kerja, gaji_per_jam)
total_gaji = hitung_total_gaji(gaji_pokok, gaji_lembur)

print("\n--- Rincian Perhitungan Gaji Karyawan ---")
print(f"Gaji pokok = Rp. {gaji_pokok:.2f}")
print(f"Gaji lembur = Rp. {gaji_lembur:.2f}")
print(f"Total gaji = Rp. {total_gaji:.2f}")
