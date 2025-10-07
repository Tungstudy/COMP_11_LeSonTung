a, b, c = map(int, input().split())

if not(a + b > c and a + c > b and b + c > a):
    print(f"ba so {a,b,c} khong tao thanh 1 tam giac")
else:
    if a == b == c:
        print("Tam giac tao ra la tam giac deu")
    elif a == b or b == c or c == a:
        print("Tam giac tao ra la tam giac can")
    else:
        print("Tam giac duoc tao ra la tam giac thuong")