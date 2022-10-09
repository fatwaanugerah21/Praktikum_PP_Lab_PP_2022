a = input('Masukkan nilai A : ')
b = input('Masukkan nilai B : ')
c = input('Masukkan nilai C : ')


if c > a and c > b :
    terbesar = c 
elif b > a and b > c:
    terbesar = b
else:
    terbesar = a   
print(int(terbesar), 'adalah nilai terbesar')    


