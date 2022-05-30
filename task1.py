from book import Book
from bookcollection import BookCollection

def show_menu():
    print('Menu:')
    print('L - List all books')
    print('A - Add new book')
    print('M - Mark a book as completed')
    print('Q - Quit')




if __name__ == '__main__':
    print('Reading Tracker 2. 1 - by Lindsay Ward')
    collection = BookCollection()
    collection.load_books('books.csv')
    while True:
        show_menu()
        cmd = input('>>> ').lower()
        if cmd == 'l':
            collection.list_book()
        elif cmd == 'a':
            collection.add_book()
        elif cmd == 'm':
            collection.mark_books()
        elif cmd == 'q':
            break
        else:
            print('Invalid menu choice')
    collection.save_book('books.csv')
    print('So many books, so little time. Frank Zappa')