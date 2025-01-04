from builtins import input, int, print


print()
print('##  Program Python Membuat Diskon Belanja  ##')
print('Ridwan Andrian (241351144)')
print('=' *55)
print()


belanja=int(input("masukan total belanjaan:"))

if (belanja < 10000):
    print('Anda mendapat diskon 0%')
    print(f"jumlah yang harus di bayar IDR.{belanja}")
elif (10000 <= belanja < 50000):
    diskon1= belanja - (0.1 * belanja) 
    print('Anda mendapatkan diskon 10%')
    print(f"jumlah yang harus di bayar IDR.{diskon1}")
elif (50000 <= belanja < 100000):
    diskon2= belanja - (0.15 * belanja) 
    print('Anda mendapatkan diskon 15%')
    print(f"jumlah yang harus di bayar IDR.{diskon2}")
elif (belanja >= 100000):
    diskon3= belanja - (0.2 * belanja) 
    print('Anda mendapatkan diskon 20%')
    print(f"jumlah yang harus di bayar IDR.{diskon3}")
else:
    print("Nilai belanjaan tidak valid.")