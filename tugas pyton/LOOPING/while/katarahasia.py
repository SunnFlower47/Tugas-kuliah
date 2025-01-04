print("tebak kata rahasia")
print("ridwan andrian(211351144)")

kata_rahasia= "apple"

while True:
    kata =str(input("tebak kata rahasia: "))
    if kata == kata_rahasia:
        print("Selamat! tebakan anda benar")
        break
    else:
        print("Tebakan salah, coba lagi!")
        