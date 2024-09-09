# book.py

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count  # Use a private attribute to manage page_count
        self.validate_page_count()

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        self._page_count = value

    def validate_page_count(self):
        if not isinstance(self._page_count, int):
            raise ValueError("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

