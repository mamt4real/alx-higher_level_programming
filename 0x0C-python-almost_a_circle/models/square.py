from models.rectangle import Rectangle

"""Defines a square model from rectangle"""


class Square(Rectangle):
    """Square model: rectangle equal sides"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        tmp = super().__str__().split(" ")
        tmp[-1] = str(self.width)
        return " ".join(tmp)
