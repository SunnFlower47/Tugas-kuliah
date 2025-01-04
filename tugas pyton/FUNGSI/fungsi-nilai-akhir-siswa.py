def hitung_nilai_akhir(nilai_ujian, nilai_tugas):
    nilai_akhir = (nilai_ujian * 0.7) + (nilai_tugas * 0.3)
    return nilai_akhir

print("Program Penghitung Nilai Akhir Siswa")
print("=" * 40)

while True:
    try:
        nilai_ujian = float(input("Masukkan nilai ujian (0-100): "))
        nilai_tugas = float(input("Masukkan nilai tugas (0-100): "))

        if 0 <= nilai_ujian <= 100 and 0 <= nilai_tugas <= 100:
            break
        else:
            print("Nilai harus angka 0-100. Silakan coba lagi.")
    except ValueError:
        print("mohon masukkan angka yang valid.")


nilai_akhir = hitung_nilai_akhir(nilai_ujian, nilai_tugas)

print("=" * 40)
print(f"Nilai Ujian: {nilai_ujian:.2f}")
print(f"Nilai Tugas: {nilai_tugas:.2f}")
print(f"Nilai Akhir: {nilai_akhir:.2f}")
print("=" * 40)
