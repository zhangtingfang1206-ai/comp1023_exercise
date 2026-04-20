b = ['a','b','c','d','e',7,9,1]     # lists' best friend is for loop
for i in b:
    print(i, end=" ")
print()
for i in range(0,len(b),4):         # = for i in range (0,8,4).   0, 4
    print(i, end="")

print()

#enumerate function:
for index, item in enumerate(b):
    print(f"{index}:{item}", end = " ")
print()
for hellokitty, mickie in enumerate(b):
    print(f"{hellokitty}:{mickie}", end = " ")
    print(hellokitty, mickie, sep=":")


#list comprehensions: use one list to build another list. 
haha = [1,2,3,4,5,6,7,8]
#then you want to produce [1,9,25,49]
list2 = [ x*x for x in haha if x%2==1]
print(list2)

list3 = [x for x in range(3)]
print(f"list3 is {list3}")

user = ["123", "456", "789"]
user_int = [int(x) for x in user]     #transfer float into integers   type: str -> int
print(user)
print(user_int)




#methods: 
s = "    heheheheheh    "
s = s.strip()
print(s)


user = ["123", "456", "789"]
x = input()
user.append(x)
print(user)  

#sets, dictionary, list they are mutable

'''a = [1, 2, 3, 4, 5, 6]
   b = [1000, 999]
   a[2:2] = b       meaning the first element of b will have the index 2 in a
   print(a)'''