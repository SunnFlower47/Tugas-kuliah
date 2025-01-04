def hitung_diskon(total_belanja):
    if total_belanja < 100000:
        diskon = 0
    elif 100000 <= total_belanja < 500000:
        diskon = total_belanja * 0.1
    elif total_belanja >= 500000:
        diskon = total_belanja * 0.2
    return diskon
def hitung_total_bayar(total_belanja, diskon):
    total_bayar = total_belanja - diskon
    return total_bayar

print("Program Menghitung Total Diskon Belanja")
print("=" * 55)
while True:
    try:
        total_belanja = int(input("Masukkan total belanjaan: "))
        if total_belanja < 0:
            print("Total belanja tidak boleh negatif. Silakan masukkan angka yang benar.")
            continue
        break
    except ValueError:
        print("Input harus berupa angka. Silakan coba lagi.")
diskon = hitung_diskon(total_belanja)
total_bayar = hitung_total_bayar(total_belanja, diskon)

print("=" * 55)
print(f"Total belanja: {total_belanja}")
if diskon > 0:
    persen_diskon = (diskon / total_belanja) * 100
    print(f"-- Kamu mendapat diskon {persen_diskon:.0f}% sebesar Rp{diskon:,.0f} --")
else:
    print("--Kamu tidak mendapatkan diskon--")
print(f"Total yang harus dibayar: {total_bayar}")
print("=" * 55)