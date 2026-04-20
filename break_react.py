import random

def main():
    area = 100.0
    while area > 50.0:
        length = float(input("Enter length of rect: "))
        if length < 5.0:
            break
        width = float(input("Enter width of rect: "))
        if width < 5.0:
            break
        area = length * width
        print("The area =", area)
    print(random. choice(('a', 'b', 'asdf')))

if __name__=="__main__":
    main()