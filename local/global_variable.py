X = 45

def f() -> None:
    # change x into global variable
    x = 80
    return x
# cannot access local and global at the same time
# call the function
a = f()
print(X, a, sep = "#")

