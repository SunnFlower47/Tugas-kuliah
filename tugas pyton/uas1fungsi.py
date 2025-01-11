def menentukan_kenaikan_gaji(nama, jabatan, masa_kerja):
    
    kenaikan_gaji = 0

    if jabatan.lower() == "manager" and masa_kerja > 5:
        kenaikan_gaji = 20
    elif jabatan.lower() == "staff" and masa_kerja > 3:
        kenaikan_gaji = 10
    elif jabatan.lower() == "intern" and masa_kerja > 1:
        kenaikan_gaji = 5

    if kenaikan_gaji > 0:
        print(f"{nama} jabatan ({jabatan}) dengan masa kerja {masa_kerja} tahun berhak mendapatkan kenaikan gaji sebesar {kenaikan_gaji}%.")
    else:
        print(f"{nama} ({jabatan}) dengan masa kerja {masa_kerja} tahun tidak berhak mendapatkan kenaikan gaji.")

nama_karyawan = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan karyawan (Manager/Staff/Intern): ")
masa_kerja = int(input("Masukkan masa kerja (dalam tahun): "))

menentukan_kenaikan_gaji(nama_karyawan, jabatan, masa_kerja) 