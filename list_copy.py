import copy      #a document called "copy.py"

x = [1,2,[3,4]]

a = x

y = copy.copy(x)  #function
#y = x.copy()     #method, another way to do the shallow copy
#y = list(x)
z = copy.deepcopy(x)

x[2][1] = 999

print(y[2][1])     #999. shallow copy, x modified, y MAY does
print(z[2][1])     #4.   deep copy, x modified, z not
print(a is x)      #T
print(y is x)      #F