print('=====Program Konversi Detik Ke Jam=====')
detik = int(input('Masukkan Jumlah detik yang ingin di konversi : '))
 
jam = detik/3600
sisa_detik = detik % 3600
menit = sisa_detik / 60
detik = sisa_detik % 60 

jam=str(jam)
menit=str(menit)
detik=str(detik)

print(jam + ':' + menit +':' + detik)