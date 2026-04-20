def dudu():
    return 'a', 'b'    #packing

def give_me_five():
    return 3,

dd, jj = dudu()        #unpacking
print(give_me_five())    

names: tuple[str] = ("Alex", "Cecia", "Desmond")
scores: tuple[float] = (100, 90, 80)
result = zip(names, scores)
print(tuple(result))      #(('Alex', 100), ('Cecia', 90), ('Desmond', 80))
print(list(result))