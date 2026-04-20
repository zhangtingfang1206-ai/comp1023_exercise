import math
from decimal import Decimal   #decimal is accurate but expensive
                              #文件名不可以和deciaml.py重复，会让python误会

def main():   
    print(0.1+0.2==0.3)      #print False
    print(math.isclose(0.1+0.2, 0.3))#print True
    print(Decimal('0.1')+Decimal('0.2')==Decimal('0.3'))#print True

if __name__=="__main__":
    main()