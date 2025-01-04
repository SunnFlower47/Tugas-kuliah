print('##  Program Python menetukan gaji mingguan dari jam kerja dan menetukan golongan  ##')
print('Ridwan Andrian (241351144)')
print('=' *90)
print()


jam_kerja=eval(input('masukan jam kerja:'))
golongan =input('masukan golongan (A/B/C/D):')

if (golongan == 'A' and jam_kerja <= 48):
    gaji_perjam = 4000
    gaji_total = gaji_perjam * jam_kerja
    print(f'gaji total: Rp.{gaji_total}')
elif (golongan == 'A' and jam_kerja > 48):
    gaji_lembur = (jam_kerja - 48) * 3000
    gaji_total = 48 * 4000 + gaji_lembur
    print(f'gaji total: Rp.{gaji_total}')
elif (golongan == 'B' and jam_kerja <= 48):
    gaji_perjam = 5000
    gaji_total = gaji_perjam * jam_kerja
    print(f'gaji total: Rp.{gaji_total}')
elif (golongan == 'B' and jam_kerja > 48):
    gaji_lembur = (jam_kerja - 48) * 3000
    gaji_total = 48 * 5000 + gaji_lembur
    print(f'gaji total: Rp.{gaji_total}')
elif (golongan == 'C' and jam_kerja <= 48):
    gaji_perjam = 6000
    gaji_total = gaji_perjam * jam_kerja
    print(f'gaji total: Rp.{gaji_total}')
elif (golongan == 'C' and jam_kerja > 48):
    gaji_lembur = (jam_kerja - 48) * 3000
    gaji_total = 48 * 6000 + gaji_lembur
    print(f'gaji total: Rp.{gaji_total}') 
elif (golongan == 'D' and jam_kerja <= 48):
    gaji_perjam = 7500
    gaji_total = gaji_perjam * jam_kerja
    print(f'gaji total: Rp.{gaji_total}')
elif (golongan == 'D' and jam_kerja > 48):
    gaji_lembur = (jam_kerja - 48) * 3000
    gaji_total = 48 * 7500 + gaji_lembur
    print(f'gaji total: Rp.{gaji_total}')
else:
    print('golongan tidak valid')
    