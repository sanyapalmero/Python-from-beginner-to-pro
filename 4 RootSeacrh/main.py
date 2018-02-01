import math

def RootsSearch (a,b,c):
        d = (b**2)-(4*a*c)
        if d > 0:
            x1 = ((-b + math.sqrt(d)) / (2*a))
            x2 = ((-b - math.sqrt(d)) / (2*a))
            print(x1,x2)
        elif d == 0:
            x = -b / 2*a
            print(x)
        else:
            print("Корней нет")

def main():
    a = int(input("Введите а: "))
    b = int(input("Введите b: "))
    c = int(input("Введите c: "))
    RootsSearch(a,b,c)

if __name__ == '__main__':
    main()
