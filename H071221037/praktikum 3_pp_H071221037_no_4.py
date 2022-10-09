x = int(input('masukkan baris : '))

for i in range(x) : 
    for j in range(0, x- 2 * i + 3) :
        print(' ', end = '')
    for j in range(0, 2 * i + 1) :
        print('*', end = ' ')
    print()   
     

