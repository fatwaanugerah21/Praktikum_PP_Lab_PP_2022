# 1. Buatlah program yang dapat mengkonversi nilai dalam bentuk angka ke huruf
nilai = int(input("Masukkan nilai:"))

if nilai >= 90 and nilai <=100:
    print(f"Nilai {nilai} = 'A'")
elif nilai >= 80 and nilai <90:
    print(f"Nilai {nilai} ='B'" )
elif nilai >= 70 and nilai < 80:
    print(f"Nilai {nilai}  ='c'" )
elif nilai >= 60 and nilai < 70:
    print(f"Nilai {nilai} = 'D'")
elif nilai >= 40 and nilai < 60:
    print(f"Nilai {nilai} = 'E'" )
elif nilai < 40 and nilai >= 0 :
    print(f"Nilai {nilai} = 'F'") 

else:
    print("Nilai tidak valid")