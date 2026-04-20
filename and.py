import random

def example_function(*args: int, **kwargs: str | int) -> None:
    print("Arguments:", args, type(args))
    print("Keyword Arguments:", kwargs, type(kwargs))
    return args, kwargs


result = (lambda x, y: x + y)(1, 2)     # put only one expression
print(result)

(lambda x, y: print(x + y))(1, 3)


def check(string1):
    if 'z' and 'h' in string1:
        return bool(1)
    else:
        return 0
        

import random

def main() -> None:
    args, kwargs = example_function(1, 2, 3, name='Alice', age=30)
    print(kwargs['name'])     # Alice
    print(args[0])


    print(1.2e0)
    print(random. choice(['a', 'b']))
if __name__ == "__main__":
    main()