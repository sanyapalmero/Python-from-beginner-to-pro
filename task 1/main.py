def create_array():
    input_array = []
    array_len = int(input("Введите длину массива: "))
    i = 0
    for i in range(array_len):
        elem = int(input(f"Введите {i + 1} элемент массива: "))
        input_array.append(elem)
        i += 1
    print("Исходный массив: ", input_array)
    return (input_array)

def transform_array(array):
    output_array = []
    j = 0
    elem = 0
    for j in range(len(array)):
        elem += int(array[j])
        output_array.append(elem)
        j += 1
    print("Новый массив: ", output_array)

def main():
    input_array = create_array()
    transform_array(input_array)

if __name__ == '__main__':
    main()