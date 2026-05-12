import numpy as np

class Student:
    def __init__(self, desmond):
        self.__name = 'g'  # two _ _ only allow internal methods can access
                           # new name: _Student__name
        self._age = 4
        self.instructor = desmond

    def print(self):
        print(self.__name)
    def get_score(self):
        score = np.array(([2,3,4],
                          [4,5,6],
                          [7,8,9]))
        return score[self.age]

your = Student("mark")
print(your.instructor)