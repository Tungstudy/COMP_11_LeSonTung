a = float(input("Enter a float: "))

# Lam tron xuong
print(int(a//1), end = (" "))

# Lam tron len

if a == (a // 1):
    print(int(a), end = (" "))
else:
    print( int((a // 1) + 1), end = (" "))

# Lam tron den so nguyen gan nhat

if (a - (a//1)) >= 0.5:
    print(int(a//1 + 1),end= (" ") )
else:
    print(int(a//1), end=(" "))
