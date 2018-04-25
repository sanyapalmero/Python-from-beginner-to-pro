class Book:
    def CreateBook(self, Author, Title, Year):
        self.Author = Author
        self.Title = Title
        self.Year = Year


def main():
    b = Book()
    author = input("Введите автора: ")
    title = input("Введите название: ")
    year = input("Введите год: ")
    b.CreateBook(author, title, year)
    print(f"Автор: {b.Author}\nНазвание: {b.Title}\nГод: {b.Year}")


if __name__ == '__main__':
    main()
