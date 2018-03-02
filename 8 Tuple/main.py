def main():
    test_tuple = ("Name1", "Surname1")
    try:
        test_tuple[0] = "Name2"
        test_tuple[1] = "Surname2"
        print(test_tuple)
    except Exception:
        print("Невозможно переприсвоить значения кортежа")

    test_array = ["Name1", "Surname1"]
    try:
        test_array[0] = "Name2"
        test_array[1] = "Surname2"
        print(test_array)
        print("Новые значения успешно установлены")
    except Exception:
        print("some error")


if __name__ == '__main__':
    main()
