import numpy as np

a = np.array([[11, 22, 33, 44], 
              [55, 66, 77, 88],])
e = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8]])
print(np.shape(e))
e = e.reshape(4,2)
print()
b = a[:, 2]      # 33, 77
c = a[(0,1), (2,3)]    # 33, 88 # advanced indexing / fancy indexing
d = np.expand_dims(a, axis = 2)     
print(np.shape(d))     # (2,4,1)
print(a @ e)     # works with a(2,4), e(4,2)   @ dot mulplication
f = np.zeros((1,2,3,4))
print(f)