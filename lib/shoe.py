# shoe.py

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
        self.validate_size()

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            return
        self._size = value

    def validate_size(self):
        if not isinstance(self._size, int):
            raise ValueError("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
