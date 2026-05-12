import numpy as np
a: np.ndarray = np.array([[7, 8],
                          [9, 10],
                          [11, 12]])
print(a[[0,0,1,2],[0,1,1,1]])
print(type(a))
b = np.array([1,0,1])
print(a[np.arange(3), b])  # == a[[0, ,1, 2], [1, 0, 1]]
print(a[np.arange(3), b] + 5)    # add 5 to every elements
print()
bool_idx: np.ndarray = (a < 10)
print(bool_idx)
print(a[bool_idx])      # same as line 14
print(a[(a < 10) & (a > 0)])    # | for 'or'; & for 'and'; ~ for 'not'
z = np.array([+3, -4], dtype = np.int32)
print(z.dtype)
x: np.ndarray = np.array([[2, 4], 
                          [6, 8]])
y: np.ndarray = np.array([[1, 3], 
                          [5, 7]])
print(x @ y)     # matmul
print(np.matmul(x, y))
print(x. dot(y))
c = np.full((4, 4), 4)
c[2] = 3
print(c)
print()
d = np.eye((3)); print(d)
e = np.array([[3,4,5],
              [6,7,8],
              [9,10,11]])
f = np.array([3,2,5])
print(e.T)
print(f)
print(np.shape(e.reshape(1,9)))