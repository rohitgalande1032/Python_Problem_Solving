def factorial(number):
    fact = 1

    for num in range(1, number+1):
        fact = fact*num
    return fact

# Factorial using recursion
def recursive_factorial(n):
    if n == 0:
        return 1
    return n * recursive_factorial(n - 1 )

print(factorial(5))
print(recursive_factorial(5))