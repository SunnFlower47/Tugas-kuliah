print('##  Program Python kalculator sederhana  ##')
print('Ridwan Andrian (241351144)')
print('=' *54)
print()

print('=' *25)
while True:
    print('Oprasi Matematika')
    print(' 1. tambah \t [+]')
    print(' 2. Kurang \t [-]')
    print(' 3. Kali \t [*]')
    print(' 4. bagi \t [/]')
    print(' 5. Keluar')
    print('=' *25)

    oprasi = input('Pilih oprasi (1/2/3/4) :' )
    
    if oprasi == '5':
        break
    
    bilangan_1 = eval(input('Masukan Bilangan Pertama: '))
    bilangan_2 = eval(input('Masukan Bilangan kedua: '))

    if oprasi == '1':
        hasil = bilangan_1 + bilangan_2
        print(f'Hasil oprasi dari {bilangan_1}+{bilangan_2}={hasil}')
    elif oprasi == '2':
        hasil = bilangan_1 - bilangan_2
        print(f'Hasil oprasi dari {bilangan_1}-{bilangan_2} = {hasil}')
    elif oprasi == '3':
        hasil = bilangan_1 * bilangan_2
        print(f'Hasil oprasi dari {bilangan_1}*{bilangan_2} = {hasil}')
    elif oprasi == '4':
        hasil = bilangan_1 / bilangan_2
        print(f'Hasil oprasi dari {bilangan_1}/{bilangan_2} = {hasil}')    
    else:
        print('Tidak vailid')
        continue