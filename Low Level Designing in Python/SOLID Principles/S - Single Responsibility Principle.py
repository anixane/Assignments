"""
S - Single Responsiblity Principle
A class should have its primary responsiblity and shouldn't
be doing anything else.
"""

# class for journal, it should be basicaly just doing add and remove entries in journal.
# saving, loading file, loadingFromWeb methods shouldn't be overloading this class. 
# These methods should have a different class for handling these functions. eg. PersistenceManager class
# We can add all the save and load methods in this above class.
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    """
    The __str__ method in Python represents the class objects as a string – it can be used for classes. 
    The __str__ method should be defined in a way that is easy to read and outputs all the members of the class. 
    """
    def __str__(self):
        return "\n".join(self.entries)

    # following methods breaks SRP
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()

    def load(self, filename):
        pass

    def load_from_web(self, uri):
        pass


# seperate class which stores al the save,loading methods
class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = r'c:\temp\journal.txt'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())
