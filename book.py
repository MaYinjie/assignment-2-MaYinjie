class Book:
    title = ''
    author = ''
    number_of_pages = 0
    is_completed = False

    def __init__(self, *args):
        if len(args) == 0:
            args = ('', '', 0, False)
        self.title, self.author, self.number_of_pages, self.is_completed = args


    def __str__(self):
        return "{}, {}, {}".format(self.title, self.author, str(self.number_of_pages) + ' pages')


    def required(self):
        self.is_completed = False

    def completed(self):
        self.is_completed = True

    def is_long(self):
        if self.number_of_pages >= 500:
            return True
        return False
