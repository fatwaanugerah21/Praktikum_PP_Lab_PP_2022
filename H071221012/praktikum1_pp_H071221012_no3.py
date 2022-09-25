print('\n------Program mencari volume dan luas permukaan kerucut------')
jari_jari_alas = int(input('\nMasukkan Jari-jari : '))
tinggi = int(input('Masukkan Tinggi : '))

r=jari_jari_alas
t=tinggi
import math
phi = math.pi
s = (r**2)+(t**2)
S = s**0.5

volume = (phi*r*r*t)/3
luas_permukaan = (phi*r*S)+phi*r*r

print('Volume : ',round(volume,2))
print('Luas Permukaan : ', round(luas_permukaan,2))

print('\n\t-----terimakasih telah menggunakan programku:)-----')