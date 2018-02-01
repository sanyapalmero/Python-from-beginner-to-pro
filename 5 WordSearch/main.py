def word_search(word,text):
    if word in text:
        print("Слово "+word+" найдено")
    else:
        print("Слово не найдено")

def main():
    string = input("Введите строку: ")
    word = input("Введите слово: ")
    word_search(word, string)

if __name__ == '__main__':
    main()