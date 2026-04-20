def main():
    total = 0
    number = int(input("give a posive integer: "))
    while number != -1 :
        if number % 2 == 1 :
            total += number
        number = int(input("give a posive integer: "))

    print(total)

    for i in range(10):    #from 0 to 9 meaning: give some times from 0 to 9, 10 times
        print("1023 is 1024-1")

    for i in range(2,10,2):    #start value:2, end value: 10(not including 10), size: 2
        print("yeah")      #2,4,6,8(four times)
    
    for i in range(2,10):      #8 times
        print("cool")

    for i in range(10,3,-1):    #10,9,8,7,6,5,4
        print("243")

    for a in "apple":       #5 times
        print("hello and hello")

    for i in range(5):
        if i == 3:
            continue
        print(i)
    else:             #only do NOT execute when break is executed
        print("done")
    print("End")
    
if __name__=="__main__":
    main()
