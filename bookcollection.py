from book import Book

class BookCollection:
    books = list()

    def load_books(self, filename):
        for line in open(filename).readlines():
            line = line.strip()
            sp = line.split(',')
            is_completed = False
            if sp[3].strip() == 'c':
                is_completed = True
            book = Book(sp[0].strip(), sp[1].strip(), int(sp[2].strip()), is_completed)
            self.books.append(book)
        print(len(self.books), 'books loaded')

    def save_book(self, filename):
        fp = open(filename, 'w')
        for book in self.books:
            is_completed = 'r'
            if book.is_completed:
                is_completed = 'c'
            fp.write('%s,%s,%d,%s\n' % (book.title, book.author, book.number_of_pages, is_completed))
        fp.close()
        print(len(self.books), 'books saved to', filename)

    def add_book(self, book):
        if book is None:
            title = get_title_input()
            author = get_author_input()
            pages = get_pages_input()
            print('%s by %s, (%d pages) added to Reading Tracker' % (title, author, pages))
            self.books.append(Book(title, author, pages, False))
        else:
            self.books.append(book)

    def sort(self, attr):
        if attr == 'Title' or attr == 'title':
            self.books = sorted(self.books, key=lambda item: item.title)
        elif attr == 'Author' or attr == 'author':
            self.books = sorted(self.books, key=lambda item: item.author)
        else:
            return

    def get_required_pages(self):
        need_pages = 0
        for item in self.books:
            if not item.is_completed:
                need_pages = need_pages + item.number_of_pages
        return need_pages

    def list_book(self):
        index = 1
        need_pages = self.get_required_pages()
        bs = 0
        for item in self.books:
            if item.is_completed:
                print(' '+str(index)+'. ', end="")
            else:
                print('*'+str(index)+'. ', end="")
                bs = bs + 1
            print(str(item))
            index = index + 1
        print('You need to read %d pages in %d books.' % (need_pages, bs))

    def all_marked(self):
        for item in self.books:
            if not item.is_completed:
                return False
        return True

    def get_index_number_input(self):
        while True:
            number = input('Enter the number of a book to mark as completed\n>>> ').strip()
            if len(number) == 0:
                print('Invalid input; enter a valid number')
                continue
            try:
                number = int(number)
                if number <= 0:
                    print('Number must be > 0')
                    continue
                elif number > len(self.books):
                    print('Invalid book number')
                    continue
                else:
                    return number
            except:
                print('Invalid input; enter a valid number')
                continue

    def mark_books(self):
        if self.all_marked():
            print('No required books')
            return
        self.list_book()
        index = self.get_index_number_input()
        if self.books[index - 1].is_completed:
            print('That book is already completed')
        else:
            self.books[index - 1].is_completed
            print('%s by %s completed!' % (self.books[index - 1].title, self.books[index - 1].author))

def get_title_input():
    while True:
        title = input('Title: ').strip()
        if len(title) == 0:
            print('Input can not be blank')
        else:
            return title

def get_author_input():
    while True:
        author = input('Author: ').strip()
        if len(author) == 0:
            print('Input can not be blank')
        else:
            return author

def get_pages_input():
    while True:
        pages = input('Pages: ').strip()
        if len(pages) == 0:
            print('Invalid input; enter a valid number')
            continue
        try:
            page = int(pages)
            if page > 0:
                return page
            else:
                print('Number must be > 0')
                continue
        except:
            print('Invalid input; enter a valid number')
            continue