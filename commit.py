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
book1=create_book("Holes","1998","Unknown")
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
