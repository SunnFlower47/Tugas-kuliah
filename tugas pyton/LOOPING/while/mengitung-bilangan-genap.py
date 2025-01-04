print("Program Mengitung Bilangan Genap")
print("ridwan andrian(211351144)")

count = 0
bilanagn_genap = []

print("Masukkan angka -1 untuk berhenti")
while True:
    angka = int(input("Masukkan bilangan: "))
    if angka == -1:
        break
    if angka % 2 == 0:
        count += 1
        bilanagn_genap.append(angka)

if count > 0:
    print(f"Banyaknya bilangan genap adalah: {count} yaitu {bilanagn_genap}")
else:
    print("Tidak ada bilangan genap yang dimasukkan.")