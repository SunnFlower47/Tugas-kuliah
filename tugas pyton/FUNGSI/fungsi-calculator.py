print("Program Kalkulator Sederhana")

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "pembagian tidak boleh angka nol"
    return a / b

operations = {
    "1": ("+", tambah),
    "2": ("-", kurang),
    "3": ("*", kali),
    "4": ("/", bagi)
}

while True:
    print("\nMenu oprasi:")
    print(' 1. Jumlah \t [+]')
    print(' 2. Kurang \t [-]')
    print(' 3. Kali \t [*]')
    print(' 4. bagi \t [/]')
    print(' 5. Keluar')
    print()

    pilihan = input("Pilih oprasi (1/2/3/4/5): ")
        
    if pilihan == "5":
        print("Terima kasih telah menggunakan program calkulator sederhana ini!")
        break

    while True:
        try:
            a = float(input("Masukkan angka pertama: "))
            b = float(input("Masukkan angka kedua: "))
            break
        except ValueError:
            print("Harap masukkan angka yang valid!")

    if pilihan in operations:
        oprasi, func = operations[pilihan]
        hasil = func(a, b)
        print(f"Hasil dari operasi {a} {oprasi} {b} = {hasil if isinstance(hasil, str) else hasil:.2f}")
    else:
        print("Pilihan tidak valid.")