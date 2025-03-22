lama_parkir = int(input("Masukkan lama parkir (jam): "))

match lama_parkir:
    case 0 | 1:
        biaya = 5000
    case _:
        biaya = 5000 + (lama_parkir - 1) * 3000
        if biaya > 25000:
            biaya = 25000

print(f"Total biaya parkir: Rp.{biaya}")

# Nama : Ridwan Andrian
# Nim : 241351144
# Kelas : Malam A
