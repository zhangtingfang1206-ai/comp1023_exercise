d = {45: 100, 34: 110} #key should be unique
#同一个 key 出现多次时，后面的会覆盖前面的。
print(max(d))     # dictionary -> map (just another name)
del d[34]
d['fiona'] = 110
print(d)
# different ways of defining a dictionary
my_dict1 = {}
my_dict2 = dict()

# key name arguments
my_dict3 = dict(name = "elice", id = "fiona")
my_dict4 = dict([("21234343", "Timmy"),
                 ("23245454", "Evelyn")])
my_dict5 = dict([["21234343", "Timmy"],
                 ["23245454", "Evelyn"]])
print(my_dict5)
my_dict6 = {x: x ** 2 for x in range(4)} # dictionary comprehension
print(min(my_dict6))
for key in my_dict4:
    print(key)
    print(key + ": " + str(my_dict4[key]))
for key in my_dict4.keys():
    print(key)
print()
for value in my_dict4.items():
    print(type(value))
    print(value)
my_dict7 = {key: value for key, value in my_dict6.items() if key > 2}
print(my_dict7)
print(my_dict6.get("hehe", "fiona"))   # None if no "fiona"
# print(my_dict6["hehe"])     # an error




score = {"desmond": 100, "sunny": 100}
score["james"] = 98
score["desmond"] = 101
print(score)
