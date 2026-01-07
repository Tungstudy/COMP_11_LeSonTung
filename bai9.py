a, b, c = map(int, input("Nhap ba canh tam giac a,b,c: ").split())
if a*b < 0 or b*c < 0 or a*b*c < 0:
    print("So nhap vao khong hop le!")
else:

    if a + b > c and b +c > a and a + c > b:
        print('Yes')
    else:
        print("No")