def create_array(i):
    j = 0
    a1 = []
    a2 = []
    while j < i:
        elem = input(f"Введите {j + 1} элемент: ")
        a1.append(elem)
        j += 1
    print("Исходный массив: ", a1)
    #дано: [a1,a2,a3...an]
    #сделать: [a1,a1+a2,a1+a2+a3...a1+a2+a3+an]
    j = 0
    elem = 0
    while j < i:
        elem += int(a1[j])
        a2.append(elem)
        j += 1
    print("Новый массив: ", a2)

def main():
    i = int(input("Введите количество элементов: "))
    create_array(i)

if __name__ == '__main__':
    main()