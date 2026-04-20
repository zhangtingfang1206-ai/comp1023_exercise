list1 = []
list2 = [range(3,6)]     #list2 = [3,4,5]
list3 = list("abcd")     #list3 = ['a','b','c','d']
list4 = [2,3,"three",4,5,6,7,8,9,12,34]

#print(list4[-2])       
#list4[-1]refers to the last elements, lists4[-2] refers to the last two one
#list4 = [ 2,    3,      "three"]

#          0,    1,         2
#          -3,   -2,        -1     no more things like -4

list5 = list4 * 3
print(list4[2:6])    #2345
print(list3[3])
a = [1,2,3,4]
print(a[0:1900])      #print: [1,2,3,4]

list6 = [1,4,3]
list7 = [1,2,3,4,5,6,7,8,9]
print(list6 > list7)
"""i=0
while i < len(list4):
    print(list4[i])
    i += 1"""


mylist = ['a','b','c','d','e']    #len(mylist) = 5

print(mylist[2:5:2])#[start: end: step]2,4.   c,e

for i in range(len(mylist)):       #0,1,2,3,4
    mylist[i] = i
    print(mylist[i], end=" ")
#     0   1   2   3   4  5 6 7   len(b) = 8
