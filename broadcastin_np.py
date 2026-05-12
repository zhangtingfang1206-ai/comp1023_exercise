import numpy as np

# print([1,2,3,4]+5)    type error 
print([x + 5 for x in range(1, 5)])  # list comprehension
print(np.array([1,2,3,4])+4)         # same answer
