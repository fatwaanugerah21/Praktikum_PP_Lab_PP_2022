x = int(input("Horizontal : "))
y = int(input("Range : "))
for i in range(1,y+1):
    print(i, end=' ')
    if i%x==0 :
        print()