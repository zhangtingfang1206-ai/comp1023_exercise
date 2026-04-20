import random

def main():
    random_float=random.random()   #returns float in [0.0,1.0)

    my_list = [1,2,3]
    my_list[0]="turtle"    #works:["turtle",2,3].  because list is mutable
    print(my_list,random_float,sep=" ")
    #binary subtraction   2 operands
    #unary negation       1 operand


    x=int(input("give a number x:"))
    in_range1 = ((x>=3)and (x<=10))
    in_range2 = (3<=x<=10)     #same as in_range1
    print(in_range2)
    x_greater_than_1 = ((x<-1)or (x>1))
    non_zero1 = (x!=0)
    non_zero2 = not(x==0)     #same as non_zero1

    print(non_zero1)
    a=10
    b=a
    print(a is b)    #print True , "is" means if they are the same objects;caching small integers, between -5 and 256
    print(a==b)   #print True。     "==" means if they have the same value
    print(a is not b)    #print False
    print(a!=b)        #print False
    print( "des" in "desmond")        #print True
    print("Des" not in "desmond")      #print False
    print(3 in [1,2,3])      #print True
if __name__=="__main__":
    main()