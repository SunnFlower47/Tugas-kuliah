# Data pelanggan
pelanggan_hari_1 = {"Ali", "Budi", "Citra", "Dina", "Eka"}
pelanggan_hari_2 = {"Budi", "Citra", "Fahmi", "Gina", "Eka"}
pelanggan_hari_3 = {"Ali", "Gina", "Henry", "Eka", "Fahmi"}

# a. Daftar pelanggan yang datang pada hari pertama saja
hanya_hari_pertama = pelanggan_hari_1 - pelanggan_hari_2 - pelanggan_hari_3
print("Pelanggan yang datang hanya pada hari pertama:", hanya_hari_pertama)

# b. Daftar pelanggan yang datang pada semua hari
semua_hari = pelanggan_hari_1 & pelanggan_hari_2 & pelanggan_hari_3
print("Pelanggan yang datang pada semua hari:", semua_hari)

# c. Daftar pelanggan yang datang pada minimal dua hari
dua_hari = (pelanggan_hari_1 & pelanggan_hari_2) | (pelanggan_hari_1 & pelanggan_hari_3) | (pelanggan_hari_2 & pelanggan_hari_3)
print("Pelanggan yang datang pada minimal dua hari:", dua_hari)

# d. Tambahkan pelanggan baru bernama "Irma" ke daftar pelanggan hari kedua
pelanggan_hari_2.add("Irma")
print("Pelanggan hari kedua setelah menambahkan Irma:", pelanggan_hari_2)

# e. Hitung total pelanggan unik yang datang selama tiga hari
total_unik = pelanggan_hari_1 | pelanggan_hari_2 | pelanggan_hari_3
print("Total pelanggan unik selama tiga hari:", total_unik)
print("Jumlah total pelanggan unik:", len(total_unik))
