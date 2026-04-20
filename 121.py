def main():
    print(-17.5%3)      #remainder= a-(a//b)*b
    '''-17.5//3 == -6.0
        -17.5-(-6.0)*3 == 0.5
        '''
    print("The result of 10 - 20 is", 10 - 20) # Subtraction
    print("This is",-3) # Negation
    '''
    The operator- is used as both a binary subtraction operator and a unary negation
    operator.
    The binary subtraction operator takes 2 operands (e.g., 10 - 20).
    The unary negation operator takes 1 operand (e.g.,-3).
    '''

    #result= 5/0   #zero division error\in run time error. same: 5//0, 5%0, 
    result2= 0**0
    print(result2)              #0**0=1
    #evaluate = process = find the result for the expression = 
    # The process of obtaining the value of an expression is called evaluation.
    radius = 5
    print (radius <= 0)#False

    
if __name__=="__main__":
    main()