class Student:
    def __init__(self):
        self.__name = 'g'  # two _ _ only allow internal methods can access
                           # new name: _Student__name
        self._age = 34
    def print(self):
        print(self.__name) 

desmond = Student()
desmond.print()
print(desmond)
desmond.__name = 'sdfg'
desmond.id = 313
print(desmond.__name)
print(desmond.id)
print(desmond)