# Nomor 1 Menghitung panjang kapal
import math

h = str(input('Tinggi menara :'))
b = float(input('Sudut elevasi pengamat terhadap ujung kapal :'))
a = float(input('Sudut elevasi pengamat terhadap ujung belakang kapal:'))

ac = math.tan(math.radians(a))*h
bc = math.tan(math.radians(b))*h
result = (bc - ac)

print("Panjang kapal = {:.1f} m".format(result))
