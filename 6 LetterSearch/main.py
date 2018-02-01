def letter_search(letter,text):
    count = 0
    for i in text:
        if i == letter:
            count += 1
    if count != 0:
        print("Буква {} найдена и она встречается {} раз".format(letter, count))
        #print(f"Буква {letter} найдена и она встречается {count} раз") only for v 3.6.0 and older
    else:
        print("Буквы в строке нет")

def main():
    srting = input("Введите текст: ")
    letter = input("Введите букву: ")
    letter_search(letter, srting)

if __name__ == '__main__':
    main()