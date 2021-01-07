def sum(n):
    if n <= 1:
        return n
    else :
        return n + sum(n-1)

print(sum(3))

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# Fibonacci Recursion Version
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    

print(fibonacci(6))

print("---------------")
# Fibonacci Iterative Version
def fibonacci_iter(n):
    if n <= 1:
        return n
    i = 2
    first = 0
    second = 1
    result = 0
    while i <= n:
        print(f'i: {i}')
        print(f'first: {first}')
        print(f'second: {second}')
        print(f'res: {result}')
        result = first + second
        first = first + (second - first)
        second = result
        i += 1

    return result

print(f'result: {fibonacci_iter(6)}')