num = int(input("Input num: "))
if num > 0:
    print("num > 0")
    if num < 10:
        print("num < 10")
    else:
        print("num > 10")
elif num < 0:
    print("num < 0")
else:
    print("num = 0")