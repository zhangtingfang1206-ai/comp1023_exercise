def lab2(x: int):
    m = [0,0]
    m[0] = "fox"
    m[1] = 34
    print(m[0])           #m[].  syntax error
                       #m[234]     index error

    sen = ["Python", "is", "very", "fun!"]
    print(sen[0][::])                 #    sen[::3]    "Python", "fun!"
    print(sen[::-2])     #"fun!", "is"
    print(sen[1923:1923]) #[](return empty list)
    print(sen[-1023:1023]) #"Pythin", "is", "very", "fun!"
    #sen[::0]     it is a ValueError

    yy = [yy for yy in m]       #another way of (shallow) copy
    print(yy)
    
    list1 = [22,33,43,52,6]
    list2 = [3,43,52,6,7]
    yy = [x for x in list1 if x in list2]
    print(yy)

    

if __name__== "__main__":
    lab2(12)