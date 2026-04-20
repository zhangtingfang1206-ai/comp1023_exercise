a = [1,2,3,4,5,6]
b = list(map(lambda x: x + 2, a))      # map something to something
                        # filter: select something from the list
print(b)

marks = ['345', '456', '345', 45]
marks_int = list(map(lambda x: int(x), marks))
print(marks_int)