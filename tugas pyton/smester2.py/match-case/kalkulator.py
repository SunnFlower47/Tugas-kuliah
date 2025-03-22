a = float(input("Masukan Nilai Pertama: "))
b = float(input("Masukan Nilai Kedua: "))

print("\nMenu oprasi:")
print(' 1. Jumlah \t [+]')
print(' 2. Kurang \t [-]')
print(' 3. Kali \t [*]')
print(' 4. bagi \t [/]')
print(' 5. Keluar')
print()

oprasi = input("Masukan Operator (1, 2, 3, 4): ")

match oprasi:
    case "1":
        hasil = a + b
    case "2":
        hasil = a - b
    case "3":
        hasil = a * b
    case "4":
        if b == 0:
            print("Pembagian tidak boleh dengan angka nol!")
        else:
            hasil = a / b

print(f"Hasil dari {a} + {b} = {hasil:.2f}")

# Nama : Ridwan Andrian
# Nim : 241351144
# Kelas : Malam A