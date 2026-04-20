def increment(n: int) -> None:
    n += 1
    print("n inside the function is", n)
    return n

x = 45  # Global variable


def main() -> None:
    x: int = 1
    print("Before the call, x is", x)
    increment(x)     # positional arguments,   put x = at before
    print("After the call, x is", x)
if __name__ == "__main__": main()

'''
all the keywords arguments should be put on the right
all the default  arguments should be put on the right
REMEMBER: all the arguments with "=" sign should be put on the right
'''

