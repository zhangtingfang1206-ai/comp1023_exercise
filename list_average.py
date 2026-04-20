def main():
    total = 0.0
    counter = 0
    my_list = []     #create a empty list
    print("Enter 10 numbers, one number per line: ")
    for i in range(10):
        my_list.append(float(input()))
        total += my_list[-1]       #-1: the last element
        counter += 1
    average = total/counter     #counter can be replaced by len(my_list)
    print("Average is ", average)



    s = input("enter numbers separated by spaces: ")
    items = s.split()
    my_list2 = [float(x) for x in items]
    average2 = sum(my_list2)/len(my_list2)
    print(average2, "is the average" )

    months = ["一", "二", "三", "四"]
    number = int(input("enter a number: "))
    if 1 <= number and number <= 4:
        print("the number is ", months[number-1])
    else:
        print("ERROR")

if __name__=="__main__":
    main()