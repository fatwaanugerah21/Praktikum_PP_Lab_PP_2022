nilai = input ('rata-rata pemakaian listrik harian dalam satuan watt jam')
tarif = 1325 #Kwh
wh = float(nilai)

harian = float(wh/1000) # Mengubah wh menjadi Kwh
bulanan = float(harian *30)
harga = float(bulanan*tarif)

print("Jumlah tagihan listrik bulanan : Rp", round(harga, 2))