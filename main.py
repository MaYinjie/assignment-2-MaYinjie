from kivy.app import App
from bookcollection import BookCollection
from kivy.uix.button import Button
from kivy.lang import Builder
from book import Book


COLOR_REQUIRED = [1, 0, 0, 1]
COLOR_COMPLETED = [0, 1, 0, 1]
REQUIRED = False
COMPLETED = True


class MyApp(App):
    collection = BookCollection()

    def build(self):
        self.title = 'Reading Tracker 2.0'
        self.root = Builder.load_file('app.kv')
        return self.root

    def on_start(self):
        """what to do when the window is opened"""
        try:
            self.collection.load_books('books.csv')
            self.generate_book_button()
        except:
            self.root.ids.popup.open()

    def book_callback(self, value):
        """
        Callback function for book button
        :param value: The value of the selected book button
        :return:
        """
        info = ''
        for item in self.collection.books:
            flag = item.is_long()
            if str(item) == value.text:
                if item.is_completed == REQUIRED:
                    item.completed()
                    value.background_color = COLOR_COMPLETED
                    info = 'You completed' + item.title + '.'
                    if flag:
                        info = info + ' Great job!'
                else:
                    item.required()
                    value.background_color = COLOR_REQUIRED
                    info = 'You need to read' + item.title + '.'
                    if flag:
                        info = info + ' Get started!'
                self.root.ids.need_pages_label.text = 'Pages to read:' + str(self.collection.get_required_pages())
                self.root.ids.hit_label.text = info

                break

    def on_stop(self):
        """what to do when the window is closed"""
        self.collection.save_book('books.csv')

    def change_state(self, text):
        """
        Spinner's event when changing state
        :param text: the value of Spinner
        :return:
        """
        self.collection.sort(text)
        self.generate_book_button()

    def generate_book_button(self):
        """Generate book button in GridLayout"""
        self.root.ids.book_box.clear_widgets()
        length = len(self.collection.books)
        for i in range(length):
            book = self.collection.books[i]
            color = COLOR_COMPLETED
            if book.is_completed == REQUIRED:
                color = COLOR_REQUIRED

            book_button = Button(
                background_color=color,
                text=str(book),
            )
            book_button.bind(on_press=self.book_callback)
            self.root.ids.book_box.add_widget(book_button)

        self.root.ids.need_pages_label.text = 'Pages to read:' + str(self.collection.get_required_pages())

    def add_book_button_press(self, button):
        """
        Add book to system
        :param button: the button of add_book
        :return:
        """
        title_text = self.root.ids.title_input.text
        author_text = self.root.ids.author_input.text
        pages_text = self.root.ids.pages_input.text
        if title_text == '' or author_text == '' or pages_text == '':
            self.root.ids.hit_label.text = 'All fields must be completed'
            return

        try:
            pages = int(pages_text)
        except:
            self.root.ids.hit_label.text = 'Please enter a valid number'
            return
        if pages < 1:
            self.root.ids.hit_label.text = 'Pages must be > 0'
            return
        # success
        new_book = Book(title_text, author_text, pages, REQUIRED)
        self.collection.books.append(new_book)
        self.generate_book_button()
        self.root.ids.hit_label.text = 'Add book finished'

    def clear_button_press(self, button):
        """
        Clear input text
        :param button:
        :return:
        """
        self.root.ids.title_input.text = ''
        self.root.ids.author_input.text = ''
        self.root.ids.pages_input.text = ''
        self.root.ids.hit_label.text = ''

    def close_popup(self):
        """Close popup"""
        self.root.ids.popup.dismiss()


if __name__ == '__main__':
    MyApp().run()
