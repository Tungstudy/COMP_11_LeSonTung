n = int(input("Numbers: "))
if n <= 0: 
    print(f"{n} chinh xac")
else:
    if n % 2 == 0:
        print(f"{n} la so chan")
    else:
        print(f"{n} la so le")