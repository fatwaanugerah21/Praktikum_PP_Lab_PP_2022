# Nomor 3 Buatlah program yang menerima input diameter bola dan print volumenya

import math
d = float(input('Diameter :'))

phi = math.pi
V = (phi * (d**3)/6)

print("Volume Bola = {:.1f} ".format(V))