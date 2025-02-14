class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Book: {self.title} by {self.author} ({self.year_published})")

# Create three book objects
book1 = Book("Lord of the flies", "William Golding, E. M. Forster", 1962)
book2 = Book("The stranger", "Albert Camus, Matthew Ward",  1989)
book3 = Book("Vanity fair", "William Makepeace Thackeray", 1991)

# Display book details
book1.describe()
book2.describe()
book3.describe()

