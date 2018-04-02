def create_user():
    count = int(input("Введите количество пользователей: "))
    base = {}
    for i in range(count):
        print(f"Введите данные {i + 1} пользователя:")
        user_id = int(input("Введите номер пользователя: "))
        name = input("Введите имя: ")
        surname = input("Введите фамилию: ")
        age = 0
        while age == 0:
            age = int(input("Введите возраст: "))
            if age <= 0:
                print("Возраст не может быть отрицательным числом или нулем!")
                age = 0
            else:
                break
        studing = input("Введите место учебы: ")
        data = f"Имя: {name} \nФамилия: {surname} \nВозраст: {age} \nМесто учебы: {studing}"
        base[user_id] = data
    print(f"{count} пользователей были успешно добавлены")
    return base


def show_all_users(base):
    print("Все пользователи:")
    print(base)


def find_user_by_id(base):
    search_id = int(input("Введите номер пользователя: "))
    try:
        print(base[search_id])
    except KeyError:
        print(f"Пользователя с номером {search_id} не существует!")


def main():
    base = create_user()
    show_all_users(base)
    find_user_by_id(base)
    answer = True
    while answer:
        choie = input("Искать пользователя дальше? y/n: ")
        if choie == "n":
            break
        elif choie == "y":
            find_user_by_id(base)
            aswer = True
        else:
            print(
                "Команда не найдена - введите y(yes) или n(no) для продолжения работы"
            )
            answer = True


if __name__ == '__main__':
    main()
