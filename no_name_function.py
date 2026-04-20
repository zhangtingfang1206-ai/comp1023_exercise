def do_something(f, x, y):
    print(f(x, y))

do_something(lambda x, y: x + y, 10, 20)
do_something(lambda x, y: x - y, 10, 20)
do_something(lambda x, y: x * y, 10, 20)



result = (lambda x, y: x + y)(1, 2)     # put only one expression
print(result)

print((lambda x: x & 1 == 12)(x = 4))

a = [1,2,3,4,5,6]
b = list(filter(lambda x: x >= 4, a))     # filter: select something from the list
print(b)

'''iterable: tuple, lists, dictionary, sets
iterable is something you can use loop
'''