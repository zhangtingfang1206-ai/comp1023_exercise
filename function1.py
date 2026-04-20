def haah(x, y):
    for i in range(x):
        print("applee")
    for j in range(y):
        print("GG")
    return j

def add(a:int, b:int) -> int:    #return: ->     a and b: formal parameters
                                                   # a,b: parameter list
    sum = a+b
    return sum

def main():
    haah(3,4)
    print()
    print()
    print(haah(2,3))  #return can also be printed
    print(add(3,4))
if __name__=="__main__":
    main()




