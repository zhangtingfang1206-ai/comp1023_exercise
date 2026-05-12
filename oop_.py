# 面向对象 / 物件 object-oriented programming

import numpy as np
class Person:  # variable, methods
    def __init__(self):
        self.name = "Hehe"
        self.age = 98
        self.gender = 'M'

Desmond = Person()

james = Person()
print(Desmond is james)# False
james.name = "Lala"
james.age = 34
print(james)
print(Desmond.age)

