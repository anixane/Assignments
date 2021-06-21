from abc import abstractmethod

"""
Making an interface which have too many features is not a good idea.
Because this is like forcing the clients to define those methods which they might not even need.
"""
class Machine:
    def print(self,doc):
        raise NotImplementedError
    
    def fax(self,doc):
        raise NotImplementedError
    
    def scan(self,doc):
        raise NotImplementedError

# Above class is an interface
class SomeMultiFunctionalPrinter(Machine):
    """Here we need to define all the inherited methods explicitly"""
    def print(self,doc):
        pass
    
    def fax(self,doc):
        pass
    
    def scan(self,doc):
        pass

class OldFashionedPrinter(Machine):
    def print(self, document):
        # ok - print stuff
        pass

    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')

# Now segregate all the interfaces

"""
An abstract method is a method that is declared, but contains no implementation. 
Abstract classes may not be instantiated, and its abstract methods must be implemented by its subclasses.
"""
class Printer:
    @abstractmethod
    def print(self,document):
        pass

class Scanner:
    @abstractmethod
    def scan(self,document):
        pass

class Fax:
    @abstractmethod
    def fax(self,document):
        pass

# now inherit only those classes whose functionality we need
class MyPrinter(Printer):
    def print(self, document):
        print(document)


class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass  # something meaningful

"""
what if we need an abstract class having multiple functionalities?
"""
class MultipleFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass
    
    @abstractmethod
    def scan(self, document):
        pass

class MyMultipleFunctionalDevice(MultipleFunctionDevice):
    def __init__(self, Printer, Scanner) -> None:
        self.printer = Printer
        self.scanner = Scanner
    
    def print(self, document):
        self.printer.print(document)
    
    def scan(self, document):
        self.scanner.scan(document)

printer = OldFashionedPrinter()
printer.fax(123)  # nothing happens
printer.scan(123)  # oops!
