year = int(input("Nhap 1 nam nao do: "))
con_st = year % 4 == 0 and year % 100 != 0
con_nd = year % 400
if con_st or con_nd:
    print(f"{year} la nam nhuan")
else:
    print(f"{year} la nam khong nhuan")