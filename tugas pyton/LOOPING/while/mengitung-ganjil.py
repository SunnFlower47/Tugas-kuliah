jumlah_ganjil = 0
jumlah_angka = 0

while jumlah_angka < 8:
    angka = int(input("masukan angka: "))
    if angka % 2 != 0:
        jumlah_ganjil += 1
    if angka < 0:
        break
    jumlah_angka += 1
    if jumlah_angka > 8:
        break
print(f"jumlah angka ganjil yang di inputkan adalah {jumlah_ganjil}")