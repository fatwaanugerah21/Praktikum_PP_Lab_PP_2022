# 2. Buatlah program menginput informasi daya listrik dan menghitung total tagihan listrik

golongan = input("Golongan:")
daya = float(input("Daya:"))
pemakaian = float(input("Pemakaian:"))
tagihan = 0
if golongan == 'R1' : 
    if daya == 900: 
        tagihan = pemakaian * 1352
    elif daya == 1300 and daya == 2200:
        tagihan = pemakaian * 1444.70
elif golongan == 'R2' :
    if daya >= 3500 and daya <=  5500:
        tagihan = pemakaian * 1699.53
elif golongan == 'R3':
    if daya >= 6600 :
        tagihan = pemakaian * 1699.53
elif golongan == 'B2':
    if daya >=6600 and daya <= 200000:
        tagihan = pemakaian * 1444.70
elif golongan == 'B3':
    if daya > 200000 :
        tagihan = pemakaian * 1114.74
elif golongan == 'I3':
    if daya >= 200000:
        tagihan = pemakaian * 1314.12
elif golongan == 'P1':
    if daya >=6600 and daya <= 200000:
        tagihan = pemakaian * 1523.28

else: 
    print('data tidak valid')
    
print("Jumlah tagihan anda:{:0,.2f}".format(tagihan))
