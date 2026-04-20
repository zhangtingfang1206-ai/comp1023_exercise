import math

def main():

    value=float("3e34")
    print(value)

    x=math.pi
    y=math.tan(x)
    print(y)         #-1.22*10^-16    (e-16) a number which is close to 0
    print(type(4**95))
    var1 = var2 = var3 = 10
    var1 += 10
    var2 -= 3
    var3 %= 5
    print(type(var3))

    sources = cources="comp 1023"
    cources = "comp","1023","tuple"      #it is a tuple, a species which is like a list
    print(type(cources))
    print(cources)

    google=["apple", "banana"]
    print(type(google))                #it is a list
    print(google)                    

if __name__=="__main__":
    main()