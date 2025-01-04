print("Program Menghitung Nilai Rata-Rata")
print("ridwan andrian(211351144)")

print("=" * 40)
total=0
count=0

while True:
    try:
        num = int(input("Masukan nilai (-1 untuk berhenti): "))
        if num == -1:
            break
        elif num < 0:
            print("masukan bilangan positif")
            continue
        total += num
        count += 1
    except ValueError:
        print("Invalid input. masukan angka yang valid.")
            
if count == 0:
    print("tidak ada angka yang di masukan")
else:
    rata_rata = total / count
    print(f"nilai rata ratanyan adalah : {rata_rata}")