from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL=1
    MEDIUM=2
    LARGE=3

class Product:
    def __init__(self,name,color,size) -> None:
        self.name = name
        self.color = color
        self.size = size

"""
This following class breaks the open-closed principle as we are modifying in the base class itself.
open-close principle:
    open for extension
    closed for modification

PS: we cant specify filters for all the combinations in the base class itself
"""
class ProductFilter:
    def filter_by_color(self,products,color):
        for product in products:
            if product.color == color: 
                yield product
    
    def filter_by_size(self,products,size):
        for product in products:
            if product.size == size: 
                yield product
    
    def filter_by_size_and_color(self,product,size,color):
        for product in products:
            if product.size == size and product.color==color:
                yield product

apple = Product('Apple', Color.GREEN, Size.SMALL)
tree = Product('Tree', Color.GREEN, Size.LARGE)
house = Product('House', Color.BLUE, Size.LARGE)

products = [apple, tree, house]

pf = ProductFilter()
print('Green products (old):')
for p in pf.filter_by_color(products, Color.GREEN):
    print(f' - {p.name} is green')

"""
Let's try to design keeping open-closed principle in mind.
"""
class Filter:
    def __init__(self) -> None:
        pass

class specification:
    def isSatisfied(self,item):
        pass

class colorSpecification(specification):
    def __init__(self,color) -> None:
        self.color=color
    
    def isSatisfied(self, item):
        return item.color==self.color

class sizeSpecification(specification):
    def __init__(self,size) -> None:
        self.size=size
    
    def isSatisfied(self, item):
        return item.size==self.size

class BetterFilter(Filter):
    def filter(self,items,spec):
        for item in items:
            if spec.isSatisfied:
                yield item

bf = BetterFilter()
green = colorSpecification(Color.GREEN)
print('Green products (new):')
for p in bf.filter(products,green):
    print(f' - {p.name} is green')
