a, b, c, d = map(int, input("Nhap 4 so a,b,c,d: ").split())

if a >= b:
    temp1 = a
else:
    temp1 = b
if c >= d:
    temp2 = c
else:
    temp2 = d
if temp1 >= temp2:
    print(temp1)
else:
    print(temp2)
