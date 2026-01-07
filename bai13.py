n = float(input("Nhap so tien dien tieu thu: "))

if n in range (0, 51):
    print(f"Tien dien: {n * 1500} vnd")
elif n in range (51 , 101):
    print(f"Tien dien: {n * 2000} vnd")
else:
    print(f"Tien dien: {n * 3000} vnd")

