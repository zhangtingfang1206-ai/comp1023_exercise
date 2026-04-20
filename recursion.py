def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def handshake(n):
    if n == 1:
        return 0
    return handshake(n-1) + n-1

def a_power_b(a, b):
    if b == 0:
        return 1
    return a * a_power_b(a, b-1)

def fibonacci(n):   
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print("The handshaking for 3 people is:", handshake(3))
print("The factorial of 5 is:", factorial(5))
print("3 to the power of 4 is:", a_power_b(2, 10))
print("The 8th number of fibonacci sequence is:", fibonacci(8))