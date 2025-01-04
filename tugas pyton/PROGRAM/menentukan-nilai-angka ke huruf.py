print()
print('##  Program Python menetuka nilai huruf dair angka  ##')
print('Ridwan Andrian (241351144)')
print('=' *70)
print()


angka =int(input("masukan nilai angka:"))

if(0 <= angka <= 20):
    print("Nilai hurufnya adalah E")
elif(20 < angka <= 40):
    print("Nilai hurufnya adalah D")
elif(40 < angka <= 60):
    print("Nilai hurufnya adalah C")
elif(60 < angka <= 80):
    print("Nilai hurufnya adalah B")
elif(80 < angka <= 100):
    print("Nilai hurufnya adalah A")
else:
    angka > 100, angka < 0
    print("nilai salah, masukan angka dari 0 sampai 100")
