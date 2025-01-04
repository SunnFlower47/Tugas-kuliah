print()
print('##  Program Python menentukan temperatur air (cair, padat, gas) ##')
print('Ridwan Andrian (241351144)')
print('=' *70)
print()

temp = int(input("masukan suhu air dalam satuan °C:"))

if (temp <= 0):
    print(f"suhu {temp}°C adalah suhu air membeku (padat)")
elif (0 < temp < 100):
    print(f"suhu {temp}°C adalah suhu air mencair (cair)")
elif(temp >= 100):
    print(f"suhu {temp}°C adalah suhu air menguap (gas/uap)")
