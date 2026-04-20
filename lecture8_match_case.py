def main():
    number1 = int(input("choose a positive number less than 20 you like: "))

    match number1:
        case 10 if number1 % 10==0 or number1*3==45:   #and:if.  or: |. 
                                      #this or is assigned to if, selecting the condition
            print("it is a great number")

        case _:
            print(f"{number1} +1 maybe a good one")


    a = ("haha", "hehe", 43)
    match a:
        case ("haha", "hehe", 43):
            print("right")
        case ("haha", "hehe", 4):
            print("yes")
        case _:
            print("not bad")

    print('yesssss') if a==("haha", "hehe", 43) else print("noooo")
    #conditional expression


if __name__=="__main__":
    main()