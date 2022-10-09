print('\n==============================')
print('   PROGRAM TAGIHAN LISTRIK   ')
print('==============================')

golongan =(input('\nGolongan = '))
daya = float(input('Daya = '))
pemakaian = float(input('Pemakaian = '))
jumlah_tagihan_anda= ''

if daya==900 and golongan=='R1':
    tarif= 1.352
    tagihan= pemakaian*tarif
elif daya==1300 and golongan=='R1':
    tarif= 1444.70
    tagihan= pemakaian*tarif
elif daya==2200 and golongan=='R1':
    tarif= 1444.70
    tagihan= pemakaian*tarif
elif daya>=3500 and daya<=5500 and golongan=='R2':
    tarif= 1699.53
    tagihan= pemakaian*tarif
elif daya>=6600 and golongan=='R3':
    tarif= 1444.70
    tagihan= pemakaian*tarif
elif daya>=6600 and daya<=200000 and golongan=='B2':
    tarif= 1444.70
    tagihan= pemakaian*tarif
elif daya>200000 and golongan=='B3':
    tarif= 1114.74
    tagihan= pemakaian*tarif
elif daya>=200000 and golongan=='I3':
    tarif= 1314.12
    tagihan= pemakaian*tarif
elif daya>=6600 and daya<=200000 and golongan=='P1':
    tarif= 1523.28
    tagihan= pemakaian*tarif
else:
    print('Data tidak valid')

print(f'Jumlah tagihan anda : {tagihan:,}')
