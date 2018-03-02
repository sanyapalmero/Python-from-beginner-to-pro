def create_array():
    input_array = []
    array_len = int(input("Введите длину массива: "))
    for i in range(array_len):
        elem = int(input(f"Введите {i + 1} элемент массива: "))
        input_array.append(elem)
    print("Исходный массив: ", input_array)
    return (input_array)


def sort_array(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j+1]:
                temp_elem = array[j]
                array[j] = array[j+1]
                array[j+1] = temp_elem
    print("Отсортированный массив: ", array)


def main():

    input_array = create_array()
    sort_array(input_array)


if __name__ == '__main__':
    main()
