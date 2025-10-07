n = int(input("Numbers:"))
if n & (n - 1) == 0:
    print(f"{n} la luy thua cua 2")
else:
    print(f"{n} khong la luy thua cua 2")