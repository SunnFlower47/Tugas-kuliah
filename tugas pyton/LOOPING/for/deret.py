def hitung_deret():
    while True:
        try:
            n = int(input("masukan nilai:"))
            if n < 1:
                print("masukan angkalebih dari nol atau bolangan positif")
                continue
            jumlah = 0
            for i in range(1, n + 1):
                jumlah += i
            print(f"Jumlah deret angka dari 1 sampai {n} adalah {jumlah}")
            lanjut = input("Apakah Anda ingin menghitung lagi? (y/n): ").lower()
            if lanjut != 'y':
                print("Terima kasih sudah menggunakan program ini.")
                break
        except ValueError:
            print("masukan angka yang valid")
hitung_deret()
