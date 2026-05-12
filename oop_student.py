import math
import numpy as np
class student:
    def __init__(self, name, idn, cga):
        self.name = name
        self.idn = idn
        self.cga = cga

    def good_student(self):
        return self.cga > 1.5, self.idn
    
ust = student("desmond", np.array([2345351,345234523]), 4.3 )
desmond = ust
desmond.cga = 3.4

print(ust.cga)
print(ust.good_student())
print(math.pi)
