print("Program Menghitung Jumlah Angka Bulat Positif")
print("ridwan andrian(211351144)")

total = 0  

print("Masukkan angka bulat positif (-1 untuk berhenti):")
while True:
    angka = int(input("Masukkan angka: "))
    if angka == -1:
        break
    if angka < -1:  
        print("Angka negatif tidak valid. Silakan masukkan angka bulat positif (-1 untuk berhenti).")
        continue
    total += 1 

print(f"Jumlah total angka yang dimasukkan adalah: {total}")
