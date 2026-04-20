from functools import reduce



a = [1,2,3,4,5]
result = reduce(lambda x, y: x + y, a)     
# keep reducing the number of the elements
result2 = sum(a)
print(result)
print(result2)



'''heigher level function
    map(), filter(), reduce()
'''