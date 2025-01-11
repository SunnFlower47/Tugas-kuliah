def menghitung_angka_yang_di_inputkan():
    jumlah_total = 0
    jumlah_input = 0
    while jumlah_input < 10:
        try:
            angka = int(input("Masukkan angka: "))
            if angka < 0:
                print("ada angka negatif program otomatis berhenti")
                break
            jumlah_input += 1
            jumlah_total += angka
        except ValueError:
            print("Masukan angka yang valid")
    print(f"jumlah total angka yang di inputkan adalah {jumlah_total}")
menghitung_angka_yang_di_inputkan()
            