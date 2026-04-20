def main():
    n = int(input("give a number: "))
    for i in range(1,n+1):
        print(" "*(n-i), end="") #    print(" "*(n-i),"*"*(2*i-1))     python3.14会认为“，”是一个空格
        print("*"*(2*i-1))


    n = int(input("give a number: "))
    for i in range(1,n+1):
        print(" "*(n-i), "*"*(2*i-1), sep = "") 

 
    height = int(input("Height of the pattern: "))        # Outer loop for each line of the pattern
    for lines in range(1, height + 1):       # Inner loop to print spaces before the stars
        for a in range(1, height - lines + 1):
            print(" ", end="")       # Inner loop to print stars for the current line
        for b in range(1, 2 * lines):
            print("*", end="")       # Move to the next line after printing stars
        print()

if __name__=="__main__":
    main()