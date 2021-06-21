"""
This principle is basically on prohibition of using cached value for calculation.
"""

class Rectangle:
    def __init__(self,width,height) -> None:
        self._width = width
        self._height = height
    
    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width=value
    
    @height.setter
    def height(self,value):
        self._height=value

    @property
    def area(self):
        return self._width * self._height

def useRectangle(rc):
    w = rc.width
    rc.height = 10  # unpleasant side effect
    expected = int(w*10)
    print(f'Expected an area of {expected}, got {rc.area}')

rc = Rectangle(2, 3)
useRectangle(rc)
# Expected an area of 20, got 20

class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        _width = _height = value

sq = Square(5)
useRectangle(sq)
# Expected an area of 50, got 25
