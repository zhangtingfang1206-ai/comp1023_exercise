def main():
# Assume the input value of n is greater than
# or equal to 0.
    n = int(input("Enter value of n: "))
    if n == 0:
        result = 1
    else:
        result = n
        for i in range(n-1, 0, -1):      #also ok with (2,n) or (1,n)
            result *= i
    print("The factorial of", n, "is", result)


    while True:
        number = float(input("input a number +ve number:"))
        if number<=0:
            print("try again")
        else:
            print("good!")
            break

    while True:
        user_input = input("Enter a positive number: ")#string
        if user_input.isdigit() and int(user_input) > 0: 
            #isdigit: 用于查看输入的string是不是数字，34，-34，etc.-3.133不是digit
            break
        print("Invalid input. Please try again.")
    print("Valid input received.")


    total = 0
    print("Enter 8 numbers")
    for i in range(8):
        data = int(input("Enter number {}: ".format(i + 1)))
        if data < 0:
            continue
        total += data
    print("The sum =", total)


if __name__ == "__main__":
    main()
