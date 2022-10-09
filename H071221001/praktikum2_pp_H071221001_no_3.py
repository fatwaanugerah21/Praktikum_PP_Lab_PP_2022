# 3. Buatlah program untuk menentukan nilai terbesar dari tiga angka!
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
terbesar = 0
if a>b and a>c :
    terbesar = a
elif b>a and b>c :
    terbesar = b
elif c>a and c>b :
    terbesar = c

print(f"{terbesar} adalah nilai terbesar")