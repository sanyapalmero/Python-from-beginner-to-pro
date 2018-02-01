def letter_search(letter,text):
    count = 0
    for i in text:
        if i == letter:
            count += 1
    if count != 0:
        c = str(count)
        print("Буква "+letter+" найдена и она встречается "+c+" раз")
    else:
        print("Буквы в строке нет")

def main():
    srting = input("Введите текст: ")
    letter = input("Введите букву: ")
    letter_search(letter, srting)

if __name__ == '__main__':
    main()