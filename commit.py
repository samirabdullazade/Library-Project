import datetime
import json

app_name = 'library'
version = '0.1.0'
is_active = True
book_count =0

print(f"app Name: {app_name}, Version: {version}")

def create_book(title,year,author,game="Unkown"):
    book={"title":title,"year":year,"author":author,"game":game,"is_read":False}
    return book
def is_classic(book):
    if book["year"] < 1950:
        return True
    else:
        return False
book1=create_book("Holes",1998,"Unknown")
print(is_classic(book1))

library=[]
def add_book(book):
    library.append(book)
def remove_book(title):
    for book in library:
        if book["title"] == title:
            library.remove(book)
            return
    print(f"Book with title '{title}' not found in the library.")

def all_genres():
    genres=set()
    for book in library:
        genres.add(book["game"])
    return genres

classic_books=[book["title"] for book in library if book['year'] < 1950]
authors=[book["author"] for book in library]

def book_iterator(genre_filler=None):
    for book in library:
        if genre_filler is None or book["game"] == genre_filler:
            yield book

def save_library(filename="file.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(library, file, indent=2)

try:
    with open("file.json", "r", encoding="utf-8") as file:
        library = json.load(file)
except FileNotFoundError:
    print("No existing library found. Starting with an empty library.")

now = datetime.datetime.now()
print(f"Current date and time: {now}")

week_later = now + datetime.timedelta(days=7)
print(week_later)

class Book:
    def __init__(self, title, year, author, genre, is_read):
        self.title = title
        self.year = year
        self.author = author
        self.genre = genre
        self.is_read = is_read

    def mark_as_read(self):
        self.is_read = True

    def is_classic(self):
        if self.year < 1950:
            return True
book1=Book("O Alquimista", 1988, "Paulo Coelho", "Ficção", False)

class Ebook(Book):
    def __init__(self, title, year, author, genre, filesize, is_read=False):
        super().__init__(title, year, author, genre, is_read)
        self.filesize = filesize

class AudioBook(Book):
    def __init__(self, title, year, author, genre, narrator, duration, is_read=False):
        super().__init__(title, year, author, genre, is_read)
        self.narrator = narrator
        self.duration = duration