import math

print("Pilihan Bangun Ruang:")
print("1. Volume Pyramid")
print("2. Volume Cylinder")
print("3. Volume Hollow Cylinder")
print("4. Volume Sphere (Bola)")

bangunRuang = int(input("Masukkan Pilihan Bangun Ruang (1 sampai 4): "))

match bangunRuang:
    case 1:
        # Volume Pyramid
        A = float(input("Masukkan panjang alas (A): "))
        B = float(input("Masukkan tinggi (B): "))
        hasil = (A * B) / 3
        print(f"Rumus Volume Pyramid: (A × B) ÷ 3")
        print(f"Volume Pyramid = ({A} × {B}) ÷ 3 = {hasil}")
        
    case 2:
        # Volume Cylinder
        r = float(input("Masukkan jari-jari (r): "))
        t = float(input("Masukkan tinggi (t): "))
        hasil = math.pi * r**2 * t
        print(f"Rumus Volume Cylinder: π × r² × t")
        print(f"Volume Cylinder = π × {r}² × {t} = {hasil}")
        
    case 3:
        # Volume Hollow Cylinder
        D = float(input("Masukkan diameter luar (D): "))
        d = float(input("Masukkan diameter dalam (d): "))
        t = float(input("Masukkan tinggi (t): "))
        hasil = (math.pi / 4) * (D**2 - d**2) * t
        print(f"Rumus Volume Hollow Cylinder: ¼ × π × (D² - d²) × t")
        print(f"Volume Hollow Cylinder = ¼ × π × ({D}² - {d}²) × {t} = {hasil}")
        
    case 4:
        # Volume Sphere (Bola)
        D = float(input("Masukkan diameter (D): "))
        hasil = (math.pi * D**3) / 6
        print(f"Rumus Volume Sphere (Bola): (π × D³) ÷ 6")
        print(f"Volume Sphere = (π × {D}³) ÷ 6 = {hasil}")
        
    case _:
        # Jika pilihan salah
        print("Pilihan tidak valid! Masukkan angka antara 1 sampai 4.")


        # Nama : Ridwan Andrian
        # NIM : 241351144
        # kelas : Malam A
