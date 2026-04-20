def main():
    yours=int(input("Enter your score: "))
    his = int(input("Enter your friend's score: "))
    if yours > his:
        print("haha you win!")
    elif yours == his:
        print("you have the same score!")
    else:
        print("haha you lose!")


    a="123"
    b="3"
    print(b in a)   #True

    a = "a"
    print(id(a))

    major = str(input())
    print(bool(major == "math" or "cpeg"))      #boolean expression,output is "True" or "False"
    print(major == "math" or "cpeg")            #output is "True" or "cpeg"

if __name__=="__main__":
    main()