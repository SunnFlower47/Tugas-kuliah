# Meminta input total belanja dari pengguna
total_belanja = float(input("Masukkan total belanja: Rp "))

# Menentukan diskon berdasarkan total belanja
if total_belanja >= 500000:
    diskon = 0.2
elif total_belanja >= 250000:
    diskon = 0.1
else:
    diskon = 0

# Menghitung total bayar setelah di diskon
total_diskon = total_belanja * diskon
total_bayar = total_belanja - total_diskon

# Menampilkan output total belanja, diskon, dan total bayar setelah diskon
print(f"Total belanja: Rp {total_belanja:,.2f}")
print(f"Diskon: Rp {total_diskon:,.2f}")
print(f"Total bayar setelah diskon: Rp {total_bayar:,.2f}")
