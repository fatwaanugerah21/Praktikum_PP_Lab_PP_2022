detik=eval(input("Masukan nilai detik ="))

menit=detik/60
jam=detik/3600

print("%02d:%02d:%02d"% (jam, menit % 60,detik % 60))

