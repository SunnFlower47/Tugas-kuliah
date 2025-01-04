def hitung_nilai_rata_rata():
    while True:
        try:
            # Meminta input jumlah bilangan
            jumlah_bilangan = int(input("Masukkan jumlah bilangan (1-10): "))
            if jumlah_bilangan <= 0:
                print("Jumlah bilangan harus lebih dari 0.")
                continue 
            elif jumlah_bilangan >= 10:
                print("Jumlah bilangan harus kurang dari atau sama dengan 10.")
                continue
            
            # Inisialisasi total untuk menghitung rata-rata
            total = 0
            for i in range(jumlah_bilangan):
                while True:
                    try:
                        # Meminta input bilangan
                        bilangan = float(input(f"Masukkan bilangan ke-{i + 1}: "))
                        if 0 <= bilangan <= 100:
                            total += bilangan
                            break
                        else:
                            print("Nilai tidak boleh negatif atau lebih dari 100.")
                    except ValueError:
                        print("Input harus berupa angka. Silakan coba lagi.")
            
            # Menghitung rata-rata
            rata_rata = total / jumlah_bilangan
            print(f"Nilai rata-rata dari {jumlah_bilangan} bilangan di atas adalah {rata_rata:.2f}")
            
            # Menanyakan apakah ingin menghitung lagi
            lanjut = input("Apakah Anda ingin menghitung lagi? (y/n): ").lower()
            if lanjut != 'y':
                print("Terima kasih sudah menggunakan program ini.")
                break
        except ValueError:
            print("Input jumlah bilangan harus berupa angka atau bilangan bulat positif.")

hitung_nilai_rata_rata()
