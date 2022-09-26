# Nomor 2 buatlah program yang merubah detik ke dalam format jam:menit:detik


detik = int(input('detik : '))

jam = detik // 3600
sisa_detik = detik  % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print(str(jam) + ':' + str(menit) + ':'+ str(detik))
