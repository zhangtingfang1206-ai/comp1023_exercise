def main():
    print("1+2=", 1+2, "and the type is ", type(1+2))
    x,y=3,4
    x=11
    x=y
    x+=1
    print(x,y,sep='*')
    print(False and 2/0)
    num=234_475_564_7  #equals to 2344755647，区分几位数，更方便
    num2=23.34_34      # “_” can only used between digits(数字)
    print(15/3)        #for "/"(arithmetic operators) is special, even the operands are integers, the output will always be float
    print(3*5)         #operands are int then output is int
    print(5.343//-2)
    print(5.5%-2)
    print((-1)**0.5)   #need to put 1j instead of j(single j is a variable name)
    print(232_232)     #e-7   10的-7次方


if __name__=="__main__":
    main()