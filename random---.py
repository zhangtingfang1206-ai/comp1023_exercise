import random

def main():
    print(random.choice(['apple','banana','egg']))
    print(random.sample(range(1024),4), end=' ') #including from 0 to 1023,4 numbers
    print(random.randint(1,10))#including 1 and 10
    print(random.random())#random float from 0.0 to 1.0

    #print(*<objects>, sep=' ', end='\n', file=sys.stdout, flush=False) #end='\n' go to the next line
    print(1,0,2,3,sep='$', end='s')
    print() #\n,move to the next line
if __name__== "__main__":
    main()