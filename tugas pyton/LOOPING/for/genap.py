def menghitung_bilangan_genap1_sapai_10():
    jumlah_genap = 0
    for angka in range(1, 11):
        if angka % 2== 0:
            print(angka)
            jumlah_genap += 1
    print(f"Jumlah bilangan genap: {jumlah_genap}")
menghitung_bilangan_genap1_sapai_10()