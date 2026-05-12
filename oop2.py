import numpy as np
class Circle:
    def __init__(self, rr, nn):     # rr represents for radius
                                    # instance variables
        self.radius = rr
        self.number = nn     #function in class is methods

    def print(self):                # instance methods
        print(self.radius)


circle1 = Circle(np.zeros((1,2)), 34)
circle1.print()
print(np.zeros((1,2)))