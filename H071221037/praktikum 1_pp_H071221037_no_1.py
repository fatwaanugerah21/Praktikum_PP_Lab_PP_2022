import math
h = float(input("Masukkan Ketinggian Menara (dalam satuan meter): ")) 
a = float(input("Masukkan Derajat Sudut Elevasi Pengamat Terhadap Ujung Belakang Kapal: "))
b = float(input("Masukkan Derajat Sudut Elevasi Pengamat Terhadap Ujung Depan Kapal: "))

# 90 > a >  b

belakang = h * (math.tan(math.radians(a)))
depan = h * (math.tan(math.radians(b)))
panjang = belakang-depan

print("Panjang Kapalnya adalah", panjang, "m", round(panjang,1),"m")

