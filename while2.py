def main():
    for i in range(4):
        for j in range (4):
            if i==j:
                continue
            elif i+j==3:
                break
            print(f"({i},{j})", end=" ")
        print()
    print(f"after all loops, i={i},j={j}")


    x=int(input("x= "))
    y=int(input("y= "))
    while x<5 and y>0:
        print(f"{x}:{y}", end=" ")
        x += 1
        y -= 2

    def check_narcissistic(num:int):
        #initial for the count
        sum = 0                         #calculate is it a narcissistic number
        temp = num                      #save for operation
        length = len(str(num))          #how many digit

        while temp>0:
            last_digit = temp%10
            sum += (last_digit ** length)
            temp = temp // 10

        if num == sum:
            print("T")
        else:
            print("F")

    start = 100


        





if __name__=="__main__":
    main()