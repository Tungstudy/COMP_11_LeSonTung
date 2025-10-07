import math
m ,n = map(float, input("Nhap so m,n: ").split())
if n == 0:
    print("Phep chia khong hop le!")
else:
    print(math.ceil(m / n))