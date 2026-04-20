import copy

def main():
    mylist = [[1,2,3], [4,5,6]]
    copylist = copy. copy(mylist)
    copylist[0][0] = 88
    print(mylist)
    
    print(-2 ** 4) #int
    print(2 ** -5)
    print(1.2e1)
    print()
    a_s = 344; b = 34
    print(a_s, b)

    print([1] in (1,2,3))

    print()
    mylist1 = list[range(-23)]
    mylist2 = list(range(-23))
    print(mylist1)     #list[range(0, -23)]
    print(mylist2)    #[] print is an empty list
    
    
    numbers = [1, 2, 3]
    for num in numbers:
        numbers = [4, 5, 6]  # Doesn't affect current iteration 迭代
        print(num)
    print(numbers)    #[4, 5, 6]

    number: int = 10
    string: str = "10"
    print(number + int(string))
    print(str(number) + string)



if __name__ == "__main__":
    main()