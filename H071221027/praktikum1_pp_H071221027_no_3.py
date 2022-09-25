nilai=input("rata rata pemakaian listriharian (wh): ")
tarif= 1352
wh= float(nilai) 

harian= float(wh/1000)
bulanan= float(harian*30)
harga= float(bulanan*tarif)

print("jumlah tagihan listrik bulan : Rp.",round(harga)) 