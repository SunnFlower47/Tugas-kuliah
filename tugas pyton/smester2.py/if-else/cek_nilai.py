# Input data mahasiswa
NIM = input("Masukkan NIM: ")
Nama = input("Masukkan Nama: ")
Kelas = input("Masukkan Kelas: ")
Alamat = input("Masukkan Alamat: ")
Hobi = input("Masukkan Hobi: ")

try:
    # Input nilai kehadiran
    Kehadiran = float(input("Masukkan Nilai Kehadiran (0-100): "))

    # Mengecek apakah nilai kehadiran memenuhi syarat
    if Kehadiran < 75:
        print("Maaf, Anda Belum Memenuhi Batas Minimal Kehadiran sehingga Tidak Bisa Mendapat Kalkulasi Nilai Lainnya")
    else:
        print("Selamat, Anda bisa mendapatkan kalkulasi komponen nilai lain")
        # Input nilai tugas,uts,uas
        Tugas = float(input("Masukkan Nilai Tugas (0-100): "))
        UTS = float(input("Masukkan Nilai UTS (0-100): "))
        UAS = float(input("Masukkan Nilai UAS (0-100): "))

        # mwnhitung Nilai Akhir
        NilaiAkhir = (Kehadiran * 0.10) + (Tugas * 0.35) + (UTS * 0.25) + (UAS * 0.30)

        # Menentukan Grade
        if NilaiAkhir > 80:
            Grade = "A"
        elif NilaiAkhir > 60:
            Grade = "B"
        elif NilaiAkhir > 40:
            Grade = "C"
        elif NilaiAkhir > 20:
            Grade = "D"
        else:
            Grade = "E"

        # Mencetak Output hasil
        print("\n===== Hasil Perhitungan Nilai =====")
        print(f"NIM     : {NIM}")
        print(f"Nama    : {Nama}")
        print(f"Kelas   : {Kelas}")
        print(f"Alamat  : {Alamat}")
        print(f"Hobi    : {Hobi}")
        print(f"Nilai Akhir : {NilaiAkhir:.2f}")
        print(f"Grade       : {Grade}")

except ValueError:
    print("Input harus berupa angka untuk nilai Kehadiran, Tugas, UTS, dan UAS!")