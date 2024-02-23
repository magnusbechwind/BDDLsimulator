from typing import Union


class Black:
    """
    Represents the predicate black(some_str)
    """
    type: str

    def __init__(self, type_str):
        self.type = type_str

    def __str__(self):
        return "black"

class White:
    """
    Represents the predicate white(some_str)
    """
    type: str

    def __init__(self, type_str):
        self.type = type_str

    def __str__(self):
       return "white"


class Open:
    """
    Represents the predicate "open"
    """
    type: str

    def __init__(self):
        self.type = ""

    def __str__(self):
        return "open"


class Predicate:
    """
    A predicate is either open, white(some_str) or black(some_str)
    """
    piece_type: Union[Black, White, Open]

    def __init__(self, predicate_str):
        self.piece_type = Open()

    def __str__(self):
        return str(self.piece_type)




