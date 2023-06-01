class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        print("Назва книги:", self.title)
        print("Автор:", self.author)
book1 = Book("Майстер і Маргарита", "Михайло Булгаков")
book1.get_info()
