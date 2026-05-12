import numpy as np

# define a 3d_array
a = np.array([[[1,2],
               [3,4]],

              [[5,6],
               [7,8]]])
b = a.transpose([2,0,1])
c = a.T  # default reverse
print(b)
print(c)
print('**')
d = np.reshape(np.arange(1, 101), (2, 5, 10))
e = np.reshape(a, (2, 4))
print(e)
f = np.zeros((1,2,3,4))
print(f)
print("@@@")
#print([2,23,5] + 5)   # type eror
print([x + 5 for x in range(1, 5)])  # list comprehension