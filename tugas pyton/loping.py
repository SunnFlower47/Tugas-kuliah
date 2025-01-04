# Program untuk menghitung rata-rata dari sejumlah bilangan yang diinputkan
def hitung_rata_rata():
    try:
        # Meminta pengguna untuk memasukkan jumlah bilangan
        jumlah_bilangan = int(input("Masukkan jumlah bilangan: "))
        
        if jumlah_bilangan <= 0:
            print("Jumlah bilangan harus lebih dari 0!")
            return
        
        # Meminta input bilangan satu per satu
        total = 0
        for i in range(jumlah_bilangan):
            bilangan = float(input(f"Masukkan bilangan ke-{i + 1}: "))
            total += bilangan
        
        # Menghitung rata-rata
        rata_rata = total / jumlah_bilangan
        
        # Menampilkan hasil
        print(f"Rata-rata dari {jumlah_bilangan} bilangan adalah {rata_rata}")
    except ValueError:
        print("Harap masukkan angka yang valid!")

# Menjalankan program
hitung_rata_rata()
