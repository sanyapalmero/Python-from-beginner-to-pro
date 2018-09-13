import json


class AddressBook:
    def __init__(self, fio, address, phone):
        self.fio = fio
        self.address = address
        self.phone = phone


def entry_create():
    entries_list = []
    entries_count = int(input("Кол-во записей: "))
    for i in range(entries_count):
        fio = str(input("ФИО: "))
        address = str(input("Адрес: "))
        while True:
            try:
                phone = int(input("Телефон: "))
            except ValueError:
                print("Телефон содержит только цифры")
            else:
                break
        entry = AddressBook(fio, address, phone)
        entries_list.append(entry)
    return entries_list


def entries_show(entries):
    for entry in entries:
        print(
            f"ФИО: {entry.fio}, адрес: {entry.address}, телефон: {entry.phone}"
        )


def dict_create(entries):
    entries_list = []
    for entry in entries:
        entries_list.append({
            "ФИО": entry.fio,
            "Адрес": entry.address,
            "Телефон": entry.phone
        })
    print(
        json.dumps(entries_list, sort_keys=True, indent=4, ensure_ascii=False))


def start():
    while True:
        print("1 - Создать записи\n2 - Посмотреть записи\n3 - Выход")
        while True:
            try:
                action = int(input("> "))
            except ValueError:
                print("Введите 1, 2 или 3")
            else:
                break
        if action == 1:
            entries = entry_create()
        if action == 2:
            try:
                entries_show(entries)
                dict_create(entries)
            except UnboundLocalError:
                print("Записей нет")
        if action == 3:
            break


def main():
    start()


if __name__ == '__main__':
    main()
